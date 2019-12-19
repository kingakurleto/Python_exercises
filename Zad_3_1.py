'''### Zadanie 3.1 Funkcje liczbowe
​
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia
i zwraca przeliczoną wartość.
​
1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb,
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach
i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z
 wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
​
Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i
wypisują wynik.
​
'''
#------------------------->Funkcje<--------------------------------

#  1)  stopy na metry:

#1 stopa = 0,3048 metra

def stopy_na_metry(stopa:int) ->int:
    return stopa*0.3048

def test_stopy_na_metry():
    assert stopy_na_metry(25)==7.62

print('Stopa dla liczby to 58 : ', stopy_na_metry(58))

print("="*60)

#  2)   funkcja max :

def funkcja_max(a: int,b: int) ->int:
    return max(a,b)

def test_funkcji_max():
    assert funkcja_max(10,1)==10

print('Funkcja max z liczb 4 i 3 wynosi : ', funkcja_max(4,3))

print("="*60)

#   3)   średnia :

def srednia(a:float,b:int,c:float) ->float:
    return (a+b+c)/3

def test_srednia():
   assert srednia(3,4,134)==47

print('Średnia z podanych liczb 3,4,134 wynosi :',srednia(3,4,134))

print("="*60)
#  4) Pole_koła - oblicza pole koła o podanym promieniu (jeden parametr)
# podpowiedź: wartość PI jest dostępna jako `Math.PI`

#pole = pi*r2

import math
pi= math.pi

def pole_kola(r:int, pi) ->int:
    return pi*(r**2)

print('Pole koła o promieniu 3 wynosi: ', pole_kola(3,pi))

def test_pole_kola():
    assert pole_kola(3,pi)==28.274333882308138

print("="*60)
#  5) "BMI" - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.

#waga/(wzrost**2)

def bmi(wzrost:int, waga:int) ->int:
    return waga/(wzrost**2)

print(f'BMI dla osoby o wzroście 175 i 70 kg wagi wynosi: {bmi(1.75,70)}')

def test_bmi():
    assert bmi(1.75,70)==22.857142857142858

print("="*60)

#7) "Kilometry na mile" - przelicza odległość wyrażoną w kilometrach na mile

#1 kilometr = 0,621371192 mili
# x         - 1 mila

def kilometry_namile(a:int) ->int:
    return a*0.621371192

def test_kilometry_namile():
    assert kilometry_namile(3)==1.864113576

print('1 kilometr w przeliczeniu na mile to: ', kilometry_namile(1))

print("="*60)


#8) "Mile na kilometry" - przelicza odległość wyrażoną w milach na kilometry

def mile_na_kilometry(a:int) ->int:
    return a/0.621371192

def test_mile_na_kilometry():
    assert mile_na_kilometry(1)==1.6093440006146922

print('1 kilometr w przeliczeniu na mile to: ', kilometry_namile(1))

print("="*60)

