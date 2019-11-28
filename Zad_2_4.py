'''### Zadanie 2.4 | Zgadnij liczbę z zakresu
​
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik,
program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując,
 w której próbie udało się zgadnąć liczbę.
​
Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za
mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę. Umiejętnie ją
stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).'''

import random

liczba=random.randrange(0, 1000)
print(f'Losowana liczba: {liczba} (nie widzisz jej)')

for i in range(0,1000):
    liczbasprawdzenie=int(input('Zgadnij liczbę:  '))
    if liczba>liczbasprawdzenie:
        print('Liczba jest za mała')
    elif liczba<liczbasprawdzenie:
        print('Liczba jest za duża')
    elif liczba==liczbasprawdzenie:
        print(f'Gratulacje, to dobra liczba :), zgadłeś za {i+1} razem !')
        break

