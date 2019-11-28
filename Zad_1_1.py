'''Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
'''

cena_ziemniakow= int(input('Proszę podać cenę ziemniaków:   '))

koszt_zakupu=5*cena_ziemniakow

print(f'Koszt zakupu 5 kg ziemniaków to: {koszt_zakupu:.2f} zł')
