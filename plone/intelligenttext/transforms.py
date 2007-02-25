from htmlentitydefs import entitydefs
import re

def convertWebIntelligentPlainTextToHtml(orig, data=None, tab_width=4, **kwargs):
    """Converts text/x-web-intelligent to text/html
    """
    urlRegexp = re.compile(r'((?:ftp|https?)://(?:[a-z0-9](?:[-a-z0-9]*[a-z0-9])?\.)+(?:com|edu|biz|org|gov|int|info|mil|net|name|museum|coop|aero|[a-z][a-z])\b(?:\d+)?(?:\/[^;"\'<>()\[\]{}\s\x7f-\xff]*(?:[.,?]+[^;"\'<>()\[\]{}\s\x7f-\xff]+)*)?)', re.I|re.S|re.U)
    emailRegexp = re.compile(r'["=]?(\b[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}\b)', re.I|re.S|re.U)
    indentRegexp = re.compile(r'^(\s+)', re.M|re.U)
    
    text = orig
    if not isinstance(text, unicode):
        text = unicode(text, 'utf-8', 'replace')
    
    # Do &amp; separately, else, it may replace an already-inserted & from
    # an entity with &amp;, so < becomes &lt; becomes &amp;lt;
    text = text.replace('&', '&amp;')
    # Make funny characters into html entity defs
    for entity, letter in entitydefs.items():
        if entity != 'amp':
            text = text.replace(letter.decode('latin-1'), '&' + entity + ';')
        
    # Replace hyperlinks with clickable <a> tags
    def replaceURL(match):
        url = match.groups()[0]
        return '<a href="%s">%s</a>' % (url, url)
    text = urlRegexp.subn(replaceURL, text)[0]
    
    # Replace email strings with mailto: links
    def replaceEmail(match):
        url = match.groups()[0]
        return '<a href="mailto:%s">%s</a>' % (url, url)
    text = emailRegexp.subn(replaceEmail, text)[0]

    # Make leading whitespace on a line into &nbsp; to preserve indents
    def indentWhitespace(match):
        indent = match.groups()[0]
        indent = indent.replace(' ', '&nbsp;')
        return indent.replace('\t', '&nbsp;' * tab_width)
    text = indentRegexp.subn(indentWhitespace, text)[0]
    
    # Finally, make \n's into br's
    text = text.replace('\n', '<br />')

    text = text.encode('utf-8')
    
    if data is None:
        return text
    else:
        data.setData(text)
        return data
            
