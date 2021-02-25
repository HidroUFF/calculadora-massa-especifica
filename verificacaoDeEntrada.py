import re

def verificarCamposEmBranco(vetor, pressaoUnica):
    '''
    Verifica se existem campos em branco nos dados de entrada
    :param vetor: lista com todos os dados de entrada no formato
                  vetor = [dados referentes a composicao da mistura, temperatura, pressao] 
    :param presssaoUnica: boolean indicando se existe um único valor de pressao ou um intervalo
    :return: True, se existem campos em branco; False, caso contrário
    '''
    composicao = vetor[0]
    temperatura = vetor[1]
    pressao = vetor[2]

    for substancia in composicao:
        if substancia[1] == '':
            return True

    if temperatura[1] == "":
        return True

    if pressaoUnica:
        if pressao == "":
            return True
    else:
        for p in pressao:
            if p == "":
                return True

    return False

def verificarSubstanciasRepetidas(vetor):
    '''
    Verifica se foram selecionadas substancias repetidas entre os dados de entrada da composicao da mistura
    :param vetor: matriz com os elementos dinamicos da interface refentes a composicao da mistura
                  cada linha corresponde a um vetor = [frame, comboBox, lineEdit, pushButton] 
    :return: True, se existem substancias repetidas; False, caso contrário
    '''

    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if vetor[i][0] == vetor[j][0] and i != j:
                return True
                
    return False

def verificarArquivo(dados, t):
    '''
    Verifica se arquivo .csv de entrada tem o conteudo no formato correto
    :param dados: vetor que contem todas as linhas do arquivo lido
    :return: True, se o arquivo é integro; False, caso contrário
    '''

    for i in range(1, len(dados)):
        aux = re.search("^[0-9]{1,20}([.])?([eE][-+])?[0-9]{1,20}[;][0-9]{1,20}([.])?([eE][-+])?[0-9]{1,20}$", dados[i])
        
        if aux != None:
            dados[i] = aux.string
        else:
            return False

    temp = re.search("^[0-9]{1,20}([.])?([eE][-+])?[0-9]{1,20}$", t)
    if temp == None:
        return False

    return True
