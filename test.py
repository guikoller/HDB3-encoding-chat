import numpy as np
import matplotlib.pyplot as plt
from encode_decode import asciiEncode, asciiDecode, HDB3Encode, HDB3Decode, binaryEncode, binaryDecode

def plotTwist(data1, data2, msg):
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots(2)
    fig.suptitle(msg)
    axs[0].plot(data1)
    axs[1].plot(data2)
    plt.show()

text = input('Digite a mensagem\n')

text_to_ascii = asciiEncode(text)
print('ASCII encode:')
print(text_to_ascii)

ascii_to_binary = binaryEncode(text_to_ascii)
print('Binary Encode:')
print(ascii_to_binary)

# binary_to_HDB3 = HDB3Encode(ascii_to_binary)
# print('HDB3 encode: ')
# print(binary_to_HDB3)

#plotTwist(text_to_ascii, ascii_to_binary, 'Encode')

# HDB3_to_binary = HDB3Decode(binary_to_HDB3)
# print('HDB3 decode:')
# print(HDB3_to_binary)

binary_to_ascii = binaryDecode(ascii_to_binary)
print('Binary decode:')
print(binary_to_ascii)
#plotTwist(ascii_to_HDB3, HDB3_to_ascii, 'Decode')

ascii_to_text = asciiDecode(binary_to_ascii)
print('ASCII decode:')
print(ascii_to_text)