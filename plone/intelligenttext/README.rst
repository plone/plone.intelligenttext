Intelligent text
================

This package contains a transform that is capable converting plain text into HTML.

Line breaks and indentation are preserved, and web and email addresses are made into clickable links.

Intended use is for example for portal_transforms in CMF.

Basic usage
-----------

The basic usage is turning intelligenttext into html::

    >>> from plone.intelligenttext.transforms import convertWebIntelligentPlainTextToHtml
    >>> text = 'Go to http://plone.org'
    >>> bprint(convertWebIntelligentPlainTextToHtml(text))
    Go to <a href="http://plone.org" rel="nofollow">http://plone.org</a>

And the other way around::

    >>> from plone.intelligenttext.transforms import convertHtmlToWebIntelligentPlainText
    >>> html = 'Go to <a href="http://plone.org" rel="nofollow">http://plone.org</a>'
    >>> bprint(convertHtmlToWebIntelligentPlainText(html))
    Go to http://plone.org


Intelligent text to html
------------------------

We can get a hyperlink.
We always add rel="nofollow" to make this less interesting for spammers::

    >>> orig = "A test http://test.com"
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    A test <a href="http://test.com" rel="nofollow">http://test.com</a>

An email address should be clickable too::

    >>> orig = "A test test@test.com of mailto"
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    A test <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a> of mailto

Some basic fallback would be nice::

    >>> bprint(convertWebIntelligentPlainTextToHtml(None))

Text, links and email addressed can be split over multiple lines::

    >>> orig = """A test
    ... URL: http://test.com End
    ... Mail: test@test.com End
    ... URL: http://foo.com End"""
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    A test<br />URL: <a href="http://test.com" rel="nofollow">http://test.com</a> End<br />Mail: <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a> End<br />URL: <a href="http://foo.com" rel="nofollow">http://foo.com</a> End


Having the links at the end of the line should not have adverse effects::

    >>> orig = """A test
    ... URL: http://test.com
    ... Mail: test@test.com
    ... URL: http://foo.com"""
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    A test<br />URL: <a href="http://test.com" rel="nofollow">http://test.com</a><br />Mail: <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a><br />URL: <a href="http://foo.com" rel="nofollow">http://foo.com</a>


Indentation should be preserved::

    >>> orig = """A test
    ...   URL: http://test.com
    ...     Mail: test@test.com
    ...       URL: http://foo.com"""
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    A test<br />&nbsp;&nbsp;URL: <a href="http://test.com" rel="nofollow">http://test.com</a><br />&nbsp;&nbsp;&nbsp;&nbsp;Mail: <a href="&#0109;ailto&#0058;test&#0064;test.com">test&#0064;test.com</a><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;URL: <a href="http://foo.com" rel="nofollow">http://foo.com</a>
    >>> convertWebIntelligentPlainTextToHtml(orig).count(b'&nbsp;')
    12

HTML entities should be escaped::

    >>> orig = "Some & funny < characters"
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    Some &amp; funny &lt; characters

Accentuated characters, like in French, should be html escaped::

    >>> orig = "The French use é à ô ù à and ç."
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    The French use &eacute; &agrave; &ocirc; &ugrave; &agrave; and &ccedil;.

Links with ampersands in them should be handled correctly::

    >>> orig = "http://google.com/ask?question=everything&answer=42"
    >>> bprint(convertWebIntelligentPlainTextToHtml(orig))
    <a href="http://google.com/ask?question=everything&amp;answer=42" rel="nofollow">http://google.com/ask?question=everything&amp;answer=42</a>

We want to make sure that the text representation of long urls is not too long::

    >>> url0 = "http://verylonghost.longsubdomain.veryverylongdomain.com/index.html"
    >>> bprint(convertWebIntelligentPlainTextToHtml(url0))
    <a href="http://verylonghost.longsubdomain.veryverylongdomain.com/index.html" rel="nofollow">http://verylonghost.longsub[&hellip;]rylongdomain.com/index.html</a>
    >>> url1 = "http://www.example.com/longnamefortheeffectofsuch/thisisalsolong/hereisthelastrealroot/thisisanotherpage.html"
    >>> bprint(convertWebIntelligentPlainTextToHtml(url1))
    <a href="http://www.example.com/longnamefortheeffectofsuch/thisisalsolong/hereisthelastrealroot/thisisanotherpage.html" rel="nofollow">http://www.example.com/[&hellip;]/thisisanotherpage.html</a>
    >>> url2 = "https://secure.somehost.net/a/path/logout.do;jsessionid=0FB57237D0D20D377E74D29031090FF2.A11"
    >>> bprint(convertWebIntelligentPlainTextToHtml(url2))
    <a href="https://secure.somehost.net/a/path/logout.do;jsessionid=0FB57237D0D20D377E74D29031090FF2.A11" rel="nofollow">https://secure.somehost.net[&hellip;]0D20D377E74D29031090FF2.A11</a>

