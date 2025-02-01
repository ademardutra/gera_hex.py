from time import sleep
import sys

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
    