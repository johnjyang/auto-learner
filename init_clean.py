import codecs

def init_clean(raw_html):
    f = codecs.open(raw_html, 'r').read()
    start = '''<div class="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"><div class="mdl-grid">'''
    end = '''This activity was saved to your Google Account because the following settings were on:&nbsp;Web &amp; App Activity.&nbsp;You can control these settings &nbsp;<a href="https://myaccount.google.com/activitycontrols">here</a>.</div></div></div>'''
    keywords = [
        start, end, "<b>Products:</b><br>&emsp;Search<br>",
        "<b>Why is this here?</b>", "<br>", "</p>", "&", "emsp"
    ]
    cleaned = None
    for phrase in keywords:
        if cleaned:
            cleaned = cleaned.replace(phrase, '')
        else:
            cleaned = f.replace(phrase, '')
    return cleaned
