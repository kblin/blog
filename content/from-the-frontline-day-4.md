Title: From the frontline, day 4
Date: 2011-08-11 11:24
Author: Kai Blin
Tags: testing, war on legacy code
Slug: from-the-frontline-day-4
Status: published

Today, I decided to go for the downloader component that can download
files on the behalf of the users. While looking at how to test this, I
actually noticed that the `mm_unit` functionality has been merged into
the `minimock` package. Sweet.
I wanted to keep this modular, a downloader sounds like a tool I could
use in a couple of projects. So I created a Flask extension. There's a
nice wizard script that automates the creation of the boilerplate files.
Using the wizard, I created
[Flask-Downloader](https://github.com/kblin/flask-downloader). It's
pretty straightforward to use. There's a `download(url)` function that
will return a `werkzeug.FileStorage` instance, just like the flask
upload hander. I'll also add a `save(url)` function that'll save the
url's contents to a file without returning a file-like object.


Not too much to write about, spent a lot of time researching stuff
today. Hope to get done with my changes tomorrow. Let's see how that'll
work out.
