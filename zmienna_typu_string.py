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