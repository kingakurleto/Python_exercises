''' Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.'''


cena_ziemniakow = int(input('Podaj cenę ziemniaków:  '))

ile_chce_kupic_ziemniakow = int(input('Ile kg ziemniaków chcesz kupić? :  '))

koszt_zakupu_ziemniakow=cena_ziemniakow*ile_chce_kupic_ziemniakow

print(f'Za ziemniaki zapłacisz: {koszt_zakupu_ziemniakow} PLN')

cena_bananow = int(input('Podaj cenę bananów:  '))

ile_chce_kupic_bananow = int(input('Ile kg bananów chcesz kupić? :  '))

koszt_zakupu_bananow= cena_bananow*ile_chce_kupic_bananow

print(f'Za banany zapłacisz: {koszt_zakupu_bananow} PLN')

zaplata_za_caly_paragon= koszt_zakupu_ziemniakow+koszt_zakupu_bananow

print(f'Za cały paragon musisz zapłacić: {zaplata_za_caly_paragon}  PLN ')

co_wiecej= koszt_zakupu_bananow>koszt_zakupu_ziemniakow

if co_wiecej == True:
    print('Koszt zakupu bananów jest większy!')
else:
    print('Koszt zakupu ziemniaków jest większy!')

