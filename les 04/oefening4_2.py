lijst = [4,0,1,-2]

def rng(list):

    return max(list) - min(list)
res = rng(lijst)
print(res)


a = 6
b = 5

a,b = b,a
print(a,b)
