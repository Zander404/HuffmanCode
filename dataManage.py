#leitura de arquivo
from math import ceil


def reader(file):
    with open(file, 'r') as f:
        return f.read()


#escrita de arquivo
def writer(file, data):
    with open(file, 'w') as f:
        f.write(data)


#comparador de compactacao
def compatRate(compact, descompact):
    print("Compactacao:", compact)
    print("Descompactacao:", descompact)
    r = (compact*100)
    threeway = ceil(r / descompact)
    return print('taxa de compactacao de: ', threeway, "% ")


#convesor para binário

def convertStringForBinary(the_data):
    binary_converted = ' '.join(map(bin, bytearray(the_data, "utf-8")))
    return binary_converted