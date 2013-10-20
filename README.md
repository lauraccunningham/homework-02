homework-02
===========
Due October 21, 2013

**Recent Quakes**
----

Vertical Group, #2
-----
_Name ( [GitHub Account Homepage](https://github.com) )_
  - Laura CUNNINGHAM ( [lauraccunningham](https://github.com/lauraccunningham) )            
  - David LAU ( [davidopluslau](https://github.com/davidopluslau) )
  - Ashley SIA ( [ashleysia](https://github.com/ashleysia) )
  - Sherry XIA ( [xsherryxia](https://github.com/xsherryxia) )

Step-by-Step Instructions for Homework-02
-----

**GOAL**

.

**Parameters**

- .
- .
- .

_Earthquake data can be found [here](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) and at the right, the appropriate feed can be chosen for this assignment.  For our purposes, we will be choosing the data for [all earthquakes in the past 30 days](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson)_

**To Begin, Preliminary Steps**

You will need to first open your Virtual Machine.  Log in, and get it running!  From here type in the following commands as we want to make sure you are able to run iPython Notebook and all necessary packages.

    sudo apt-get install libgeos-3.3.3 python-mpltoolkits.basemap python-mpltoolkits.basemap-data python-mpltoolkits.basemap-doc python-pandas

Open a new directory within your virtual machine.  Here is where I am going to store my information for homework-02 and enter this directory.  From here we will open our iPython Notebook.

    mkdir homework-02
    ls
    cd homework-02
    ipython notebook --ip=0.0.0.0 --no-browser --script --pylab=inline


From here we will now be able to run and operate out iPython Notebook.  Within your browser (ie. Safari) type into your bar `127.0.0.1:7777` to open the iPython Dashboard.  Here you should be all set to begin, and in the correct location for **homework-02**.

**Curation, Analysis, & Visualization**

.

Our Final Project: [Repository](https://github.com/lauraccunningham/homework-02
) & [Notebook Viewer](http://nbviewer.ipython.org/urls/raw.github.com/lauraccunningham/homework-02/master/?.ipynb)

==========

[Final Projects & Presentations](https://github.com/stat157/recent-quakes/wiki/How-To-Submit-Your-Homework)

==========

Objective
----
The first objective of this assignment is to improve the data handling of the code by upgrading from the deprecated data source to the new data source which uses a different data format called [JSON](http://en.wikipedia.org/wiki/JSON).

Since we are working with live data we also need to cache the data so that we can reliably re-run the code using the same data (or optionally with the live data).

The second objective is that we would like to be able to see data for earthquakes in states other than Alaska, so the next part of the assignment requires [refactoring](http://en.wikipedia.org/wiki/Code_refactoring) the code to parameterize the function definition instead of relying on the hard-coded values for latitude and longitude of the bounding box around the region of interest.

This assignment features two main roles: the Data Curator and the Visualizer. All 4 members of your vertical group should work together no matter what individual roles you have assigned.

Your task
---------

1) Data Curation

The USGS [eqa7day-M1.txt data
url](http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt)
used in this program has been deprecated.

As suggested by the warning message in the data feed:

    This USGS data file has been deprecated. To continue receiving
    updates for earthquake information you must switch to the new data
    format [http://earthquake.usgs.gov/earthquakes/feed/]. In the
    future, data feeds will be updated and deprecated following our
    official deprecation policy
    [http://earthquake.usgs.gov/earthquakes/feed/policy.php].

you need to upgrade this program to use the new USGS data feed:

http://earthquake.usgs.gov/earthquakes/feed/

The new data feed includes a link for [Programmatic
Access](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
You should use the [pandas JSON
parser](http://pandas.pydata.org/pandas-docs/dev/io.html) to read the
data instead of the `read_csv` function in the original code.

You will also need to find a way to cache the data locally so that
your runs are exactly reproducible since the live data gets updated in
real-time. You should write a program which can use the live data, but
also optionally can store data from previous runs so that we can
re-run the program in either mode using *cached data* or *live data*.

Start simple, keep the data isolated/separate from the source code,
and remember that the goal is to make it reproducible by someone else.

**The duty of the Data Curator is to write a new version of the code
that reproduces the same output as the old version of the code, but
using the new data source.** Note, it may *not* be possible to do that
exactly if the new data and the old data are substantially different,
but hopefully they are exact in content, and differ only in format
(CSV vs JSON).

2) Visualization

The definition of `plot_ak()` has a *very bad code smell*! What if we
want to plot the earthquakes in California where I live now instead of
in my home state of Alaska? Can you spot the *code smell*? How can you
fix it so that given any arbitrary list of earthquakes you can plot
the bounding box around the location (e.g. the whole state) where the
quakes occured?

**The duty of the Visualizer is to refactor the hard-coded values out
of the program and instead parameterize the function so that for any
list of earthquakes in a particular region (i.e. California) it will
generate a map showing the correct location.** Instead of including
the lat/lon bounding box values in the body of the program you might
consider storing that data in some format on disk and read it back
into the program as a dataframe to pass to the function as a
parameter.

Also plot the quakes so we can see the magnitude and depth of each dot
instead of the way they are plotted now which only shows the location;
all the dots are the same color and the same size, but could be varied
to represent more information in the same amount of space.
