def get_data(file_name):

    with open(f'./data/{file_name}.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    results = []

    for line in lines:
        line = line.replace('\n', '')
        results.append(line)

    return results