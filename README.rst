plone.intelligenttext
=====================

Overview
--------

Provides transforms from ``text/x-web-intelligent`` to ``text/html`` and vice versa.

Line breaks and indentation are preserved, and web and email addresses are made into clickable links.
Links get a ``rel="nofollow"`` to make this less interesting for spammers.

This package works in pure Python 2.7 and 3.0 and has no dependency on Plone.
