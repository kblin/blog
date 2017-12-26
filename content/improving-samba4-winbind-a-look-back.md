Title: Improving Samba4 winbind, a look back
Date: 2007-09-19 08:01
Author: Kai Blin
Category: Samba
Tags: GSoC, Samba
Slug: improving-samba4-winbind-a-look-back
Status: published

### What the project is about
Samba4 contains a basic winbind implementation, but it is still lacking
many features. The goal of my project was to improve Samba4 winbind so
that the nsswitch and pam functionality provided by Samba3's winbindd
would be present in Samba4, too.

Simply copying code over from Samba3 would not do, of course, as the
underlying architecture in Samba4 is different. Also, the goal was to
improve readability of the code, as opposed to the more organically
"grown" look of the Samba3 winbindd code.

In Samba4, there is a library taking care of user/group management
called libnet. Samba4 winbind uses this library extensively.

### What was done so far

-  Porting nsstest to Samba4
   nsstest is a binary that test basic functionality of a
   nsswitch library. Once all the tests in nsstest work for
   libnss\_winbind from Samba4, the winbind implementation is useable.
-  Getting information about users / SIDs
   This is the basic nsswitch getpwnam/getpwuid functionality returning
   a pwent structure. It is also possible to query for AD / NT domain
   information about the user/sid.
-  User listing / enumeration
   nsswitch provides a set of functions (setpwent/getpwent/endpwent) to
   iterate over a password database. The classic database is the
   /etc/passwd file, but of course using nsswitch, it's possible to use
   a directory like LDAP or AD.
-  Mapping SIDs to user ids and back
   This one is only stubbed out, as Samba4 doesn't handle that
   mapping yet. However, functions for this were needed to make winbind
   work, so I had to stub these out. The advantage is that the other
   code will automagically start to work correctly once these functions
   are implemented for real.
-  Mapping SIDs to group ids and back
   Much the same applies here, once idmapping is supported in Samba4,
   this will be replaced by real code.

### What is left to do

- Group enumeration
  The libnet functions for group enumeration were not implemented by
  the time GSoC was up. Now these functions are in, so support for
  groups identical to the user functions will follow soon.
-  NTLM caching
  Due to time constraints, caching of NTLM blobs was discarded. The
  nsswitch/pam functionality was regarded as core importance.
-  PAC/info3 caching
  As with NTLM caching, PAC/info3 caching was discarded. Caching is
  only interesting once the other features are working and will be
  implemented eventually.
- Automated tests
  Currently the only way to test all of the functionality is to wrap
  the wbinfo binary and let that take care of constructing the
  necessary winbind queries. This is a bit clumsy. Jerry Carter is
  currently working on a winbind client library that will allow to
  access the functionality of wbinfo without a wrapper. The tests will
  be implemented using that API once it is in the tree.

### Future (related) work
First of all, the features still left on the TODO list will be
implemented. Group functions first, testing next if possible. There is
more to winbind than this GSoC project was about, so the more missing
features will be implemented. The caching will follow once the other
features are working and tested.

An improved winbind will help Samba4 to not only act as an AD controller
but also as a domain member.

### A look back
Complying with long-standing computer science tradition, I
underestimated the amount of work that had to be done before I could
start working on the actual features I was planning to implement. In the
end I had to prioritize features and drop the least important ones to
get finished in time. I did not expect to spend so much time figuring
out my way around the libnet code.

However, the foundation for implementing the dropped features is laid,
so I do not feel too bad about it. Samba4 winbind already works better
than before. Pending group support and id mapping, it will be usable for
simple scenarios.

### Conclusions
I still need to be more careful about the scheduling of projects and
estimating the amount of work required to get features to work. Still,
the only way to improve is to try and adjust the estimations
accordingly. I feel more confident around the Samba4 code now, thanks to
Metze, Jelmer and Andrew's help. Of course thanks to all the other team
members for the help and advice offered, on IRC and the mailing lists.
Last but not least I would like to thank Google in general and Leslie
Hawthorn in particular for running the third Summer of Code program in
an efficient manner, making this a really enjoyable experience.
