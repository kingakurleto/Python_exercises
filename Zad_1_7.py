'''Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić
i jaka jest jego cena. Wyświetl odpowiedni komunikat.
​
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
​
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
'''

print('Witamy w sieci sklepów Żabka')

produkt=str(input('Podaj produkt który chcesz kupić?:    '))
cena=int(input('Podaj cenę towaru:   [zł]'))
ilosc=int(input('Podaj ilość towaru:  [szt]'))

koszt=cena*ilosc

print(f'Za {produkt} zapłacisz {koszt} zł')

