from create_data.write_txt import *
import html

def log_searches(cleaned_html):
    print('Parsing searches and dates from html.')
    searches = []
    dates = []
    for query in cleaned_html[1:]:
        if query[:4] != 'Used' and query[:4] != 'View':
            if '<a' in query:
                query = query.split('''">''')[1]
                s = query.split('</a>')[0]
                s = s.replace('#39;', "'")
                s = s.replace('amp; ', "")
                s = s.replace('amp;', "&")
                if not 'http' in s:
                    searches.append(html.unescape(s.lower()))
                    d = query.split('</a>')[1].split('</div>')[0]
                    dates.append(d)
    list_of_str_to_txt("searches", searches)
    list_of_str_to_txt("dates", dates)
    print('Searches and dates lists created.')