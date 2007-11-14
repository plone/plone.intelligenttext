Intelligent text
================

Started by Martin Aspeli
 
This package contains a and a transform (for example for
portal_transforms in CMF) that is capable converting plain text into
HTML where line breaks and indentation is preserved, and web and email
addresses are made into clickable links.

Basic usage
-----------

The basic usage is turning intelligenttext into html:
 
    >>> from plone.intelligenttext.transforms import convertWebIntelligentPlainTextToHtml
    >>> text = 'Go to http://plone.org'
    >>> convertWebIntelligentPlainTextToHtml(text)
    'Go to <a href="http://plone.org" rel="nofollow">http://plone.org</a>'

And the other way around:

    >>> from plone.intelligenttext.transforms import convertHtmlToWebIntelligentPlainText
    >>> html = 'Go to <a href="http://plone.org" rel="nofollow">http://plone.org</a>'
    >>> convertHtmlToWebIntelligentPlainText(html)
    'Go to http://plone.org'


Intelligent text to html
------------------------

We can get a hyperlink.  We always add rel="nofollow" to make this
less interesting for spammers.

    >>> orig = "A test http://test.com"
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'A test <a href="http://test.com" rel="nofollow">http://test.com</a>'

An email address should be clickable too:

    >>> orig = "A test test@test.com of mailto"
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'A test <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a> of mailto'

Text, links and email addressed can be split over multiple lines.

    >>> orig = """A test
    ... URL: http://test.com End
    ... Mail: test@test.com End
    ... URL: http://foo.com End"""
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'A test<br />URL: <a href="http://test.com" rel="nofollow">http://test.com</a> End<br />Mail: <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a> End<br />URL: <a href="http://foo.com" rel="nofollow">http://foo.com</a> End'


Having the links at the end of the line should not have adverse effects.

    >>> orig = """A test
    ... URL: http://test.com
    ... Mail: test@test.com
    ... URL: http://foo.com"""
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'A test<br />URL: <a href="http://test.com" rel="nofollow">http://test.com</a><br />Mail: <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a><br />URL: <a href="http://foo.com" rel="nofollow">http://foo.com</a>'

    
Indentation should be preserved.

    >>> orig = """A test
    ...   URL: http://test.com
    ...     Mail: test@test.com
    ...       URL: http://foo.com"""
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'A test<br />&nbsp;&nbsp;URL: <a href="http://test.com" rel="nofollow">http://test.com</a><br />&nbsp;&nbsp;&nbsp;&nbsp;Mail: <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;URL: <a href="http://foo.com" rel="nofollow">http://foo.com</a>'
    >>> convertWebIntelligentPlainTextToHtml(orig).count('&nbsp;')
    12

HTML entities should be escaped.

    >>> orig = "Some & funny < characters"
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'Some &amp; funny &lt; characters'

Accentuated characters, like in French, should be html escaped.

    >>> orig = "The French use é à ô ù à and ç."
    >>> convertWebIntelligentPlainTextToHtml(orig)
    'The French use &eacute; &agrave; &ocirc; &ugrave; &agrave; and &ccedil;.'

Links with ampersands in them should be handles correctly.

    >>> orig = "http://sourceforge.net/forum/forum.php?thread_id=1719815&amp;forum_id=47987"
    >>> convertWebIntelligentPlainTextToHtml(orig)
    '<a href="http://sourceforge.net/forum/forum.php?thread_id=1719815&amp;amp;forum_id=47987" rel="nofollow">http://sourceforge.net/foru[&hellip;]9815&amp;amp;forum_id=47987</a>'

XXX Actually, this is wrong.  We should check for unescaped ampersands
like in "?question=all&answer=42".  But we leave that for the moment.


We want to make sure that the text representation of long urls is not too long.

    >>> url0 = "http://verylonghost.longsubdomain.veryverylongdomain.com/index.html"
    >>> convertWebIntelligentPlainTextToHtml(url0)
    '<a href="http://verylonghost.longsubdomain.veryverylongdomain.com/index.html" rel="nofollow">http://verylonghost.longsub[&hellip;]rylongdomain.com/index.html</a>'
    >>> url1 = "http://www.example.com/longnamefortheeffectofsuch/thisisalsolong/hereisthelastrealroot/thisisanotherpage.html"
    >>> convertWebIntelligentPlainTextToHtml(url1)
    '<a href="http://www.example.com/longnamefortheeffectofsuch/thisisalsolong/hereisthelastrealroot/thisisanotherpage.html" rel="nofollow">http://www.example.com/[&hellip;]/thisisanotherpage.html</a>'
    >>> url2 = "https://secure.somehost.net/a/path/logout.do;jsessionid=0FB57237D0D20D377E74D29031090FF2.A11"
    >>> convertWebIntelligentPlainTextToHtml(url2)
    '<a href="https://secure.somehost.net/a/path/logout.do;jsessionid=0FB57237D0D20D377E74D29031090FF2.A11" rel="nofollow">https://secure.somehost.net[&hellip;]0D20D377E74D29031090FF2.A11</a>'
