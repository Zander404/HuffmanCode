from Huffman import HuffmanEncoding, HuffmanDecoding
from arvroreBinariaTAD import reader, writer

the_data = reader('test.txt')
encoding, the_tree = HuffmanEncoding(the_data)
decoding = HuffmanDecoding(encoding, the_tree)
print("Arquivo compactado", encoding)
print("Arquivo descompactado:", decoding)
print("Espaco usado depois de compactado(em bits):", len(encoding))
writer('test.zin', encoding)



