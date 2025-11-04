napis = 'informatyka'

# I) Fragment tekstu:
#1) Wycinanie od ... do
print(napis[2:5]) #czyli tak naprawdę od 2 do 4

#2) Wycinanie od ... do co ileś
print(napis[2:10:2])

#3) Wycinanie od początku
print(napis[:3])

#4 WYcinanie do końca
print(napis[7:])

#5) Czytanie od końca
print(napis[::-1])


# II) Zawieranie się znaku w słowie
if 'a' in napis:
    print('należy')
else:
    print('nie należy')

# III) Łączenie napisów (konkatenacja)
napis2 = napis + 'jestnajlepsza'
print(napis2)

# IV) Funkcje zmiennych typu string

#1.) poszukiwanie danengo fragmentu w tekście
'''napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz jest w napisie ')
else:
    print('xyz nie jest w napisie')

#2.) Podział tekstu na fragmenty
piec_liczb = input('Podaj pięć liczb. oddziel je przecinkiem: ')
piec_liczb_po_przedziale = piec_liczb.split(',')
print(piec_liczb_po_przedziale)
trzecia_liczba = int(piec_liczb_po_przedziale[2])
print(trzecia_liczba)
'''

#3.) Łączenie napisów
lista_napisow = ['widnows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'abc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie)

#4.) Zliczanie danego znaku w tekście
napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)

#5.) Mutowalność stringów
napis6 = 'fiwyka'
'''napis6[2] = 'z'
print(napis6)'''
#Wniosek: Stringi są niemutowalne, czyli nie można podmienić pojedyńczych liter

#Sposób na zmutowanie stringa
napis6_lista = list(napis6)
print(napis6_lista)
napis6_lista[2] = 'z'
print(napis6_lista)
napis6_gotowy = ''.join(napis6_lista)
print(napis6_gotowy)

#Długość napisu
napis7 = 'jezykpolski'
print(len(napis7))

#7.) Powielanie stringa
napis8 = 'informatyka'
print(napis8 * 3)

#8.) Funkcje testujące cyfry i litery
napis9 = 'qwerty'
if napis9.isalpha() == True:
    print('słowo składa się z liter')
else:
    print('słowo nie składa się z liter')

napis10 = '1410'
if napis10.isdigit() == True:
    print('słowo składa się z cyfr')
else:
    print('słowo nie składa się z cufr')

napis11 = 'qwerty123'
if napis9.isalnum() == True:
    print('słowo składa się z cyfr lub liter')
else:
    print('słowo nie składa się tylko z cyfr lub liter')
