'''### Zadanie 2.1 | Zagadka matematyczna
​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka
 jest ich suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
 Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
'''

import random

liczba1 = random.randrange(0, 101)
print(f'Pierwsza wylosowana liczba to: {liczba1}')
liczba2 = random.randrange(0, 101)
print(f'Druga wylosowana liczba to: {liczba2}')

suma=int(input('Wpisz sumę liczb: '))

while liczba1 + liczba2 == suma:
    print('Odgadłeś dobrą liczbę !')
    break
if liczba1 + liczba2 != suma:
    print('Próbuj jeszcze raz..')










