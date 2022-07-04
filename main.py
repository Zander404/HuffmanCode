from Huffman import HuffmanEncoding, HuffmanDecoding
from dataManage import *

the_data = reader('test.txt')
writer('text_original.doido', convertStringForBinary(the_data))
encoding, the_tree = HuffmanEncoding(the_data)
decoding = HuffmanDecoding(encoding, the_tree)
print("Arquivo compactado", encoding)
print("Arquivo descompactado:", decoding)

writer('test.zin', encoding)
compatRate(len(encoding), len(' '.join(map(bin, bytearray(the_data, "utf-8")))))

# descompactação

new_data = reader('test.zin')
decoding = HuffmanDecoding(new_data, the_tree)

print("Arvore de novo: ", decoding)