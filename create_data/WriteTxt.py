def ListToTxt(file, content):
    write = ''

    for word in content:
        write += word + '\n'

    with open(f"./data/{file}.txt", 'w', encoding='utf-8') as f:
        f.write(write)


def TupleToTxt(file, content):
    write = ''

    for t in content:
        write += t[0] + ',' + str(t[1]) + '\n'

    with open(f"./data/{file}.txt", 'w', encoding='utf-8') as f:
        f.write(write)