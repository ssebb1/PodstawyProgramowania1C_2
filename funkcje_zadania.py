#Zadanie 0.3
#a)
def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]

wynik = suma_v(u, v)

print(wynik)

def iloczyn_v(u, v):
    w = []
    for i in range(len(u)):
        iloczyn = u[i] * v[i]
        w.append(iloczyn)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]

wynik = iloczyn_v(u, v)
print(wynik)