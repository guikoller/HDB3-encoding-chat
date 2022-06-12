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

msg = input("Digite a mensagem:\n")
msg = asciiEncode(msg)

print(msg)
print(asciiDecode(msg))