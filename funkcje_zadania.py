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


# # Zadanie 2.1.
# def czy_anagramy(s1, s2):
#     '''if sorted(s1) == sorted(s2):
#            return True
#       else:
#           return False'''
#     return sorted(s1) == sorted(s2)
#
#     # print(czy_anagramy('nosek', 'keson'))
#
#
# '''    s1 = 'nosek'
#     s2 = 'kseon'
# print(sorted(s1) == sorted(s2))'''

def jaki_trojkat(a,b,c):
    if a + b + c > 2 * max(a, b, c):
        if a ** 2 + b ** 2 + c ** 2 == 2 * max([a, b, c]) ** 2:
            print('prostokątny')
        if a ** 2 + b ** 2 + c ** 2 > 2 * max([a, b, c]) ** 2:
            print('ostrokątny')
        if a ** 2 + b ** 2 + c ** 2 < 2 * max([a, b, c]) ** 2:
            print('rozwartokątny')
    else:
        print('To nie jest trójkąt')
jaki_trojkat(5, 5, 12)


def liczby_niezalezne(lista):
    for e in lista:
        dzielniki = []
        for l in lista:
            if e % l == 0:
                dzielniki.append(l)
        if len(dzielniki) == 1:
            wynik.append(e)
    return wynik
print(liczby_niezalezne([12, 7, 3, 6, 21, 74]))
#Zadanie domowe: 2.4, 2.5, 2.6, 2.7, 2.8

def ile_cyfr(liczba):
    licznik = 0
    while liczba > 0:
        liczba = liczba // 10
        licznik += 1
    return
print(ile_cyfr(127))

def unikatowe_elementy(l1, l2):
    zbior = set()
    l = l1 + l2
    for x in l:
        if l.count(x) == 1:
            zbior.add(x)
    return zbior
print(unikatowe_elementy([1, 2, 6, 4, 5], [8, 4, 5, 2]))

