getallenlijst = [2, 4, 6, 8, 10, 9, 7]

def sum(getallenlijst):
    count = 0
    for getal in getallenlijst:
        count = count + getal

    return count
print("De som van de getallen lijst:" +  str(sum(getallenlijst)))
