def convert(c):
    f = c * 1.8 + 32
    return f

def table():
    listf = ['F']
    listc = ['C']
    for c in range(-30,50,10):
        f = convert(c)
        listf.append(f )
        listc.append(float(c))
    for i in range(len(listf)):
        print('{:^6} {:^6}'.format(listf[i],listc[i]))
table()

