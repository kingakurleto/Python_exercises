'''Napisz program FizzBuzz
Wypisz wszystkie liczby od 1 do 100
Jeśli liczba jest podzielna przez trzy wypisz “Fizz“
Jeśli liczba jest podzielna przez pięć wypisz “Buzz“
Jeśli liczba jest podzielna przez trzy i pięć wypisz “FizzBuzz“'''

for x in range(0,101):
    print(x)
    if x % 3 == 0:
        print(f' {x} - Fizz')
    if x % 5 == 0:
        print (f'{x}  Buzz')
    if x % 3 == 0  and x % 5 == 0:
        print (f' {x} FizzBuzz')

