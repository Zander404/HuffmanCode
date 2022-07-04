from Huffman import HuffmanEncoding, HuffmanDecoding
from arvroreBinariaTAD import reader, writer


the_data = reader('test.txt')
encoding, the_tree = HuffmanEncoding(the_data)
decoding = HuffmanDecoding(encoding, the_tree)
print("Arquivo conectado", encoding)
print("Arquivo descompactado:", decoding)
print("Tamanho do arquivo:", len(the_data))
print("Tamanho do arquivo comprimido:", len(encoding))
writer('test.zin', encoding)


