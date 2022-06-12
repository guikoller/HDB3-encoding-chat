from encode_decode import asciiEncode, asciiDecode, HDB3Encode, HDB3Decode

data = input('Digite a mensagem\n')

data = asciiEncode(data)
print('ASCII encode:')
print(data)

data = HDB3Encode(data)
print('HDB3 encode: ')
print(data)

data = HDB3Decode(data)
print('HDB3 decode:')
print(data)

data = asciiDecode(data)
print('ASCII decode:')
print(data)