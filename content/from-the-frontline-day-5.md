Title: From the frontline, day 5
Date: 2011-08-12 07:16
Author: Kai Blin
Tags: testing, war on legacy code
Slug: from-the-frontline-day-5
Status: published

Another day, another piece of testing mayhem. I've completed the 0.1
version of my
[Flask-Downloader](http://pypi.python.org/pypi/Flask-Downloader/0.1)
helper class. With this, I could complete my web app. Now, the
downloader itself has a bunch of tests to make sure it's working as
expected, but I was also going to test the corresponding code paths in
the web app's tests.
The user can provide the input either by uploading a file or by giving
an accession number. Testing for the file uploads was easy, as the Flask
test client accepts file-like objects as data input for POST requests.
So testing the app will do the right thing is as easy as:

```python
def test_upload(self):
    file_handle = open(tmp_filename)
    data = dict(file=file_handle)
    rv = self.client.post('/upload', data=data)
    assert "upload succeeded" in rv.data
```

Assuming your upload function listens on '/upload' and returns a page
that contains "upload succeeded", of course.


Testing file downloads is a bit more elaborated, because I don't
actually want my downloader to connect to the internet during a test
run. Minimock to the rescue! I can fake the download helper and create
the same kind of output to fool the application code.

```python
from minimock import Mock
from werkzeug import FileStore
def test_download(self):
    data = dict(id="FAKE")
    # now create the fake downloader
    tmp_file = open(tmp_file_path)
    dl.download = Mock('dl.download')
    dl.download.mock_returns = FileStore(stream=tmp_file)
     rv = self.client.post('/download', data=data)
    assert "download succeeded" in rv.data
```

With similar assumptions as in the example before, and also the idea
that you have a pre-existing file in `tmp_file_path`. A StringIO
file-like object should do the trick as well.

With all the tests in place and a test coverage of 100%, I declare this
campaign a success. I still need to deploy the new web app on my test
server instead of the old one, but I'm going to do that next week. I
will also continue my war on legacy code, now tackling the pieces that
do the actual work. No war is over as quick as you'd initially hope
after all. Also, I'm pretty sure the 100% code coverage don't mean
there's not plenty of places for bugs to hide in, just that at least all
of the code is looked at by the interpreter once. Still, it's a good
conclusion to a busy week. Testing rocks.
