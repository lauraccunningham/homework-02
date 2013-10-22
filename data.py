# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# homework-02: recent-quakes

# <headingcell level=3>

# step 1

# <headingcell level=4>

# import packages and earthquake data

# <codecell>

import urllib
import json
from pandas import read_csv
import pandas as pd
from time import gmtime, strftime, strptime, ctime
from cPickle import load, dump
from pprint import pprint
from datetime import date
from datetime import datetime

# <codecell>

#Locate earthquake data of interest from the USGS website: http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php


URL_45_WEEK = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson' # earthquake data of magnitude 4.5+ that's been updated in the past 7 days
URL_1_WEEK = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson' # earthquake data of magnitude 1.0+ that's been updated in the past 7 days
URL_1_HOUR = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson' # earthquake data of magnitude 1.0+ that's been updated in the past hour

def getEarthquakeFilename():
    now = datetime.now()
    timeStr = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    timeZone = 'PST'
    name = 'earthquakeData'+ "_" + str(date.today()) + "_" + timeStr + "_" + timeZone + '.dict'
    return name

def usgsTimeExtraction(earthquake, humanReadable = True):
    """Takes in an earthquake (dictionary) and extracts the time from it, in seconds since the epoch (float)"""
    time = earthquake['properties']['time']
    if humanReadable:
        return usgsTimeConversion(time)
    return time

def usgsTimeConversion(time):
    """Takes in the seconds since the epoch (float) and returns a human readable time."""
    humanReadableTime = gmtime(float(str(time)[0:10]))
    return strftime("%a %b %d %H:%M:%S %Y", humanReadableTime)

def getEarthquakeDataframe(fileLocation = None, isUrl = True, save = False):
    """Get earthquake JSON from FILELOCATION, depending on if it ISURL, and can SAVE data as pickle if data is live.
    Defaults to magnitude 1+ earthquakes in last week."""
    if fileLocation is None:
        isUrl = True
        fileLocation = URL_1_WEEK
    if isUrl:
        print fileLocation
        earthquakeJson = json.loads(urllib.urlopen(URL_1_WEEK).read())
        if save:
            with open(getEarthquakeFilename(), 'wb') as filename:
                dump(earthquakeJson, filename)
    else:
        with open(fileLocation, 'rb') as filename:
            earthquakeJson = load(filename)    
    earthquakeDataframe = pd.DataFrame(earthquakeJson.items())

    earthquakes = earthquakeDataframe[1][1]
    srcList = []
    eqidList = []
    versionList = []
    dateTimeList = []
    latList = []
    lonList = []
    magList = []
    nstList = []
    regionList = []

    for earthquake in earthquakes:
        srcList.append(earthquake['properties']['sources'])
        eqidList.append(earthquake['properties']['code'])
        versionList.append(1)
        dateTimeList.append(usgsTimeConversion(earthquake['properties']['time']))
        latList.append(earthquake['geometry']['coordinates'][1])
        lonList.append(earthquake['geometry']['coordinates'][0])
        magList.append(earthquake['properties']['mag'])
        nstList.append(earthquake['properties']['nst'])
        regionList.append(earthquake['properties']['place'])

    reducedEarthquakeData = {
        'Source': srcList,
        'Eqid': eqidList,
        'Version': versionList,
        'Datetime': dateTimeList,
        'Lat': latList,
        'Lon': lonList,
        'Magnitude': magList,
        'NST': nstList,
        'Region': regionList
    }
    reducedEarthquakeDataframe = pd.DataFrame(reducedEarthquakeData)
    return reducedEarthquakeDataframe

# <headingcell level=3>

# step 3

# <headingcell level=4>

# visualizations

# <headingcell level=4>

# *** these are other people's - to be seen as examples of what can be done, not what we are doing exactly.  you both should fix something interesting that maps the depth, magnitude, and location of the these earthquakes. maybe we can make darker colored dots for deeper quakes and larger dots for higher magnitude placed on a state map. ***

# <headingcell level=5>

# a. group #2's mapping program

# <codecell>

# Now let's just focus on earthquakes in Alaska (my home state! :)

# <codecell>
earthquakeDataframe = getEarthquakeDataframe()

# <codecell>

def getEarthquakesFromLocation(earthquakeDataframe, region = "California"):
    """When you enter a city or state into this function, it will output a data frame containing that region"""
    regionQuakes = earthquakeDataframe[earthquakeDataframe.Region.str.contains(region)]
    return regionQuakes

alaskaQuakes = getEarthquakesFromLocation(earthquakeDataframe, "Alaska")
caliQuakes = getEarthquakesFromLocation(earthquakeDataframe)

# <codecell>

# <codecell>

from mpl_toolkits.basemap import Basemap

ALASKA_DISPLAY = {
                     'regionName' : "Alaska",
                     'llcrnrlon' : -180,
                     'llcrnrlat' : 50.,
                     'urcrnrlon' : -120.,
                     'urcrnrlat' : 72,
                     'resolution' : 'l',
                     'area_thresh' : 1000.,
                     'projection' : 'merc',
                     'lat_0' : 62.9540,
                     'lon_0' : -149.2697
                }

CALI_DISPLAY = {
                     'regionName' : "California",
                     'llcrnrlon' : -130,
                     'llcrnrlat' : 30.,
                     'urcrnrlon' : -110.,
                     'urcrnrlat' : 45,
                     'resolution' : 'l',
                     'area_thresh' : 1000.,
                     'projection' : 'merc',
                     'lat_0' : 36.1700,
                     'lon_0' : -119.7462
                }

StateParams = {
                   'Alaska' : ALASKA_DISPLAY,
                   'California' : CALI_DISPLAY
               }
EARTHQUAKE_DISPLAY_PARAM_FILE = 'earthquake_display_param_file.json'

def plot_quakes(quakes, display):
    """Plot QUAKES dataframe from the dictionary with DISPLAY parameters"""
  #  with open(EARTHQUAKE_DISPLAY_PARAM_FILE, 'rb') as filename:
  #      earthquakeDisplayParamDict = load(filename)
  #  if isinstance(display, str):
  #      displayParams = earthquakeDisplayParamDict[display]
  #  else:
    displayParams = display
   #     earthquakeDisplayParamDict[display['regionName']] = display
   #     with open(getEarthquakeFilename(), 'wb') as filename:
   #         dump(earthquakeJson, filename)
            
    m = Basemap(llcrnrlon=displayParams['llcrnrlon'],
                llcrnrlat=displayParams['llcrnrlat'],
                urcrnrlon=displayParams['urcrnrlon'],
                urcrnrlat=displayParams['urcrnrlat'],
                resolution=displayParams['resolution'],
                area_thresh=displayParams['area_thresh'],
                projection=displayParams['projection'],
                lat_0=display['lat_0'],
                lon_0=display['lon_0'])
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='coral',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    x, y = m(quakes.Lon, quakes.Lat)
    for lon, lat, size in zip(x, y, quakes.Magnitude):
        m.plot(lon, lat, 'go', linewidth = size)
    return m

plot_quakes(caliQuakes, CALI_DISPLAY)

# <codecell>


