frase = input('Digite uma frase: ')

x = -len(frase)
frase_reversa = ''
i = -1
while i > -(len(frase)+1):
    frase_reversa += frase[i]
    print(frase_reversa)
    i -= 1
