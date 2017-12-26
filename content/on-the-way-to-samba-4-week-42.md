Title: On the way to Samba 4, week 42
Date: 2010-10-27 06:19
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: on-the-way-to-samba-4-week-42
Status: published

This is the first installment of my hopefully regular progress reports
on the things I did last week to get Samba 4 closer to a stable release.

The biggest piece of work certainly was finally pushing the DNS server
implementation. Yes, that's correct, Samba 4 now has it's own DNS
server. So far, all it does is serve out resource records from AD that
it's authoritative for. You need to sync over the LDAP entries from
another AD DC as well. Still, that's a good start, and thanks to the
existing infrastructure in Samba4, it was possible to do all of this in
about 1000 lines of code.
Features still missing from the DNS server so far:

-  Recursive query support (needs a DNS resolver library, working
   on that)
-  Support for update requests so clients can update their own entries
-  On provisioning, we need to pre-load the database with a couple of
   DNS records

You can see a broad overview of the todo items for the DNS server in
`source4/dns_server/TODO`.
