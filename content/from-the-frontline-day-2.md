Title: From the frontline, day 2
Date: 2011-08-09 07:41
Author: Kai Blin
Tags: flask, testing, war on legacy code
Slug: from-the-frontline-day-2
Status: published


Looks like my system strikes back. A fitting thing to happen for an
episode 2, I guess. Turns out that `nosetests` and `virtualenv` need
some extra care and feeding when kept together. Installing another copy
of nosetests into my virtualenv fixed the test failures I was seeing.
Thanks to the folks on \#python and \#pocoo for pointing me the right
way.

Of course this broke the code coverage. Nothing a
`pip install --upgrade coverage` wouldn't fix, though. As an added
bonus, the coverage html output now looks much nicer. I guess it was
redesigned between whatever my system got and the version pip grabbed.

Of course, after spending quite some time writing tests for my email
sending module, the \#pocoo folks point me at the already existing
[Flask-Mail](http://packages.python.org/flask-mail) extension, that
integrates into the Flask test harness (as in, if you're testing, it
won't send email) already. Oh well. Switched, ditched quite some code
and corresponding tests. Even less stuff I have to maintain myself.


Unfortunately, Flask-Mail doesn't seem to like it when you switch on
`app.config['TESTING'] = True` after initialization. Fortunately, you
can still fiddle with the value used so it doesn't try sending emails,
like so:

```python
def setUp(self):
    webapp.app.config['TESTING'] = True
    webapp.mail.suppress = True
```

The key here is the `mail.suppress = True` setting.
Once that's done, all the testing options work as expected. You can even
have a look at the msg objects that would have been sent using the
following snippet:

```python
def test_sent_mail(self):
    """Test if emails were generated and sent correctly"""
    with webapp.mail.record_messages() as outbox:
        rv = self.app.post('/send-email',
                 data=dict(message="hello world"))
        assert len(outbox) == 1
        msg = outbox[0]
        assert "hello world" in msg.body
```

I like it, this really gets all the stuff I do under test in a very
straightforward manner.
