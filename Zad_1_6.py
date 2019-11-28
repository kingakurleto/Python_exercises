'''
Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90
​
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
​
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
'''

print('Witamy w kinie Wenus')

wiek=int(input('Podaj swój wiek:   '))

ilosc_biletow=int(input('Podaj ilość biletów które chcesz kupić:  '))

cena=(0,2.28,3.80,1.90)

koszt_biletów=cena*ilosc_biletow

if 0 < wiek <= 6:
    koszt_biletów=0*ilosc_biletow
    print(f'Koszt biletów wynosi: {koszt_biletów}')
if 6 < wiek <= 17:
    koszt_biletów = 2.28 * ilosc_biletow
    print(f'Koszt biletów wynosi: {koszt_biletów}')
if 17 < wiek <= 64:
    koszt_biletów = 3.8 * ilosc_biletow
    print(f'Koszt biletów wynosi: {koszt_biletów}')
if 64 < wiek <= 200:
    koszt_biletów = 1.9 * ilosc_biletow
    print(f'Koszt biletów wynosi: {koszt_biletów}')
