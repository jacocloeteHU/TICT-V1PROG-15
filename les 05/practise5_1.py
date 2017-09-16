def convert(c):
    f = c * 1.8 + 32
    return f
def table():
    listf = ['F']
    listc = ['C']
    for c in range(-30,40,10):
        f = convert(c)
        listf.append(f )
        listc.append(c)
    for i in range(len(listf)):
        print(listf[i],listc[i])
table()

