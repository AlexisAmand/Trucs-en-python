# Choisir des étudiants

r = [] # liste des refusés
a = [] # liste des admis

def select_student(students, threshold):
    for (i,j) in students:
        if j < threshold:
            r.append((i,j))
        else:
            a.append((i,j))
    resultat = {"Accepted": sorted(a, key=lambda a: a[1], reverse=True), "Refused": sorted(r, key=lambda r: r[1], reverse=False)}
    return resultat

# pour le test

my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]
print(select_student(my_class, 20))