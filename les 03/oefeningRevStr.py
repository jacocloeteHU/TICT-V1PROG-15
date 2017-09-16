print(reversed('hallo'))

def rev(str):
    s = ''
    for i in range(len(str)-1,-1,-1):
        print(i)
        s += str[i]

    print(s)

rev('jaco')
