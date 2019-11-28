'''Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli
 `Fizz`; dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli
 `FizzBuzz`.
'''


ile = 1
for i in range(0, 101):
    if i % 3 == 0:
        print(f' {i}, Fizz')
    if i % 5 == 0:
        print(f'{i},Buzz')
    if i % 15 == 0:
        print(f'{i},Fizzbuzz')
