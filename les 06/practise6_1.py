def seizoen(maand):
    m = ''
    if(maand >= 3 and maand <= 5):
        m = 'lente'
    elif(maand > 5 and maand < 9):
        m = 'zomer'
    elif(maand >= 9 and maand <= 11):
        m = 'herfst'
    else:
        m = 'winter'

    return m

print(seizoen(5))
print(seizoen(12))
print(seizoen(1))
print(seizoen(6))
print(seizoen(9))
print(seizoen(8))
