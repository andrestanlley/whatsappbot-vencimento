from dados import *
import os

revenda = int(input('Revendedor (1 - revenda1, 2 - revenda2, 3 - revenda3.): '))
while True:
    if revenda == 1:
        arq = 'revenda1.txt'
    elif revenda == 2:
        arq = 'revenda2.txt'
    elif revenda == 3:
        arq = 'revenda3.txt'
    else:
        break
    print('Iniciando novo cadastro!\n')
    nome = str(input('Nome: '))
    numero = int(input('Celular(DDD): '))
    vencimento = int(input('Vencimento: '))
    registro(arq, nome, numero, vencimento)
    os.system('cls')
