from matplotlib.pyplot import text


def asciiEncode(message):
    values = []
    for char in message:
        values.append(ord(char))
    return values

def asciiDecode(message):
    values = []
    for char in message:
        values.append(chr(char))
    return ''.join(values)

def binaryEncode(array):
    values = []
    bit_values = []
    
    for i in array:
        values.append(f'{i:08b}'.format(8))
    
    values = list(''.join(values))

    for bit in values:
        bit_values.append(int(bit))

    return bit_values

def binaryDecode(array):
    #printar grafico aqui
    string_ints = [str(int) for int in array]
    string_ints = ''.join(string_ints)
    values = []
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    ascii_array =  [string_ints[i:i+8] for i in range(0, len(string_ints), 8)] 
    for i in ascii_array:
        values.append(int(i,2))
    return values

def HDB3Encode(message):
    amiMessage = AMIencoding(message)
    hdb3Message = amiMessage

    zerosCounter = 0
    polarity = 0
    iterator = 0

    for bit in amiMessage:
        if bit == 0:
            zerosCounter += 1

            if zerosCounter == 4:
                zerosCounter = 0
                if iterator == 3:
                    hdb3Message[iterator] = -1 # Preventbinary_to_asciiing segFault
                else:
                    hdb3Message[iterator] = hdb3Message[iterator-4]
                
                if hdb3Message[iterator] == polarity:
                    hdb3Message[iterator] = hdb3Message[iterator]*(-1)
                    hdb3Message[iterator-3] = hdb3Message[iterator]
                    i = iterator + 1
                    while i <= len(hdb3Message):
                        #try:
                        hdb3Message[i] = hdb3Message[i]*(-1)
                        i += 1
                        #except:
                            # print('cu seg fault')

                polarity = hdb3Message[iterator]

        else:
            zerosCounter = 0

        iterator += 1

        string_array  = []        
        for bit in hdb3Message:
            if bit == 1:
                string_array.append('+')
            elif bit == -1:
                string_array.append('-')
            else:
                string_array.append('0')

    return ''.join(string_array)

def HDB3Decode(message):
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    # array =  [string[i:i+8] for i in range(0, len(string), 8)] 
    
    bit_array = []
    message  = list(''.join(message))
    for bit in message:
            if bit == '+':
                bit_array.append(1)
            elif bit == '-':
                bit_array.append(-1)
            else:
                bit_array.append(0)

    decodedMessage = bit_array
    polarity = 0
    iterator = 0

    while iterator < len(bit_array):
        if decodedMessage[iterator] != 0:
            if bit_array[iterator] == polarity:
                i = iterator-3
                while i <= iterator:
                    decodedMessage[i] = 0
                    i += 1

            polarity = decodedMessage[iterator]
        
        iterator += 1

    iterator = 0
    while iterator < len(decodedMessage):
        if decodedMessage[iterator] == -1:
            decodedMessage[iterator] = 1

        iterator += 1

    return decodedMessage

# Turning the binary string into a Alternate Mark Inversion(AMI) string
def AMIencoding(binaryMessage):
    amiMessage = binaryMessage
    polarity = 1
    iterator = 0

    for bit in binaryMessage:
        if bit == 1:
            amiMessage[iterator] = polarity
            polarity = polarity*(-1)
        
        iterator += 1

    return amiMessage

def encode(message):
    text_to_ascii = asciiEncode(message)
    ascii_to_binary = binaryEncode(text_to_ascii)
    binary_to_HDB3 = HDB3Encode(ascii_to_binary)

    return binary_to_HDB3

def decode(message):
    HDB3_to_binary = HDB3Decode(message)
    binary_to_ascii = binaryDecode(HDB3_to_binary)
    ascii_to_text = asciiDecode(binary_to_ascii)

    return ascii_to_text
