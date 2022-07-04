def reader(file):
    with open(file, 'r') as f:
        return f.read()


def writer(file, data):
    with open(file, 'w') as f:
        f.write(data)


#leitura de arquivo
