homework-02
===========
Due October 07, 2013

**Questionnaire Data Wrangling**
----

Vertical Group, #2
-----
_Role -- Name ( [GitHub Account Homepage](https://github.com) )_
  - Administrator -- Sherry XIA ( [xsherryxia](https://github.com/xsherryxia) )
  - Producer -- Laura CUNNINGHAM ( [lauraccunningham](https://github.com/lauraccunningham) )            
  - Entrepreneur -- Ashley SIA ( [ashleysia](https://github.com/ashleysia) )
  - Integrator -- David LAU ( [davidopluslau](https://github.com/davidopluslau) )

Step-by-step Instructions for Homework-02
-----

**GOAL**

To see if there is a relationship between the VARK Scores and suggested roles as opposed to the projected roles within groups we see ourselves as.  To look at the columns "What type of Learning Style?" and the following four columns, we were able to identify where we are perceived and how we perceive ourselves along the spectrum of group members.

**Parameters**

-	Types of VARK Scores: Aural, Visual, Read/Write, Kinesthetic
-	Group Roles: Administrator, Producer, Entrepreneur, Integrator
-	Responses: Always, Sometimes, Often, Not Often

_Data from the Questionnaire can be found at: http://goo.gl/Cplm9O_

**To Begin**

You will need to first open your Virtual Machine.  Log in, and get it running!  From here type in the following commands as we want to make sure you are able to run iPython Notebook, and the necessary functions for claiming data from the Questionnaire data on the Google Document shared to us via our Professor.

    sudo apt-get install ipython ipython-notebook python-pip
    sudo pip install gspread

From here we will ne cloning the `example.cfg` file from the standard class repository [_Questionnaire_](https://github.com/stat157/Questionnaire).  We want to places these files into our home directory named as `stat157.cfg` like this:

    cp example.cfg ~/stat157.cfg

Use a programming text editor to edit the example config file
`~/stat157.cfg` such as:

    vi ~/stat157.cfg

To edit this way, you will need to understand how to you `vi` and how to change the mode to edit.  We will need to be changing the email and username along with the correct [bConnected key](https://kb.berkeley.edu/campus-shared-services/page.php?id=27226).

**Curation**	SHERRY

**Analysis**

From the Curator's data, we used `git clone` to transfer our `dataCuration.ipynb` file into our virtual machine.

In opening our virtual machine, we have run the commands `git clone http://github.com/lauraccunningham/homework-02.git`. This copied our GitHub repository over to the virtual machine.

Now, we need to make sure that when we open our iPython Notebook, we are in the correct directory.  To make sure of this, go through your basic UNIX commands to move around until in the right directory.  In our case, the necessary commands were `ls` to understand where we are in our machines, and `cd homework-02/` to move into the correct folders within our machines.

To open the iPython Notebook, run `ipython notebook --ip=0.0.0.0 --no-browser` and open _127.0.0.1:7777_ in a browser.  Here you should see within the `homework-02` repository all necessary and up to date files from GitHub.
Using basic Python syntax, you can continue to parse and examine the data.  We used a basic **for loop** to run through all of the data and determine sums, lengths, and averages of each of the four VARK scores, and prevelance of the student responses.  Building this into a dictionary made it much more consise.

**Visualization**	ASHLEY

**Presentation**	DAVID

==========
==========

Objective
----
You will use the Stat 157 Questionnaire data that you will access using the Google API. Your primary objective is to visualize data from two columns of the spreadsheet data: 1) the column labeled "What is your learning style?" and 2) any other column of your choosing that you feel helps give us insight into the people in the class.

The data that we have available in the spreadsheet comes from the real world, which means the data is **dirty**. Your job before you visualize the data is to clean it up and transform it into a form that the analyzers and visualizers in your group can use.

Specifically, this is the data that YOU submitted via the Google Form as part of the Questionnaire for this course so we can better understand you, your skills, and where you're headed after you graduate. All identifying data has been redacted from this data!

Any questions regarding the homework can be found [here](https://github.com/stat157/questionnaire/issues).

Hints For Success
-----------------
To be successful you will need to collaborate within your horizontal (11 person) AND vertical (4 person) groups.

You have a better chance of succeeding with this assignment by running `git commit` frequently on your local system and by running `git push` often. If you're not sure what this means or have any questions, use resources such as GitHub Help, StackOverflow, IRC, and other resources that we configured in the first weeks of the class.

Keep notes about your process. If you are not able to make your process reproducible by the deadline then you should be able to provide notes about the errors, confusions, and other roadblocks that you encountered.

Also, keep track of those "Aha!" moments and share those with others in the class.