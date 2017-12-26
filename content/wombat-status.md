Title: WOMBAT status
Date: 2008-08-03 21:19
Author: Kai Blin
Category: WorldForge
Tags: WOMBAT, WorldForge
Slug: wombat-status
Status: published

Hi folks,

development around WOMBAT hasn't really slowed down, despite the lack of
releases recently. We're currently working hard on bringing the back-end
data model into a shape that will allow us to add more features to
WOMBAT more easily.

I'm currently busy writing a svn xml parser that will load the metadata
into a SQL database, instead of relying on files like we used to. This,
together with a major overhaul of the overal design of the data model,
gives us better integration with the SVN backend.

A next step in this design will be tracking svn updates file by file
instead of forcing a re-scan of the whole data set.

Stay tuned for updates.
