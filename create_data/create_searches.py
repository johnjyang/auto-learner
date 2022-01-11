from create_data.write_txt import *

def log_searches(cleaned_html):
    write = []
    for s in cleaned_html[1:]:
        if s[:8] == "Searched":
            s = s.replace(
                '''Searched for <a href="https://www.google.com/search?q=''', '')
            s = s.replace('''Searched for <a href="''', '')
            s = s.split('''amp;''')[0]
            s = s.split('''"''')[0]
            s = s.replace('''+''', ' ')
            if not '%' in s and not '/' in s:
                s = s.replace('%27', "'")
                write.append(s.lower())
    list_of_str_to_txt("searches", write)