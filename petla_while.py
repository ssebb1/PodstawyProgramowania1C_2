#Pętla while - przykłady

'''liczba = 120
licznik = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0:   #tak długo jak liczba jrest dodatnia, pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)'''

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć: ')
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć: ')
print(licznik)'''

#Zadanie 2.

popr_haslo = 'w_dupie_trzaslo'
haslo = input('Podaj hasło: ')
proba = 1
while haslo != popr_haslo and proba <= 5:
    print('Chciałbyś <3. Wpisuj jeszcze raz: ')
    haslo = input('PODAJ TO HASŁO NIEROBIE: ')
    proba = proba + 1
if haslo == popr_haslo:
    print('Wreszcie... BRAWOOO udało się Tobie :D')
else:
    print('Skończyło się nie wejdziesz co systemu :>')
