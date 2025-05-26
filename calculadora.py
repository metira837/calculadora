n1 = (int(input('escolha o primeiro numero:\n')))
n2 = (int(input('escolha o segundo numero:\n')))
resposta = input('digite qual jeito vai calcular:\n x , +, /, -\n')

if resposta == 'x':
    print(f'a soma deu {n1*n2}')
elif resposta == '/':
    print(f'a soma deu {n1/n2}')
elif resposta == '-':
    print(f'a soma deu {n1-n2}')
elif resposta == '+':
    print(f'a soma deu {n1+n2}')