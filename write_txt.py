def list_to_txt(file, content):
    write = ''

    for word in content:
        write += word + '\n'

    with open(f"data/{file}.txt", 'w') as f:
        f.write(write)


def tuple_to_txt(file, content):
    write = ''

    for t in content:
        write += t[0] + ',' + str(t[1]) + '\n'

    with open(f"data/{file}.txt", 'w') as f:
        f.write(write)