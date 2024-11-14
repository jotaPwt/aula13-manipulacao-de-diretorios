import os

import shutil

# **Exercício 1: Criar e ler um Arquivo**

def ler():

    with open('texto.txt', 'r') as ler:
        leitura = ler.read()
        
    print(leitura)

# **Exemplo 2: Entrar em um Diretório**

def criar_arq():

    with open('criar.py', 'w') as criar:
        os.mkdir('criar.py')
        print('feito')

# **Exercício 3: Renomear um Diretório**

def renomear():
    os.rename('criar.py', 'criar.js')

# # **Exercício 4: Remover um Diretório**
    
def remover():
    shutil.rmtree('c:/Users/aluno/Desktop/aula13-manip-de-diretórios')


# **Exercício 5: Listar Arquivos em um Diretório** 
def listar_arqs():

    with os.scandir('c:/Users/aluno/Desktop/aula13-manip-de-diretórios') as entrada:
        for arquivos in entrada:
            print('Arquivo > ', arquivos.name)

**Exercício 6: Copiar Arquivos em um Diretório**
        
criar_arq()


shutil.copytree('pasta', 'copia.js')


