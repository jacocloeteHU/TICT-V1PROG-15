cijferlijst = {
    'jaco' : 9,
    'klaas': 10,
    'henk' : 5,
    'jan-peter' : 6,
    'henk-jan' : 8,
    'pieter' : 10,
    'marijn' : 9.5,
    'karel' : 8
}

for cijfer in cijferlijst.items():
    if(cijfer[1] >= 9):
        print('{} heeft cijfer: {}'.format(cijfer[0], cijfer[1]))
