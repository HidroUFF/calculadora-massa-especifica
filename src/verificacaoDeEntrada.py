import re

'''
Module responsible for data entry verification.
'''

def verificar_campos_em_branco(vetor, pressaoUnica) -> bool:
    '''
    Checks for blank fields in input data.
    :param vetor: list with all input data in format
                   vector = [data regarding the composition of the mixture, temperature, pressure] 
    :param presssaoUnica: boolean indicating if there is a single pressure value or an interval
    :return: True, if there are blank fields; False otherwise.
    :rtype: bool
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

def verificar_substancias_repetidas(vetor) -> bool:
    '''
    Checks whether repeated substances were selected from the mixture composition input data.
    :param vetor: matrix with the dynamic elements of the interface referring to the composition of the mixture 
                each line corresponds to a vector = [frame, comboBox, lineEdit, pushButton] 
    :return: True, if there are repeated substances; false otherwise.
    :rtype: bool
    '''

    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if vetor[i][0] == vetor[j][0] and i != j:
                return True
                
    return False

def verificar_arquivo(dados, t) -> bool:
    '''
    Checks if input .csv file has content in correct format.
    :param dados: vector containing all lines of the read file
    :return: True, if the file is whole; false otherwise.
    :rtype: bool
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
