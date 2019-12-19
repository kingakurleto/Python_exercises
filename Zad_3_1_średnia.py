#średnia :

przywitanie=print(' Program oblicza średnią z 3 liczb, podaj je aby uzyskać wynik.')
a=int(input('Podaj liczbę a: '))
b=int(input('Podaj liczbę b : '))
c=int(input('Podaj liczbę c : '))

def srednia(a:float,b:int,c:float) ->float:
    return (a+b+c)/3

def test_srednia():
   assert srednia(3,4,134)==47

print('Średnia z podanych liczb wynosi :',srednia(a,b,c))