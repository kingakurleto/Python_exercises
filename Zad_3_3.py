'''### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
​
- `suma(liczby)` - zwraca sumę liczb z listy `liczby`
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby`
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w
liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy
`liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby`
liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`;
 zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`,
 jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
'''

print("="*60)

#1. - "Suma(liczby)" - zwraca sumę liczb z listy "liczby"

lista=[10,20,30,40]


def funkcja_liczaca_sume_z_liczb(lista:list) ->list:
    return sum(lista)

print(f'Suma liczb występujących w liście to:' , funkcja_liczaca_sume_z_liczb(lista))


def test_funkcja_liczaca_sume():
    assert funkcja_liczaca_sume_z_liczb([10,10,10])==30


print("="*60)

# "Średnia(liczby)" - zwraca średnią wartość z listy "liczby"

ilosc_liczb_w_liscie=len(lista)
print(f'Ilość liczb w liście:', ilosc_liczb_w_liscie)

def funkcja_liczaca_srednia_z_listy(lista:list)->list:
    return sum(lista)/ilosc_liczb_w_liscie


def test_funkcja_liczaca_srednia():
    assert funkcja_liczaca_srednia_z_listy([10,20,30,40])==25


print(f'Średnia z liczb w liście to: ' , funkcja_liczaca_srednia_z_listy(lista))


print("="*60)

# `Max(liczby)` – zwraca największą wartość z listy `liczby`

listamax=[]
def max_z_listy(listamax:list) ->list:
    return max(listamax)

print('Wartość maksymalna z listy to: ', max_z_listy([3,5,6]))

def test_max_z_listy():
    assert max_z_listy([6,7,20])==20

print("="*60)

#- "Różnica max-min-liczby" – różnica pomiędzy największą a najmniejszą liczbą w
#liście; "0" jeśli tablica jest pusta

def roznica_min_max(liczby: list):
    if liczby==():
        wynik=0
    else:
        return max(liczby) - min(liczby)


print('Różnica liczb wynosi: ', roznica_min_max([9,10,1]))

print("="*60)

#- "Wypisz_wieksze(liczby, x)" – wypisuje ("print()") wszystkie te liczby z listy
#"liczby", które są większe od "x"

def wypisz_wieksze(liczby:list, x):
    wynik = set()
    for znak in liczby:
        if znak > x:
            wynik.add(znak)

    return wynik

print(f'Z podanego zbioru liczby większe od x to : {wypisz_wieksze([5,6,7],5)}')

print("="*60)

#`pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby`
#liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma

def pierwsza_wieksza(liczby:list, x):
    wynik = set()
    for znak in liczby:
        if znak > x:
            wynik = znak
        if znak < x:
            wynik = None
    return wynik

print(f'Pierwsza znaleziona liczba większa od x to: {pierwsza_wieksza([5,6,7],1)}')

print("="*60)

#- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`

def suma_wiekszych(liczby:list, x):
    for znak in liczby:
        if znak < x:
            break
        if znak > x:
            return sum(liczby)

print(f'Suma liczb większych od x to : {suma_wiekszych([5,6,7],2)}')

print("="*60)

# `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`

def ile_wiekszych(liczby:list, x):
    wynik = set()
    for znak in liczby:
        if znak > x:
            wynik.add(znak)
    return len(wynik)

print(f'Liczba większych liczb od x to : {ile_wiekszych([5,6,7],6)}')

print("="*60)

# `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`

def wypisz_podzielne(liczby:list, x:int):
    wynik = set()
    for znak in liczby:
        if znak % x == 0:
            wynik.add(znak)
    return wynik

print(f'Liczby podzielne przez x to : {wypisz_podzielne([5,6,60,66,1],6)}')

print("="*60)
#`pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`;
#zwraca `None`, jeśli takiej liczby tam nie ma


def piersza_podzielna(liczby:list, x:int):
    wynik = set()
    for znak in liczby:
        if znak % x == 0:
            wynik.add(znak)
            break
        if znak % x != 0:
            return None
    return wynik

print(f'Pierwsza liczba podzielna to: {piersza_podzielna([6,66,109],6)}')

print("="*60)

#`znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`,
# jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma



def znajdz_wspolny(liczby1, liczby2):
    wynik = []
    for element in liczby1:
        if element in liczby2:
            wynik.append(element)
    return wynik

print(f'Wspólne elementy dla dwóch list to: {znajdz_wspolny([1,5,6],[5,6,2])}')
