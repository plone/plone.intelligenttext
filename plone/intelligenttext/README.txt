Intelligent text
================

Started by Martin Aspeli
 
This package contains a and a transform (for example for
portal_transforms in CMF) that is capable converting plain text into
HTML where line breaks and indentation is preserved, and web and email
addresses are made into clickable links.

The basic use is this:
 
    >>> from plone.intelligenttext.transforms import convertWebIntelligentPlainTextToHtml
    >>> text = 'Go to http://plone.org'
    >>> convertWebIntelligentPlainTextToHtml(text)
    'Go to <a href="http://plone.org" rel="nofollow">http://plone.org</a>'

And the other way around:

    >>> from plone.intelligenttext.transforms import convertHtmlToWebIntelligentPlainText
    >>> html = 'Go to <a href="http://plone.org" rel="nofollow">http://plone.org</a>'
    >>> convertHtmlToWebIntelligentPlainText(html)
    'Go to http://plone.org'
