'''Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
 (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawda?), a jeśli mogą, oblicza pole powierzchni
 trójkąta o takich bokach.
​
Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
​
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
​
```
import math
​
x = math.sqrt(10)
'''

#a, b, c - długości boków trójkąta

#a + b musi być większe niż c

#a + c musi być większe niż b

#b + c musi być większe niż a

import math



a=int(input('Podaj długość boku a: '))
b=int(input('Podaj długość boku b: '))
c=int(input('Podaj długość boku c:  '))

p=0.5*(a+b+c)
Pole=math.sqrt(p)


if a+b>c and a+c>b and b+c>a:
    print(f'Pole trójkąta wynosi: {Pole} !')
else:
    print('Zweryfikuj długość wszystkich boków! Któryś bok jest za krótki.')



