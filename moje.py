'''print('Hello World')

n = int(input('Podaj liczbę całkowitą dodatnią: '))
ile = 0
for i in range(n):

'''


'''n = int(input('Podaj liczbę całkowitą dodatnią: '))
ile = 0

for i in range(1, n+1):
    if n % i == 0 and i % 2 == 0:
        ile += 1  # to musisz dodać

print(ile)  # a to na końcu'''



'''lista = []
for i in range(100, 1000):
    if i % 11 == 0:
        lista.append(str(i))
print(', '.join(lista))'''



'''n = int(input('Podaj liczbę całkowitą dodatnią:  '))
ile = 0
for i in range(1, n+1):
    if n % i == 0 and i % 2 != 0:
        ile = ile + 1
print(ile)'''

#Zadania kkartkowka A petle1

#1.
'''for i in range(101):
    print('Cześć')

#2.

lista = [12, 45, 78, 101, 9, -5, 9, 7, 23]

for j in lista:
    if j % 2 != 0:
        print(j)'''

#4.



#Zadania kartkowka B petle2

#1.
'''for i in range(6):
    print('informatyka')'''

#2.

'''lista = [34, 90, 77, 56, 54, 33, 21, 98, 45]

for i in range(len(lista)):
    if i % 3 == 0:
        print(lista[i])'''


#-----------------------------------------------

'''i = 10
while i >= 1:
    print(i)
    i = i - 1


for i in range(10, 1, -2):
    print(i)
    i -= 1
    print(i)'''

################# KALKULATOR ##################


'''while True:
    a = int(input("Wyjście: 'q'. Podaj pierwszą liczbę: "))
    znak = input("Podaj znak działania '+' lub '-' lub '*' lub '/': ")
    b = int(input('Podaj drugą liczbę: '))
    if znak == 'q':
        break
    elif znak == '+':
        print(a + b)
    elif znak == '-':
        print(a - b)
    elif znak == '*':
        print(a * b)
    elif znak == '/':
        print(a / b)
    else:
        print('Nieprawidłowy znak')'''




        #-------------------------------------------------

'''liczba = int(input('Podaj liczbę całkowitą: '))
ile = 0
c = 2

while liczba > 1:
    while liczba % c == 0:
        liczba = liczba // c
        if c >= 10 and c <= 99:
            ile = ile + 1

    c = c + 1
print(ile)'''


'''a = int(input('Podaj liczbę całkowitą a: '))
b = int(input('podaj liczbę całkowitą b: '))
org_a = a
org_b = b
while a != b:
    if a > b:
        b = b + org_b
    else:
        a = a + org_a
nww = a
print (nww)'''

'''wiek = int(input('Podaj swój wiek: '))

if wiek < 18:
   print('Nie pracujesz, ale mam nadzieję, że się uczysz')
elif 18 <= wiek < 65:
    print('Mam nadzieję, że już pracujesz')
else:
    print('Miłego odpoczynku')'''

'''slowo = 'informatyka'
odwr = slowo[::-1]
if slowo == odwr:
    print('Słowo jest palindromem')
else:
    print('Słowo nie jest palindromem')'''

'''slowo = 'BRNQZPFXLMWUGTSHPDAAOVKICNRTEQYBPMZEFDCXHJMFAOTLPMXGSAQWETRMADYUBXCNPLKJYHOFA'

print(slowo[9::10])'''

'''slowo = 'częstochowa'
print('stoch' in slowo)

print(slowo.find('stoch'))

if 'stoch' in slowo:
    print('Znajduje się')

if slowo.count('stoch') > 0:
    print('Znaleziono')'''

'''slowo = input('Podaj słowo: ')
print('W podanym słowie znajdują się litery a, b, c i d w następujących ilościach:')
print(f'litera a: {slowo.count("a")}')
print(f'litera b: {slowo.count("b")}')
print(f'litera c: {slowo.count("c")}')
print(f'litera d: {slowo.count("d")}')'''


'''# Pobranie trzech liczb rzeczywistych w jednej linii
liczby = input("Podaj trzy liczby rzeczywiste: ").split()

# Konwersja każdego elementu na liczbę rzeczywistą (float)
liczby = [float(x) for x in liczby]

# Obliczenie sumy liczb
suma = sum(liczby)

# Wyświetlenie wyniku
print("Suma podanych liczb to:", suma)'''





'''slowo = 'ABCKOTXYZDEFGHIJKOTLMNOPQRSTUVWXKOTYZABCDEFGHIJKLMNOPQRSTUVWXABCDEFGHIJKLMN'

start = 0
while True:
    ind = slowo.find('KOT', start)
    if ind == -1:
        break
    print(ind)
    start = ind + 1
'''


'''lista = ['Gdańsk', 'Gdynia', 'Sopot', 'Słupsk', 'Puck']
miasta = ', '.join(lista)
print(f'Najpopularniejszymi miastami na Pomorzu są: {miasta}')'''




'''sentencja = 'abbccaaaa'

a = sentencja.count('a')
b = sentencja.count('b')
c = sentencja.count('c')

if a > b and a > c:
    print(f'Najczęściej występuje litera a. {a} razy.')
elif b > c and b > a:
    print(f'Najczęściej występuje litera b. {b} razy.')
elif c > a and c > b:
    print(f'Najczęsciej występuje litera c. {c} razy.')
else:
    print('Brak jednoznacznej odpowiedzi (remis).')'''





#SPRAWDZIAN Listy, słowniki i zbiory
#ZAD. 1
#sposób 1
'''dziedzina = [-2, 0, 4, 6, 7, 11]

wartosci = []
for x in dziedzina:
    wartosci.append(3 * x - 2)
print(wartosci)

#sposób 2

wartoscii = [3 * y - 2 for y in dziedzina]

print(wartoscii)'''

#ZAD. 2

lista = ['kot', 'pies', 'żółw', [4, 6, 7, 1], 2.7, [[8, 9], [3, 5]]]

#a)
print(len(lista))

#b)
print(lista[5][1][1])

#d)
print(sum(lista[3]))

#ZAD. 3

przeslanie = [[90, 65, 87, 83, 90, 69], [87, 65, 82, 84, 79], [66, 89, 67], [80, 82, 90, 89, 90, 87, 79, 73, 84, 89, 77]]
print(' '.join([''.join(map(chr, x))for x in przeslanie]))

dupa = []
for x in przeslanie:
    litery = map(chr, x)
    slowo = ''.join(litery)
    dupa.append(slowo)
wynik = ' '.join(dupa)
print(wynik)


#ZAD. 4
plansza = [
    [3, 8, 1, 9],
    [4, 6, 5, 2],
    [7, 1, 8, 3],
    [2, 9, 4, 6]
]

#ZAD. 5
przedmioty = ['informatyka', 'matematyka pp', 'matematyka pr', 'język polski pp', 'język angielski']
wyniki = [100, 28, 98, 30, 80]

#a)
matura = dict(zip(przedmioty, wyniki))
print(matura)

#b)
print(matura['język polski pp'])

#c)

matura['matematyka pp'] += matura['matematyka pp'] // 2
print(matura)

tekst = 'NAUCZYCIELEMWSZYSTKIEGOJESTPRAKTYKA'

print(len(set(tekst)))

for x in tekst:








