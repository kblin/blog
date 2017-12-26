Title: On the way to Samba 4, week 46
Date: 2010-11-24 22:05
Author: Kai Blin
Category: Samba
Tags: Samba
Slug: on-the-way-to-samba-4-week-46
Status: published

Really not much time to work on Samba this week. So I didn't get around
to really debug the failing echo test for quite a while. Then tridge
pointed out that I was trying to use a connected UDP socket as if it was
not connected, and things started to work like a charm.

It doesn't look like I'll have much more time during week 47. Hopefully
I will get around to clean up the patches and push my example anyway.
