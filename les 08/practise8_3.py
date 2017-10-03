def code(invoerstring):
    newString = ''
    for char in invoerstring:
        cr = ord(char) + 3
        newString += chr(cr)
    return newString

print(code("RutteAlkmaarDen Helder"))
