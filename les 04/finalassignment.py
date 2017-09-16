def standaardtarief(afstandKM):
    kpkm = 0.80
    bedrag = 0.0
    if afstandKM <= 0:
        bedrag = 0.0
    elif afstandKM >= 50:
        rest = afstandKM - 50
        kpkm = 0.60
        bedrag = 15.0 + (kpkm*rest)
    else:
        bedrag = afstandKM*kpkm

    return bedrag


def ritprijs(leeftijd, weekendrit, afstandKM):
    korting = 0.0
    prijs = standaardtarief(afstandKM)
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        korting = 0.70
    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        korting = 0.65
    elif leeftijd >= 12 and leeftijd < 65 and weekendrit == True:
        korting = 0.60
    else:
        korting = 1.0
    return prijs*korting


print(ritprijs(11, True , 51))
print(ritprijs(11, True , 15))
print(ritprijs(11, True , -15))
print(ritprijs(11, False , 15))
print(ritprijs(11, False , 51))
print(ritprijs(11, False , -51))

print(ritprijs(12, True , 15))
print(ritprijs(12, True , 51))
print(ritprijs(12, True , -51))
print(ritprijs(12, False , 51))
print(ritprijs(12, False , 15))
print(ritprijs(12, False , -15))

print(ritprijs(64, True , 15))
print(ritprijs(64, True , 51))
print(ritprijs(64, True , -51))
print(ritprijs(64, False , 51))
print(ritprijs(64, False , 15))
print(ritprijs(64, False , -15))

print(ritprijs(65, True , 80))
print(ritprijs(65, True , 15))
print(ritprijs(65, True , -15))
print(ritprijs(65, False , 15))
print(ritprijs(65, False , 80))
print(ritprijs(65, False , -80))
