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

def binaryDecode(string):
    values = []
    array = [string[i:i+8] for i in range(0, len(string), 8)]
    print(array)
    for i in array:
        values = ''.join(i)
        #values.append(int(i,2))
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
                    hdb3Message[iterator] = -1 # Preventing segFault
                else:
                    hdb3Message[iterator] = hdb3Message[iterator-4]
                
                if hdb3Message[iterator] == polarity:
                    hdb3Message[iterator] = hdb3Message[iterator]*(-1)
                    hdb3Message[iterator-3] = hdb3Message[iterator]
                    i = iterator + 1
                    while i <= len(hdb3Message):
                        hdb3Message[i] = hdb3Message[i]*(-1)
                        i += 1

                polarity = hdb3Message[iterator]

        else:
            zerosCounter = 0

        iterator += 1

    return hdb3Message

def HDB3Decode(message):
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    # array =  [string[i:i+8] for i in range(0, len(string), 8)] 

    decodedMessage = message
    polarity = 0
    iterator = 0

    while iterator < len(message):
        if decodedMessage[iterator] != 0:
            if message[iterator] == polarity:
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
    message = asciiEncode(message)
    print(message)
    message = binaryEncode(message)
    print(message)
    print('------------------------------------------------------------------')
    return message

def decode(message):
    print(message)
    message = binaryDecode(message)
    print(message)
    message = asciiDecode(message)
    print('------------------------------------------------------------------')
    return message
