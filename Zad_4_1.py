
#Dodawanie liczb z listy

sequence = input().split(',')

conv = []

for i in sequence:
    conv.append(int(i))

print(sum(conv))

