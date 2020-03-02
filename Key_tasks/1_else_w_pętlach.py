instruction = ['say hello', 'say how are you?', 'abort', 'ask for money']
instructionApprowed = []

for inst in instruction:
    print('Adding instruction', inst)
    instructionApprowed.append(inst)

    if inst == 'abort':
        print('Aborting!')
        instructionApprowed.clear()
        break
print('Following actions will be taken', instructionApprowed)