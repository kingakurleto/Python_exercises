''''### Zadanie 2.2 | Choinka
​
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach
"choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
​
```
    *
  * * *
* * * * *
'''

liczba = -1
iloscgwiazdek = int(input("Ile poziomów ma mieć choinka? :  "))
for x in range(0,iloscgwiazdek):
    liczba = liczba + 2
    print(" " * (iloscgwiazdek - x), "*" * liczba)


