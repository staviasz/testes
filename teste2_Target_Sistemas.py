fibo = [0,1]

numero_escolhido = int(input('Qual numero deseja verificar: '))

while True:
    fibo.append(fibo[-2] + fibo[-1])
    if fibo[-1] == numero_escolhido:
        print(f'O numero {numero_escolhido}, pertence a sequencia de fibonacci')
        break
    elif fibo[-1] > numero_escolhido:
        print(f'O numero {numero_escolhido}, não pertence a sequencia de fibonacci')
        break



