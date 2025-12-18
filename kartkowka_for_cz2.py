'''n = int(input('Podaj liczbę: '))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)

    print(iloczyn)'''
import random
import time

#zadanie2

'''lista = [4, 12, 8, 1, 5, 6, 3]
sraka = 0

for x in lista:
    for y in lista:
        if x != y and x in lista and y in lista and (x + y) % 3 == 0:
            sraka += 1
print(sraka)'''

#zadanie3

'''n = int(input('Podaj ile będzie napisów: '))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis: ')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)'''


#Zadanie 6.
'''wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2)): #abs(x) = |x| wartosc bezwzgledna
    akcja += 1
    print(f'Akcja {akcja}')
    #druzyna = int(input('Podaj nr drużyny, która wygrała akcję'))
    druzyna = random.randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1}:{wynik2}')
    time.sleep(1)
if wynik1 > wynik2:
    print('WYgrała drużyna1')
else:
    print('WYgrałą drużyna2')'''

'''liczba = int(input('Podaj liczbę: '))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

#Zadanie 8.

'''liczba = int(input('Podaj liczbę: '))
d = 2
ile_czyn = 0
ile_r_czyn = 0
while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba = liczba // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)'''


#Zadanie 5
from random import randint
x, y = 0, 0
ruchy = ['p'] * 10 + ['d'] * 5 + ['l'] * 5 + ['g'] * 10 + ['q']
print(ruchy)
while True:
    #ruch = input('Podaj ruch: ')
    ruch = ruchy[randint(0, len(ruchy) - 1)]
    if ruch == 'q':
        break
    elif ruch == 'g':
        if y < 9:
            y += 1
        else:
            print('Ruch niemożliwy')
    elif ruch == 'd':
        if x > 0:
            x -= 1
        else:
            print('Ruch niemożliwy')
    elif ruch == 'p':
        if y < 9:
            y += 1
        else:
            print('Ruch niemożliwy')
    elif ruch == 'l':
        if x > 0:
            x -= 1
        else:
            print('Ruch niemożliwy')
    else:
        print('Nieznany ruch')
    print(f'({x}, {y})')




