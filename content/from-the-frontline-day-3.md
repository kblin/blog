Title: From the frontline, day 3
Date: 2011-08-10 07:21
Author: Kai Blin
Tags: testing, war on legacy code
Slug: from-the-frontline-day-3
Status: published


Today, I decided to go and restructure my webapp into a package as
recommended by the [Flask "Larger Applications"
pattern](http://flask.pocoo.org/docs/patterns/packages/). Thanks to my
existing test suite, the move was quick and pain-free. I had to fix
imports in one of the tests, but apart from that, the only thing I had
to do was splitting up the webapp.py file correctly into
webapp/\_\_init\_\_.py, webapp/views.py and webapp/models.py.


I then started playing with implementing the actual functionality for
uploading files and creating database entries for the jobs submitted.
Took a while to get this right, never done database stuff with Flask
before. But again, pretty easy to set up tests for all this. Also, I
discovered [Flask-Testing](http://packages.python.org/Flask-Testing/),
making flask unit testing even more comfy. Just had to fix up the
[Twill](http://twill.idyll.org/) module Flask-Testing comes with to not
use the md5 and sha modules, triggering deprecation warnings. Will
continue to write the last tests for the job submission form tomorrow,
and then see how to deal with making the web app download data from
elsewhere for the user.
