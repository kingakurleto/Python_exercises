'''Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.).
Ma też podać, ile dni będzie trwała naprawa.
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.'''


data_oddania=str(input('Podaj dzień oddania obuwia (poniedziałek,wtorek,środa,czwartek,piątek):  '))
naprawa=int(input('Podaj długość naprawy obuwia:  '))

if data_oddania == 'poniedziałek':
    wynik= naprawa + 1
    print(f'Buty będą do odbioru w  : {wynik}')
elif data_oddania == 'wtorek':
    wynik=naprawa + 2
    print(f'Buty będą do odbioru w  : {wynik}')
elif data_oddania == 'środa':
    wynik = naprawa + 3
    print(f'Buty będą do odbioru w  : {wynik}')
elif data_oddania == 'czwartek':
    wynik = naprawa + 4
    print(f'Buty będą do odbioru w  : {wynik}')
elif data_oddania == 'piątek':
    wynik = naprawa + 5
    print(f'Buty będą do odbioru w  : {wynik}')
    