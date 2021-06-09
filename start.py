from dados import *
import os

# Para adicionar novas revendas, você deve copiar esse padrão nos arquivos start/cadastrar/dados, incluindo funções com o seu nome.

abrir()
arq = 'revenda1.txt'
notificar(arq, revenda1)
avisar('revenda1')              # Caso seja apenas um revendedor, você pode deixar comentado até a linha 13. 
arq = 'revenda2.txt'
notificar(arq, revenda2)
avisar('revenda2')
arq = 'revenda3.txt'
notificar(arq, revenda3)
avisar('revenda3')
browser.quit()
os.system('shutdown /s /t 0')
