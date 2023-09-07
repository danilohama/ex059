"""Crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
O seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

num1 = int(input('\033[37mPrimeiro valor:\033[0m '))
num2 = int(input('\033[37mSegundo valor\033[0m: '))
opcao = 0
while opcao != 5:
    print("""    [\033[32m1\033[32;0m] \033[31;05msomar\033[31;0m
    [\033[32m2\033[32;0m] \033[31;05mmultiplicar\033[31;0m
    [\033[32m3\033[32;0m] \033[31;05mmaior\033[31;0m
    [\033[32m4\033[32;0m] \033[31;05mnovos números\033[31;0m
    [\033[32m5\033[32;0m] \033[31;05msair do programa\033[31;0m""")
    opcao = int(input('>>>>\033[33m Qual opção deseja\033[33;0m? '))
    print('\033[36m=-=\033[0m' * 10)
    if opcao == 1:
        soma = num1 + num2
        print('\033[37mA soma entre\033[0m \033[32m{}\033[0m + \033[32m{}\033[0m é \033[32m{}\033[0m'
              ''.format(num1, num2, soma))
    elif opcao == 2:
        produto = num1 * num2
        print('\033[37mO resultado de\033[0m \033[32m{}\033[0m X \033[32m{}\033[0m é ''\033[0m{}\033[0m'
              ''.format(num1, num2, produto))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('\033[37;0mEntre\033[0m \033[32m{}\033[0m \033[37me\033[0m \033[32m{}\033[0m \033[37o maior número '
              'é\033[0m \033[32m{}\033[0m '.format(num1, num2, maior))
    elif opcao == 4:
        print('\033[37mInforma os números novamente!\033[0m')
        num1 = int('\033[37mPrimeiro Valor: \033[0m')
        num2 = int('\033[37m Segundo valor:\033[0m ')
    elif opcao == 5:
        print('\033[33mFinalizando...\033[0m')
        sleep(3)
        print('\033[33mFinalizando...\033[0m')
        sleep(2)
        print('\033[33mFinalizando...\033[0m')
        sleep(1)

    else:
        print('\033[32mOpção invalida. tente novamente\033[0m!')
    print('\033[36m=-=\033[0m' * 10)
print('\033[37mFim do programa! Volte sempre!')
