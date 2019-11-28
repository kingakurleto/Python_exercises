'''### Zadanie 2.3
​
Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum
'''

liczby = []

while len(liczby) < 3:
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)

srednia = sum(liczby) / len(liczby)
print(f'Średnia z wprowadzonych liczb to : {srednia}')
minimum=min(liczby)
print(f'Wartość mimimum z wpisanych liczb to: {minimum}')
maximum=max(liczby)
print(f'Wartość maximum z wpisanych liczb to: {maximum}')
count=len(liczby)
print(f'Ile podano liczb: {count}')
suma=sum(liczby)
print(f'Suma podanych liczb to: {suma}')




