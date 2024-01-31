from time import sleep
import sys
import string
import random

def linha():
    print('')
    
def linhatam(msg):
    print('='* len(msg))
    print(f'{msg}')
    print('=' *len(msg))
        
def exits():
    sleep(0.5)
    print('saindo...', flush=True)
    sleep(0.5)
    print(sys.exit())     
    
c = 0      
usuarios = list() 
class GeradorX():
    def __init__(self):
        id_token = ''
        cont = 0
        while True:
            try:
                caracters = int(input('Digite o tamanho do seu id:'))
                break
            except Exception as erro:
                print(f'algum erro encontrado {erro}\n'
                      'digite numeros'.upper())
        nome = str(input('Digite seu nome:'))
        gera_hex = string.hexdigits 
        for itens in range(caracters):
            cont += itens / 2
            id_token += random.choice(gera_hex)
        print(f'Olá {nome}, seu ID é: {id_token}, e contem {cont:.1f} caracteres')
        usuarios.append(f'{nome} ')
        usuarios.append(f'"{id_token}"\n')
        with open('usuarios.txt', 'w') as users:
            for posi,item in enumerate(usuarios):
                if posi == 0:
                    users.write('Nome de usuario & ID_token:\n\n')
                users.write(item)
            
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
sleep(0.5)
linhatam('Obrigado, volte sempre'.center(100))       
exits()