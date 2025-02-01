from time import sleep
import string
import random
from defs import linha
from defs import linhatam
from defs import exits

c = 0      
usuarios = list() 
class GeradorX():
    def __init__(self):
        id_token = ''
        cont = 0
        while True:
            try:
                caracters = int(input('Digite o tamanho do seu id:'))
                if caracters <= 0:
                    print('digite um numero positivo, tente novamente!'.upper())
                    linha()
                    continue
                break
            except Exception as erro:
                linha()
                print(f'Algum erro encontrado --> {erro}\n')
                linha()
        nome = str(input('Digite seu nome:'))
        gera_hex = string.hexdigits 
        for itens in range(caracters):
            cont += 1
            id_token += random.choice(gera_hex)
            print(f'{itens+1} - loading...',flush=True)
        linha()
        print(f'Olá {nome}, seu ID_token é: {id_token} & tem {cont} caracteres')
        usuarios.append(f'{nome} ')
        usuarios.append(f'"{id_token}"\n')
        
        with open('usuarios.txt', 'r') as arq:
            if arq.read() == '':
                with open('usuarios.txt', 'w') as arquivo:
                    arquivo.write('Nome  |  ID_Token\n\n')

        with open('usuarios.txt', 'a') as users:
            for i in usuarios:
                users.write(i)
            usuarios.clear()

           
while True:
    print('Gerador-Hexadecimal (1)\n'
          'Sair                (2)\n')
    opcao = int(input('Digite sua opção:'))
    if opcao == 1:
        while True:
            continuar = ' '
            linhatam('<Gerador-Hexadecial>')
            GeradorX()
            c += 1
            while continuar not in 'SN':
                linha()
                continuar = str(input('Quer continuar [S/N]:')).upper().strip()[0]
            if continuar == 'N':
                break
    elif opcao == 2:
        break            

linhatam(f'Você cadastrou {c} usuarios no sistema'.center(100)) 
print('usuarios salvos no arquivo: usuarios.txt')
linha()
sleep(0.1)
linhatam('Obrigado, volte sempre'.center(100))       
exits()