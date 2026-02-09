lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]

#a)
print(lista2[1][2])

#b)

mrowka = (list(lista2[3]))
print(mrowka[2])

#odwrotnie
slowo = ''.join(mrowka)
print(type(slowo))

#c)
lista3 = lista1[2::2]
print(lista3)

#d)
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.append(lista_b)
print(lista_a)
lista2.append(lista2[1] * 3)
print(lista2)

#e)
lista1 = lista1 + [9, 6, 16, -8, 7]
print(lista1)

#f)
#lista1.sort()
lista1_posortowana = sorted(lista1)
print(lista1_posortowana)
print(lista1)
print(lista1_posortowana[0], lista1_posortowana[-1])
print(min(lista1), max(lista1))

#g)
'''del lista1[4]
print(lista1)'''

#h)
del lista1[4:9]

#i)
while 2 in lista1:
    lista1.remove(2)

lista1 = [x for x in lista1 if x != 2]
print(lista1)

#j)
'''lista3 = [x ** 2 for x in lista1]'''
lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)

#ZADANIE 2

'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

x_max = max(lista)
x_min = min(lista)

lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)'''

plansza = [
    [3, 8, 1, 9],
    [4, 6, 5, 2],
    [7, 1, 8, 3],
    [2, 9, 4, 6]
]

# Zadanie 6.1.
'''
#średnie w wierszach
for x in plansza:
    print(sum(x) / len(x))

#średnie w kolumnach
for i in range(len(plansza[0])):
    suma = 0
    for j in range(len(plansza)):
        suma += plansza[j][i]
    print(suma / len(plansza))'''

# Zadanie 6.2.
for i in range(len(plansza)):
    for j in range(len(plansza[0])):
        licznik = 0
        srodkowy = plansza[i][j]  # szary element
        '''if srodkowy < plansza[i - 1][j]:
            licznik += 1
        if srodkowy < plansza[i + 1][j + 1]:
            licznik += 1'''

        for x in range(i - 1, (i + 1) + 1):
            for y in range(j - 1, (j + 1) + 1):
                if i < 0:
                    x = len(plansza) - 1
                elif x > len(plansza) - 1:
                    x = 0
                if y < 0:
                    y = len(plansza[0]) - 1
                elif y > len(plansza[0]) - 1:
                    y = 0
                czerwony = plansza[x][y]
                if srodkowy < czerwony:
                    licznik += 1
        print(i, j, licznik)
