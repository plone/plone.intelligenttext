Changelog
=========


2.2 (2017-08-04)
----------------

New:

- Recognizes URLs embedded at the end of sentences.
  The punctuation mark of the sentence is split from the URL.
  Use brackets to force punctuation marks at the end of URLs.
  [tarnap]

Fixes:

- Use pyenv for installing python versions on Travis.
  [Rotonen]


2.1.0 (2015-10-27)
------------------

New:

- Make compatible with Python 3.
  [davisagli]

Fixes:

- Minor cleanup (pep8, readability, ReST)
  [jensens]


2.0.3 (2015-05-11)
------------------

- Minor cleanup: whitespace, git ignores.
  [gforcada, rnix]


2.0.2 (2013-01-01)
------------------

- Allows an easy way to extend the converter through subclassing.
  One might want to override the regexps, or modify the HTML that one of
  the replace* methods produces.
  https://github.com/plone/plone.intelligenttext/pull/1
  [dnouri]

- Add MANIFEST.in.
  [WouterVH]


2.0.1 - 2010-07-18
------------------

- Update license to GPL version 2 only.
  [hannosch]


2.0 - 2010-06-13
----------------

- Package metadata cleanup.
  [hannosch]


2.0a1 - 2009-04-04
------------------

- Specify package dependencies.
  [hannosch]


1.0.3 - 2009-04-09
------------------

- Handle windows line endings.
  [elro]

- URLs in html really should have the ampersand quoted.
  [elro]

- Specify package dependencies.
  [hannosch]


1.0.2 - 2008-07-17
------------------

- When convertWebIntelligentPlainTextToHtml is called with an explicit tab_width
  we try to make an integer of that ('2' -> 2). When that fails we use the default of 4.
  [maurits]

- Minor change in code path, really only to get 100 percent test
  coverage.
  [maurits]


1.0.1 - 2007-12-04
------------------

- Accept ip addresses as valid urls.
  [maurits]

- Accept localhost as valid url.
  [maurits]

- Recognize urls with port numbers as links.
  Fixes http://plone.org/products/poi/issues/156
  [maurits]

- If there is a url in brackets, the link should not contain one of the brackets.
  Fixes http://plone.org/products/poi/issues/155
  [maurits]

- Fix error where ampersands in urls would get html escaped.
  Refs http://plone.org/products/poi/issues/101
  [maurits]

- Accept input of None to our transforms.
  [maurits]

- Add unit tests (mostly taken from Products.intelligenttext).
  [maurits]


1.0 - 2007-08-15
----------------

- Released version 1.0.
  [diefenbach]


1.0b2 - 2007-05-07
------------------

- Some documentation cleanup.
  [hannosch]


1.0-beta1 - 2007-04-07
----------------------

- Move into plone namespace and integration to PloneTransforms and
  MimetypesRegistry/
  [diefenbach]


0.1
---

- Initial development by Martin Aspeli (optilude@gmx.net). For further
  informations see http://dev.plone.org/collective/browser/intelligenttext/

- The transform was originally based on the url_to_hyperlink transform from
  Ploneboard by Plone Solutions and others.

- Initial package structure.
  [zopeskel]