If there is a url in brackets, the link should not contain one of the brackets::

    >>> bracket_url = "<http://plone.org/products/poi/issues/155>"
    >>> bprint(convertWebIntelligentPlainTextToHtml(bracket_url))
    &lt;<a href="http://plone.org/products/poi/issues/155" rel="nofollow">http://plone.org/products/poi/issues/155</a>&gt;

Port numbers should be recognized as linkworthy::

    >>> url = "http://plone3.freeman-centre.ac.uk:8080/caldav"
    >>> bprint(convertWebIntelligentPlainTextToHtml(url))
    <a href="http://plone3.freeman-centre.ac.uk:8080/caldav" rel="nofollow">http://plone3.freeman-centre.ac.uk:8080/caldav</a>

localhost should be good::

    >>> url = "http://localhost:8080/"
    >>> bprint(convertWebIntelligentPlainTextToHtml(url))
    <a href="http://localhost:8080/" rel="nofollow">http://localhost:8080/</a>

Check ip numbers too while we are at it::

    >>> url = "http://127.0.0.1:8080/"
    >>> bprint(convertWebIntelligentPlainTextToHtml(url))
    <a href="http://127.0.0.1:8080/" rel="nofollow">http://127.0.0.1:8080/</a>
    >>> bprint(convertWebIntelligentPlainTextToHtml("http://255.255.255.255"))
    <a href="http://255.255.255.255" rel="nofollow">http://255.255.255.255</a>
    >>> bprint(convertWebIntelligentPlainTextToHtml("http://0.0.0.0"))
    <a href="http://0.0.0.0" rel="nofollow">http://0.0.0.0</a>


ftp is accepted::

    >>> bprint(convertWebIntelligentPlainTextToHtml("ftp://localhost"))
    <a href="ftp://localhost" rel="nofollow">ftp://localhost</a>

https is accepted::

    >>> bprint(convertWebIntelligentPlainTextToHtml("https://localhost"))
    <a href="https://localhost" rel="nofollow">https://localhost</a>

URLs at the end of sentences are recognized::

    >>> sentence = "Go to http://some.webpa.ge."
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Go to <a href="http://some.webpa.ge" rel="nofollow">http://some.webpa.ge</a>.
    >>> sentence = "Visit http://some.webpa.ge?"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Visit <a href="http://some.webpa.ge" rel="nofollow">http://some.webpa.ge</a>?
    >>> sentence = "Follow http://some.webpa.ge!"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Follow <a href="http://some.webpa.ge" rel="nofollow">http://some.webpa.ge</a>!

URLs with trailing slashes at the end of sentences are recognized::

    >>> sentence = "Go to http://some.webpa.ge/."
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Go to <a href="http://some.webpa.ge/" rel="nofollow">http://some.webpa.ge/</a>.
    >>> sentence = "Visit http://some.webpa.ge/?"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Visit <a href="http://some.webpa.ge/" rel="nofollow">http://some.webpa.ge/</a>?
    >>> sentence = "Follow http://some.webpa.ge/!"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Follow <a href="http://some.webpa.ge/" rel="nofollow">http://some.webpa.ge/</a>!

URLs with GET arguments at the end of sentences are recognized::

    >>> sentence = "Go to http://some.webpa.ge/with/?get=arguments."
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Go to <a href="http://some.webpa.ge/with/?get=arguments" rel="nofollow">http://some.webpa.ge/with/?get=arguments</a>.
    >>> sentence = "Visit http://some.webpa.ge/with/?get=arguments?"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Visit <a href="http://some.webpa.ge/with/?get=arguments" rel="nofollow">http://some.webpa.ge/with/?get=arguments</a>?
    >>> sentence = "Follow http://some.webpa.ge/with/?get=arguments!"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Follow <a href="http://some.webpa.ge/with/?get=arguments" rel="nofollow">http://some.webpa.ge/with/?get=arguments</a>!

