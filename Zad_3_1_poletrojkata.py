#   6) "Pole trójkąta" - z trzema parametrami - oblicza pole trójkąta o podanych bokach z
 #wzoru Herona.

import math


a=int(input('Podaj długość boku a: '))
b=int(input('Podaj długość boku b: '))
c=int(input('Podaj długość boku c:  '))

p=0.5*(a+b+c)
Pole=math.sqrt(p)

def pole_trojkata(a:int,b:int,c:int) -> float:
    if a+b>c and a+c>b and b+c>a:
        return Pole
    else:
        raise ValueError('Któryś bok jest za krótki - zweryfikuj długości')


print(f'Pole trójkąta wynosi:  {pole_trojkata(a,b,c)} ')
