'''### Zadanie 3.2 | Miesiące
​
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​
Logikę obliczania liczby dni wydziel do osobnej funkcji.
​
**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
​
**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był
 przestępny czy nie.
​'''

#Rok jest przestępny, gdy jest podzielny przez 4 i nie jest podzielny przez 100
# lub jest podzielny przez 400. Np. 2012, 1996, 2000 to lata przestępne, natomiast 1900,
# 2001, 1998 nie są przestępne.

miesiac=input('Podaj miesiąc:  ')


def czy_przestepny(rok):
    return (rok % 4 == 0 and  rok % 100 != 0 and rok % 400 != 0)

def dni_miesiac(miesiac, rok):
    if miesiac == 'Wrzesień' or miesiac == 'Kwiecień' or miesiac == 'Czerwiec' or miesiac == 'November':
        wynik=30
    elif miesiac == 'Styczeń' or miesiac== 'Marzec' or miesiac == 'Maj' or miesiac== 'Lipiec' or miesiac == 'Sierpień' or miesiac == 'Październik'or miesiac== 'Grudzień':
        wynik=31
    elif miesiac == 'Luty' and czy_przestepny(rok) == True:
        wynik=29
    elif miesiac == 'Luty' and czy_przestepny(rok) == False:
        wynik=28
    return wynik

print('Ilość dni dla podanego miesiąca to:')
print(dni_miesiac(f'{miesiac}',2019))