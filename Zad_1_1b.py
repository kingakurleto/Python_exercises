'''Potem napisz program, który prosi użytkownika (przez `input()`),
żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.'''


cena_ziemniakow = int(input('Podaj cenę ziemniaków:  '))

ile_chce_kupic = int(input('Ile kg ziemniaków chcesz kupić? :  '))

koszt_zakupu=cena_ziemniakow*ile_chce_kupic

print(f'Do zapłaty masz: {koszt_zakupu} PLN')
