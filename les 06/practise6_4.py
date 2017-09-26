studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
 antw = []
 for student in range(len(studentencijfers)):
     number = studentencijfers[student]
     antw.append(sum(number) / len(number))
 return antw

def gemiddelde_van_alle_studenten(studentencijfers):
 list = []
 antw = 0
 for student in range(len(studentencijfers)):
     number = studentencijfers[student]
     list.append(sum(number) / len(number))
 for row in range(len(list)):
    antw = antw + list[row]

 return antw / len(list)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
