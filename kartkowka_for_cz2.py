'''n = int(input('Podaj liczbę: '))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)

    print(iloczyn)'''

#zadanie2

lista = [4, 12, 8, 1, 5, 6, 3]
sraka = 0

for x in lista:
    for y in lista:
        if x != y and x in lista and y in lista and (x + y) % 3 == 0:
            sraka += 1
print(sraka)

#zadanie3

n = int(input('Podaj ile będzie napisów: '))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis: ')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)
