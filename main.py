from Huffman import HuffmanEncoding, HuffmanDecoding
from dataManage import *

the_data = reader('test.txt')
writer('text_original.doido', convertStringForBinary(the_data))
encoding, the_tree = HuffmanEncoding(the_data)
decoding = HuffmanDecoding(encoding, the_tree)
print("Arquivo compactado", encoding)
print('\n')
compatRate(len(encoding), len(' '.join(format(c, 'b') for c in bytearray(the_data, "utf-8"))))
#print("Arquivo descompactado:", decoding)
writer('test.zin', encoding)


# descompactação

new_data = reader('test.zin')
decoding = HuffmanDecoding(new_data, the_tree)

