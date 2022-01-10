def get_searches():

    with open('./data/searches.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    searches_list = []

    for line in lines:
        line = line.replace('\n', '')
        searches_list.append(line)

    return searches_list
