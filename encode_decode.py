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
    for i in array:
        values.append(f'{i:08b}'.format(8))
    return ''.join(values)

def binaryDecode(string):
    values = []
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    array =  [string[i:i+8] for i in range(0, len(string), 8)] 
    for i in array:
        values.append(int(i,2))
    return values

def HDB3Encode(message):
    message = AMIencoding(message)
    hdb3Message = message

    zerosCounter = 0
    polarity = 0
    iterator = 0

    for bit in message:
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
                    for i in len(hdb3Message):
                        hdb3Message[i] = hdb3Message[i]*(-1)

                polarity = hdb3Message[iterator]

        else:
            zerosCounter = 0

        iterator += 1

    return hdb3Message

def HDB3Decode(message):
    decodedMessage = message
    polarity = 0
    iterator = 0

    for iterator in len(message):
        if message[iterator] != 0:
            if decodedMessage[iterator] == polarity:
                i = iterator-3
                for i in iterator:
                    decodedMessage[i] = 0

            polarity = message[iterator]

    iterator = 0
    for iterator in len(decodedMessage):
        if decodedMessage[iterator] == -1:
            decodedMessage[iterator] = 1

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
    print('encoding\n')
    message = asciiEncode(message)
    #print(message)
    message = binaryEncode(message)
    #print(message)
    return message

def decode(message):
    print("decoding\n")
    message = asciiDecode(message)
    #print(message)
    message = binaryDecode(message)
    #print(message)
    return message
