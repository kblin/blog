Title: Samba4 DNS sprint, day 5 summary
Date: 2012-03-31 00:04
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: samba4-dns-sprint-day-5-summary
Status: published

Another long and only partially successful day is behind me, and my
allocated time for this sprint is over.
I said "partially successful", because I did not manage to get GSS-TSIG
working. This is mostly due to the fact that
I don't understand how to hook it up to GENSEC/gss on the Samba side.
The API is a bit confusing to the uninitiated.
What I did get done was to get to a point where incoming TKEY messages
are parsed and checked, and pretty much handled correctly.
We currently bail out of there with a BADKEY error, pretending the
client's key didn't work. If someone with a reasonable grasp of
GENSEC would explain what I need to do there to get the GSSAPI blob from
the client authenticated, I would expect GSS-TSIG is very, very close.

Because it's the end of the week let me take a look at the high and low
points of this sprint over the week:

- High point: On Tuesday morning, I finally got forwarding sorted out.
  Ever since Tuesday, all DNS requests on my dev machine were handled
  by my local samba server.
- Low point: I wasted most of Tuesday trying to debug my HMAC-MD5
  signing code. Debugging crypto is hard, because the only debug tool
  available is "stare at the code and think very hard". This might be
  the weapon of choice of the kernel community, but certainly not my
  preferred way of doing things.
- High point: On Wednesday morning, I managed to fix signing of
  TSIG requests.
- Low point: This got me work on TSIG some more instead of moving on
  to GSS-TSIG, and ultimately failed because signing of TSIG replies
  doesn't work correctly yet, another day wasted.
- Low point: After reading up on TKEY and GSS-TSIG, I realized that I
  didn't really understand what I had to do in Samba to get this
  sorted out. This ended up being a major stumbling block, in fact I'm
  still stuck there.
- High point: During my tries to find a useful test for TKEY, I set up
  a Win7 client for my domain, and after a tiny fix to get PTR records
  handled in the update code, that machine would correctly register
  forward and reverse zones (without crypto, but also without
  complaining), and was perfectly happy using samba's DNS service for
  it's needs.

So to sum up, forwarding turned out to be a neater feature than I
initially expected it to be, and allows me to run samba as my main name
server for the local network. On the negative side, all that fancy
crypto stuff isn't working yet. I do feel that none of these is really
far off anymore. Maybe another pair or two of eyes would help there.
I've updated the [Samba Wiki
DNS](https://wiki.samba.org/index.php/DNS#Internal_DNS) page to reflect
the current status.
