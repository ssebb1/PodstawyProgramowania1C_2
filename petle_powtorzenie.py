lista = [10, 56, 89, 59]

#1. Chodzenie bezpośrednie po elementach listy
# Do zmiennej b trafiają bezpośrednie elementy listy, tzn. 10, 56, 89, 59
'''for b in lista:
    print(b)'''

# Chodzenie po liście z użyciem indeksów
# 2.1) Co to jest indeks?

# lista[2]
# 2 to indeks
# lista[2]  to element znajdujący pod indeksem 2 = 89

# 2.2)
for k in range(0, 4): #range(0, 4)
    print(lista[k])