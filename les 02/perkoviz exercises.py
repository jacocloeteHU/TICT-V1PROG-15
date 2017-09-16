




def p(val):
    print(val)
    return;

# avarage

p((23+19+31)/3)

# 2.1
p(7 + 7+ 7+7 +7)
p(403 // 73)
p(403 % 73)
p(2**10)
p(57-54)
p(min(34.99,29.95,31.50))

# 2.2
p((2+2) < 4)
p((7 // 3) == (1 + 1))
p(((3**3) + (4**4) == 25))
p((2+4+6) > 12)
p((1387 / 19) and True)
p(31 % 2 == 2)
p(min(29.95,34.99) < 30.00)

# 2.3

a = 3
b = 4
c = a * a + b * b
p(c)




# 2.12

s1 = "-"
s2 = "+"

p(s1 + s2)
p(s1 + s2 + s1)
p(s2 + s1 + s1)
p((s2 + s1 + s1 ) * 2)
p((s2 + s1 + s1 ) * 10 + s2)
p((s2 + s1 + s2 + s2 + s2 + s1 + s1) * 5)

# 2.13

s = "abcdefghijklmnopqrstuvwxyz"

p(s[0] + s[2]+ s[-1]+ s[-2] + s[-10])

# 2.14

st = "goodbye"
p(st[0] == "g")
p(st[6] == "g")
p((st[0] == "g") & (st[1] == "a"))
p(st[len(st) - 1] == "x")
p(st[3] == "d")
p(st[0] == st[6])
p(st[3] +st[4]+ st[5] +st[6]== 'tion')

# 2.18

flowers = ("rose","bougainvillea","yucca", "marigold", "daylilly", "lilly of the valley")

p('potato' in flowers)
thorny =  flowers[0], flowers[1], flowers[2]
poisonous = flowers[-1],
dangerous = thorny + poisonous

p(dangerous)

# 2.19

awnsers = ['Y','N','N','Y','N','Y','N','Y','Y','Y','N','N','N']
numYes = 5
numNo = 6
percentYes = 5 / len(awnsers)
p(percentYes)
awnsers.sort()
p(awnsers)
p(awnsers.index('Y'))
f = awnsers.index('Y')
