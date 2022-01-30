def list_of_str_to_txt(file_name, content):
    write = ''

    for word in content:
        write += word + '\n'

    with open(f'./data/{file_name}.txt', 'w', encoding='utf-8') as f:
        f.write(write)


def list_of_list_to_txt(file_name, content):
    write = ''

    for l in content:
        for s in l:
            write += s + ', '
        write = write[:-2]
        write += '\n'

    with open(f'./data/{file_name}.txt', 'w', encoding='utf-8') as f:
        f.write(write)


def tuple_to_txt(file_name, content):
    write = ''

    for t in content:
        write += t[0] + ',' + str(t[1]) + '\n'

    with open(f'./data/{file_name}.txt', 'w', encoding='utf-8') as f:
        f.write(write)
