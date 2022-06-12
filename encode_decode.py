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

def HDB3Encode(message):
    return message

def HDB3Decode(message):
    return message