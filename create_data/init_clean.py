import codecs

def init_clean(raw_html_name):
    f = codecs.open(raw_html_name, 'r', encoding='utf-8').read()
    start = '''<div class="outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"><div class="mdl-grid">'''
    end = '''This activity was saved to your Google Account because the following settings were on:&nbsp;Web &amp; App Activity.&nbsp;You can control these settings &nbsp;<a href="https://myaccount.google.com/activitycontrols">here</a>.</div></div></div>'''
    keywords = [
        start, end, '<b>Products:</b><br>&emsp;Search<br>',
        '<b>Why is this here?</b>', '<br>', '</p>', '&', 'emsp'
    ]
    f = f.split('<body>')[1]
    for phrase in keywords:
        f = f.replace(phrase, '')
    return f.split(
        '''<div class="header-cell mdl-cell mdl-cell--12-col"><p class="mdl-typography--title">Search</div><div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">'''
    )