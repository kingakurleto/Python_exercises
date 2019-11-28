'''Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza,
ile trzeba zapłacić. Zasady są takie:
​
- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
​
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki'''

# Dane do programu
print('***** Witamy w hotelu Grand-Hotel *****')

wiek=int(input('Podaj swój wiek:  '))
ilosc_nocy=int(input('Podaj ilość nocy:   '))
cena=1
koszt_pobytu=cena*ilosc_nocy

if 0 <= wiek < 18:
    koszt_pobytu=100*ilosc_nocy
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')
if 18 <= wiek <65 and 0 < ilosc_nocy <= 1:
    koszt_pobytu=200*ilosc_nocy
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')
if 18 <= wiek <65 and 2 <= ilosc_nocy < 5:
    koszt_pobytu=180*ilosc_nocy
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')
if 18 <= wiek <65 and 5 <= ilosc_nocy < 100:
    koszt_pobytu=150*ilosc_nocy
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')
if 65 < wiek <100 and 0 < ilosc_nocy <= 1:
    koszt_pobytu=(200*ilosc_nocy)-(200*ilosc_nocy*0.1)
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')
if 65 < wiek <100 and 2 <= ilosc_nocy < 5:
    koszt_pobytu=(180*ilosc_nocy)-(180*ilosc_nocy*0.1)
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')
if 65 < wiek <100 and 5 <= ilosc_nocy < 100:
    koszt_pobytu=(150*ilosc_nocy)-(150*ilosc_nocy*0.1)
    print(f'Twój koszt pobytu wynosi: {koszt_pobytu}')






