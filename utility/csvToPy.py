'''
============================================================
Converte os arquivos kij.csv e substancias.csv que contêm as 
propriedades das substâncias em um arquivo .py que pode ser 
utilizado pela aplicação.

É necessário ter a biblioteca 'unidecode' instalada em seu
computador. Utilize o comando 'pip install unidecode' para
realizar a instalação.

Não utilize caracteres especiais, tais como '()', '[]', '@',
'#', '$' etc ao dar nome às substancias.
============================================================
'''
from csv import reader
from unidecode import unidecode

def get_data() -> str:
    substancias = []
    substances = []
    sustancias = []
    elementos = []
    data = ''

    tabela.pop(0) # remover cabeçalho

    for i in range(len(tabela)):
        substancias.append(tabela[i][0])
        substances.append(tabela[i][1])
        sustancias.append(tabela[i][2])

        for j in range(3, len(tabela[0])):
            tabela[i][j] = tabela[i][j].replace(",",".")

    # obtendo nome para as variáveis python
    for z in range(len(substancias)):
        subs = substancias[z].replace('-','_').replace(' ', '_')
        subs = subs.lower()
        subs = unidecode(subs)
        elementos.append(subs)

    # declarando variáveis com propriedades de cada uma das substancias
    for i in range(len(tabela)):
        data += elementos[i] + ' = ['
        
        for j in range(3, len(tabela[i])):
            data += tabela[i][j]
            if j != len(tabela[i])-1:
                data += ', '

        data += ']\n'

    data += '\nELEMENTOS = ['
    for i in range(len(elementos)):
        data += elementos[i]
        if i != len(elementos)-1:
            data += ', '
        if i % 10 == 0 and i != 0:
            data += '\n'
    data += ']\n\n'
        
    data += 'SUBSTANCIAS = ['
    for i in range(len(substancias)):
        data += '"'+substancias[i]+'"'
        if i != len(substancias)-1:
            data += ', '
        if i % 10 == 0 and i != 0:
            data += '\n'
    data += ']\n'

    data += 'SUBSTANCES = ['
    for i in range(len(substances)):
        data += '"'+substances[i]+'"'
        if i != len(substances)-1:
            data += ', '
        if i % 10 == 0 and i != 0:
            data += '\n'
    data += ']\n'
    
    data += 'SUSTANCIAS = ['
    for i in range(len(sustancias)):
        data += '"'+sustancias[i]+'"'
        if i != len(sustancias)-1:
            data += ', '
        if i % 10 == 0 and i != 0:
            data += '\n'
    data += ']\n\n'

    data += '# Número de fluidos cadastrados\n'
    data += 'NUM_SUBSTANCIAS = ' + str(len(substancias)) + '\n'

    return data

def get_kij() -> str:
    kij = '#Tabela kij\nKIJ = [\n'

    tabela.pop(0) # remover cabeçalho
    
    for i in range(len(tabela)):  
        tabela[i].pop(0)
        for j in range(len(tabela)):
            if tabela[i][j] == "<empty>":
                tabela[i][j] = 0
            else:
                tabela[i][j] = tabela[i][j].replace(",",".")
                tabela[i][j] = float(tabela[i][j])
    
    for linha in tabela:
        kij += '\t['
        for valor in linha:
            kij += str(valor) + ', '

        kij += '],\n'
    
    kij += ']\n'

    return kij

conteudo = '# -*- coding: utf-8 -*-'+\
        '\n\n# ============================================================'+\
        '\n#                          CONSTANTES                         '+\
        '\n# ============================================================\n\n'
                
# Ler arquivo que contém valores kij
nome_arquivo = 'data/kij.csv'
tabela = []
with open(nome_arquivo, encoding='utf-8') as arquivo:
        data = reader(arquivo, delimiter=',')
        for linha in data:
            tabela.append(linha)

try:
    conteudo += get_kij()
except:
    print('ERRO: Preencha o arquivo kij.csv corretamente!')

# Ler arquivo que contém nomes das substâncias e valores de suas propriedade
conteudo += '\n# Listas dos fluidos\n'+\
            '# [Massa molar(g/mol), Pressão crítica(KPa), Temperatura crítica (K), Fator acênctrico]\n'

nome_arquivo = 'data/substancias.csv'
tabela = []
with open(nome_arquivo, encoding='utf-8') as arquivo:
        data = reader(arquivo, delimiter=',')
        for linha in data:
            tabela.append(linha)

try:
    conteudo += get_data()
except:
    print('ERRO: Preencha o arquivo substancias.csv corretamente!')

# Escrever arquivo .py de constantes
arquivo = open('src/constant.py', 'w', encoding='utf-8')
arquivo.writelines(conteudo)
arquivo.close()