import os
from dotenv import load_dotenv
from init_clean import *
from write_txt import *

load_dotenv()
file_name = os.getenv('HTML_FILE_NAME')

f = init_clean(file_name)
searches = f.split(
    '''<div class="header-cell mdl-cell mdl-cell--12-col"><p class="mdl-typography--title">Search</div><div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">'''
)

write = []

for s in searches[1:]:
    if s[:8] == "Searched":
        s = s.replace('''Searched for <a href="https://www.google.com/search?q=''', '')
        s = s.replace('''Searched for <a href="''', '')
        s = s.replace('''amp;tbm=vid''', '')
        s = s.replace('''amp;tbm=isch''', '')
        s = s.split('''"''')[0]
        s = s.replace('''+''', ' ')
        if not '%' in s and not '/' in s:
            s = s.replace('%27', "'")
            write.append(s.lower())

list_to_txt("searches", write)
