#leitura de arquivo
from math import ceil


def reader(file):
    with open(file, 'r') as f:
        return f.read()


def writer(file, data):
    with open(file, 'w') as f:
        return f.write(data)


#escrita de arquivo
def writerD(file, data, the_tree):
    with open(file, 'a') as f:
        f.write(data)
        f.write('\n')



#comparador de compactacao
def compatRate(compact, descompact):
    r = (compact*100)
    threeway = ceil(r / descompact)
    return print('taxa de compactacao de: ', threeway, "% ")


#convesor para binário

def convertStringForBinary(the_data):
    binary_converted = ' '.join(format(c, 'b') for c in bytearray(the_data, "utf-8"))
    return binary_converted

