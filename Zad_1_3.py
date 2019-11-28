'''Napisz trzy programy, które dla podanych liczb: wzrostu w cm i masy ciała
w kg obliczą i wypiszą współczynnik BMI, oraz podsumowanie informujące o stanie/zaleceniach.
(Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
Programy mają różnić się sposobem interakcji z użytkownikiem. '''

masa_ciala=int(input('Podaj masę ciała:  [KG] '))
wzrost=float(input('Podaj wzrost:   [M] '))
bmi=masa_ciala/(wzrost**2)

if 0 <= bmi <= 16:
    print(f'Twoje bmi wynosi {bmi} to wygłodzenie!! Zjedz coś :<')
if 16 < bmi < 19:
    print(f'Twoje bmi wynosi {bmi} to niedowaga!!')
if 19 < bmi < 25:
    print(f'Twoje bmi wynosi {bmi} to optymalna masa ciała! :) Gratulacje!')
if 25 < bmi < 30:
    print(f'Twoje bmi wynosi {bmi} to niestety nadwaga! :/ Ruszaj się więcej!')
if 30 < bmi < 35:
    print(f'Twoje bmi wynosi {bmi} to już OTYŁOŚĆ! :(')