URLs with named anchors at the end of sentences are recognized::

    >>> sentence = "Go to http://some.webpa.ge/with/named/#anchors."
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Go to <a href="http://some.webpa.ge/with/named/#anchors" rel="nofollow">http://some.webpa.ge/with/named/#anchors</a>.
    >>> sentence = "Visit http://some.webpa.ge/with/named/#anchors?"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Visit <a href="http://some.webpa.ge/with/named/#anchors" rel="nofollow">http://some.webpa.ge/with/named/#anchors</a>?
    >>> sentence = "Follow http://some.webpa.ge/with/named/#anchors!"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Follow <a href="http://some.webpa.ge/with/named/#anchors" rel="nofollow">http://some.webpa.ge/with/named/#anchors</a>!

You can put URLs in brackets to explicitly add punctuation marks to it::

    >>> sentence = "Go to <http://some.webpa.ge/with/named/#anchors.>"
    >>> bprint(convertWebIntelligentPlainTextToHtml(sentence))
    Go to &lt;<a href="http://some.webpa.ge/with/named/#anchors." rel="nofollow">http://some.webpa.ge/with/named/#anchors.</a>&gt;

Unicode should be fine too::

    >>> text = u"Línk tö http://foo.ni"
    >>> bprint(convertWebIntelligentPlainTextToHtml(text))
    L&iacute;nk t&ouml; <a href="http://foo.ni" rel="nofollow">http://foo.ni</a>

Leading whitespace is converted to non breaking spaces to preserve indentation::

    >>> text = "Some text.\n    And some indentation."
    >>> bprint(convertWebIntelligentPlainTextToHtml(text))
    Some text.<br />&nbsp;&nbsp;&nbsp;&nbsp;And some indentation.

Leading tabs are converted to spaces.  The default is ``4``::

    >>> text = "Before the tab:\n\tand after the tab."
    >>> bprint(convertWebIntelligentPlainTextToHtml(text))
    Before the tab:<br />&nbsp;&nbsp;&nbsp;&nbsp;and after the tab.

You can specify a different tab width::

    >>> bprint(convertWebIntelligentPlainTextToHtml(text, tab_width=2))
    Before the tab:<br />&nbsp;&nbsp;and after the tab.

In case the tab width is not an integer, we try to convert it::

    >>> bprint(convertWebIntelligentPlainTextToHtml(text, tab_width='2'))
    Before the tab:<br />&nbsp;&nbsp;and after the tab.

When that fails we fall back to 4 spaces::

    >>> bprint(convertWebIntelligentPlainTextToHtml(text, tab_width='1.5'))
    Before the tab:<br />&nbsp;&nbsp;&nbsp;&nbsp;and after the tab.


Html to intelligent text
------------------------

We want the transform to work the other way around too.
For starters this means that tags must be stripped::

    >>> orig = "Some <b>bold</b> text."
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    Some bold text.

Some basic fallback would be nice::

    >>> bprint(convertHtmlToWebIntelligentPlainText(None))

Line breaks need to be handled.::

    >>> orig = "Some<br/>broken<BR/>text<br />"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    Some
    broken
    text

Starting blocks::

    >>> orig = "A block<dt>there</dt>"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    A block
    <BLANKLINE>
    there

Ending blocks::

    >>> orig = "<p>Paragraph</p>Other stuff"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    Paragraph
    <BLANKLINE>
    Other stuff

Indenting blocks::

    >>> orig = "An<blockquote>Indented blockquote</blockquote>"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    An
    <BLANKLINE>
      Indented blockquote

Lists::

    >>> orig = "A list<ul><li>Foo</li><li>Bar</li></ul>"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    A list
    <BLANKLINE>
      - Foo
        - Bar

Non breaking spaces::

    >>> orig = "Some space &nbsp;&nbsp;here"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    Some space   here

Angles::

    >>> orig = "Watch &lt;this&gt; and &lsaquo;that&rsaquo;"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    Watch <this> and &#8249;that&#8250;

Bullets::

    >>> orig = "A &bull; bullet"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    A &#8226; bullet

Ampersands::

    >>> orig = "An &amp; ampersand"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    An & ampersand

Entities::

    >>> orig = "A &mdash; dash"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    A &#8212; dash

Pre formatted text::

    >>> orig = "A <pre>  pre\n  section</pre>"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    A
    <BLANKLINE>
      pre
      section

White space::
    >>> orig = "A \n\t spaceful, <b>  tag-filled</b>, <b> <i>  snippet\n</b></i>"
    >>> bprint(convertHtmlToWebIntelligentPlainText(orig))
    A spaceful, tag-filled, snippet


Credits
-------

- Started by Martin Aspeli
- Contributions from the Plone Community
