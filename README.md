homework-02
===========
Due October 07, 2013

**Questionnaire Data Wrangling**
----

Vertical Group, #2
-----
_Name                       Email                           GitHub Username             Duty_
  - Laura CUNNINGHAM            lccunningham@berkeley.edu       [lauraccunningham](https://github.com/lauraccunningham)            Producer              
  - David LAU                   davidopluslau@berkeley.edu      [davidopluslau](https://github.com/davidopluslau)               Integrator
  - Ashley SIA                  lorraineh@berkeley.edu          [ashleysia](https://github.com/ashleysia)                   Entrepreneur
  - Sherry XIA                  x_sherry_xia@berkeley.edu       [xsherryxia](https://github.com/xsherryxia)                  Administrator


Horizontal Group, Producers (Analyzers)
-----
_Name                       Email                           GitHub Username_
  - Laura Catherine CUNNINGHAM  lccunningham@berkeley.edu       lauraccunningham
  - Yee Tung MAN                aliceman@berkeley.edu           amx01
  - Alyssa Janine PARKER        alyssaparker@berkeley.edu       aparker92
  - John RISKO                  snowstorm1@berkeley.edu         johnrisko
  - Teresa R TENFELDER          teresatenfelder@berkeley.edu    teresita
  - Khoa Quang Dang TRAN        khoatran@berkeley.edu           kqdtran
  - David WANG                  davidwang001@berkeley.edu       davidwang001
  - Tay WON SHIN                taywonshin@berkeley.edu         taywon
  - Qi ZHANG                    qi.zhang@berkeley.edu           qi-zhang	
  - Jody ZHANG                  jodyzhang@berkeley.edu          j-zhang

_Data for the questionnaire can be found at: http://goo.gl/Cplm9O_

Objective
----
You will use the Stat 157 Questionnaire data that you will access using the Google API. Your primary objective is to visualize data from two columns of the spreadsheet data: 1) the column labeled "What is your learning style?" and 2) any other column of your choosing that you feel helps give us insight into the people in the class.

The data that we have available in the spreadsheet comes from the real world, which means the data is **dirty**. Your job before you visualize the data is to clean it up and transform it into a form that the analyzers and visualizers in your group can use.

Specifically, this is the data that YOU submitted via the Google Form as part of the Questionnaire for this course so we can better understand you, your skills, and where you're headed after you graduate. All identifying data has been redacted from this data!

Any questions regarding the homework can be found [here](https://github.com/stat157/questionnaire/issues).


Preliminary Setup Steps
-----------------------
You'll need to follow these steps on your virtual machine to do data wrangling for this assignment:

    sudo apt-get install ipython ipython-notebook python-pip
    sudo pip install gspread

Then copy the example config file to your home directory, but named
`stat157.cfg` like this:

    cp example.cfg ~/stat157.cfg

Use a programming text editor to edit the example config file
`~/stat157.cfg` such as:

    vi ~/stat157.cfg

Edit the `~/stat157.cfg` config file so it will use your full @berkeley username, e.g.: `foobear@berkeley.edu`. The password should be your [bConnected key](https://kb.berkeley.edu/campus-shared-services/page.php?id=27226).

NOTE: Do **NOT** put your actual password into example.cfg! And definitely **DO NOT** check it into github!

**UPDATE:** You might also be wondering [How to save your edit in vi](https://github.com/stat157/questionnaire/issues/3).

Use `example.ipynb` in this repository as a starting point to access the Google Spreadsheet data. You should run the IPython Notebook in your virtual machine using this command:

    ipython notebook --no-browser --ip=0.0.0.0

You can auto-generate a .py file from your IPython Notebook using an additional argument:

    ipython notebook --no-browser --ip=0.0.0.0 --script

Sometimes it is convenient to easily track changes between versions of your script by checking in changes made to the script in git since the iPython Notebook is hard to inspect using a text editor instead of a browser.

Hints For Success
-----------------
To be successful you will need to collaborate within your horizontal (11 person) AND vertical (4 person) groups.

You have a better chance of succeeding with this assignment by running `git commit` frequently on your local system and by running `git push` often. If you're not sure what this means or have any questions, use resources such as GitHub Help, StackOverflow, IRC, and other resources that we configured in the first weeks of the class.

Keep notes about your process. If you are not able to make your process reproducible by the deadline then you should be able to provide notes about the errors, confusions, and other roadblocks that you encountered.

Also, keep track of those "Aha!" moments and share those with others in the class.
