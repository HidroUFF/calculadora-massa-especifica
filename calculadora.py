from io import StringIO
from sympy import solveset, S, Symbol, functions
import matplotlib.pyplot as plt
from datetime import datetime
from math import sqrt, exp

###   CONSTANTES   

# TABELA Kij
kij = [
    [0, 0.00224, 0.1, 0.036, 0.00683, 0.0123, 0.085, 0.0219, 0.0395, 0.03097, 0.05121, 0.044, 0.04701, 0.01427, 0.0392, 0.04, 0.0649, 0.5, 0.03496, 0.023, ],
    [0.00224, 0, 0.1298, 0.050, 0.00126, 0.0041, 0.084, 0.0082, 0.00042, 0.0032, 0.0167, 0.02199, 0.007, -0.00074, 0.0261, 0.02, 0.0344, 0.5, 0.05351, 0.05, ],
    [0.1, 0.1298, 0, -0.02, 0.135, 0.1298, 0.1, 0.125, 0.125, 0.1199, 0.115, 0.1037, 0.1181, 0.09545, 0.0901, 0.0806, 0.0936, -0.5572, 0.0975, 0.0, ],
    [0.036, 0.05, -0.02, 0, 0.08, 0.09, 0.1676, 0.1015, 0.1415, 0.1535, 0.171, 0.1778, 0.1205, 0.21136, 0.1, 0.1597, 0.1932, -2.238, -0.012, 0.0, ],
    [0.00683, 0.00126, 0.135, 0.08, 0.00, 0.00082, 0.075, 0.00471, 0.00682, 0.00769, 0.00725, 0.00697, 0.0062, -0.01397, 0.0143, 0.02, 0.031, 0.48, 0.07318, 0.03753, ],
    [0.01230, 0.004100, 0.12980, 0.090, 0.000820, 0, 0.06, -3e-05, 0.00091, 0.00083, -0.00032, -0.00118, -0.00239, -0.02143, 0.00578, 0.01019, 0.00601, 0.48, 0.09399, 0.1151, ],
    [0.085, 0.084, 0.1, 0.1676, 0.075, 0.06, 0, 0.04972, 0.05915, 0.06596, 0.055, 0.05, 0.0356, -0.00488, 0.05874, 0.009, 0.0081, -0.3896, 0.0, 0.0, ],
    [0.0219, 0.0082, 0.125, 0.1015, 0.00471, -3e-05, 0.04972, 0, -0.00049, -0.00117, -0.00277, -0.00399, -0.00546, -0.02365, 0.0013, 0.016, 0.013, 0.48, 0.11518, 0.0713, ],
    [0.0395, 0.00042, 0.125, 0.1415, 0.00682, 0.00091, 0.05915, -0.00049, 0, -0.00184, -0.0038, -0.0053, -0.00701, -0.02478, -0.003, 0.007, 0.008, 0.48, 0.095, 0.02132, ],
    [0.03097, 0.0032, 0.1199, 0.1535, 0.00769, 0.00083, 0.06596, -0.00117, -0.00184, 0, -0.00292, -0.00463, -0.0065, -0.02394, -0.0072, -0.002, 0.006, 0.48, 0.1587, 0.0866, ],
    [0.05121, 0.0167, 0.115, 0.171, 0.00725, -0.00032, 0.055, -0.00277, -0.0038, -0.00292, 0, -0.00257, -0.00456, -0.02171, -0.00906, 0.003, -0.004, 0.48, 0.156, 0.11463, ],
    [0.044, 0.02199, 0.1037, 0.1778, 0.00697, -0.00118, 0.05, -0.00399, -0.0053, -0.00463, -0.00257, 0, -0.0028, -0.01984, -0.01051, -0.00524, -0.00953, 0.48, 0.20298, 0.11241, ],
    [0.04701, 0.007, 0.1181, 0.1205, 0.0062, -0.00239, 0.0356, -0.00546, -0.00701, -0.0065, -0.00456, -0.0028, 0, -0.01768, 0.01, 0.01, 0.01, 0.48, 0.22529, 0.12404, ],
    [0.01427, -0.00074, 0.09545, 0.21136, -0.01397, -0.02143, -0.00488, -0.02365, -0.02478, -0.02394, -0.02171, -0.01984, -0.01768, 0, -0.03171, -0.00746, -0.02722, 0.48, 0.3305, 0.14388, ],
    [0.0392, 0.0261, 0.0901, 0.1, 0.0143, 0.00578, 0.05874, 0.0013, -0.003, -0.0072, -0.00906, -0.01051, 0.01, -0.03171, 0, 0.02012, 0.003, 0.48, 0.11405, 0.04707, ],
    [0.04, 0.02, 0.0806, 0.1597, 0.02, 0.01019, 0.009, 0.016, 0.007, -0.002, 0.003, -0.00524, 0.01, -0.00746, 0.02012, 0, 0.009, 0.48, 0.09588, 0.03466, ],
    [0.0649, 0.0344, 0.0936, 0.1932, 0.031, 0.00601, 0.0081, 0.013, 0.008, 0.006, -0.004, -0.00953, 0.01, -0.02722, 0.003, 0.009, 0, 0.48, 0.208, 0.06096, ],
    [0.5, 0.5, -0.5572, -2.238, 0.48, 0.48, -0.3896, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0, 0.0, 0.5, ],
    [0.03496, 0.05351, 0.0975, -0.012, 0.07318, 0.09399, 0.0, 0.11518, 0.095, 0.1587, 0.156, 0.20298, 0.22529, 0.3305, 0.11405, 0.09588, 0.208, 0.0, 0, 0.0104, ],
    [0.023, 0.05, 0.0, 0.0, 0.03753, 0.1151, 0.0, 0.0713, 0.02132, 0.0866, 0.11463, 0.11241, 0.12404, 0.14388, 0.04707, 0.03466, 0.06096, 0.5, 0.0104, 0, ]
]

# listas fluidos
# [Massa molar(g/mol), Pressão crítica(KPa), Temperatura crítica (K), Fator acênctrico]
metano = [16.04, 4641, 190.55, 0.0115]
etano = [30.07, 4884, 305, 0.0986]
co2 = [44.01, 7370, 304.13, 0.2389]
n2 = [28.01, 3394.00, 130.0, 0.0400]
propano = [44.1, 4257.0, 369.75, 0.1524]
nbutano = [58.12, 3797.0, 425, 0.2010]
h2s = [34.08, 9008.0, 373.65, 0.081]
n_pentano = [72.15, 3419.72, 469.5, 0.2539]
n_hexano = [86.18, 3072.17, 507.7, 0.3007]
n_heptano = [100.21, 2773.27, 540.0, 0.3498]
n_octano = [114.23, 2530.09, 568.4, 0.4018]
n_nonano = [128.2, 2330.48, 594.4, 0.4455]
n_decano = [170.33, 2135.93, 617.4, 0.4885]
n_pentadecano_C15 = [212.42, 1537.1, 706.9, 0.706]
ciclohexano = [84.16, 4106.7, 553.1, 0.2133]
benzeno = [78.11, 4989.24, 561.9, 0.215]
tolueno = [92.14, 4154.33, 591.6, 0.2596]
agua_pura = [18.01528, 22413.09, 647.1, 0.344]
gas_oxigenio_O2 = [15.999, 5147.31, 154.6, 0.019]
argonio = [39.948, 4928.45, 150.6, -0.004]

elementos = [metano, etano, co2, n2, propano, nbutano, h2s, n_pentano, n_hexano, n_heptano, n_octano, n_nonano,
            n_decano, n_pentadecano_C15, ciclohexano, benzeno, tolueno, agua_pura, gas_oxigenio_O2, argonio]

# ATENÇÃO: Ao inserir novos elementos no vetor elementos, insira-os nos vetores
# SUBSTANCIAS, SUBSTANCES e SUSTANCIAS seguindo o mesmo padrão para manter a integridade  
# e funcionamento da calculadora.
SUBSTANCIAS = ["METANO", "ETANO", "CO2", "N2", "PROPANO", "N-BUTANO", "H2S", "N-PENTANO", "N-HEXANO", "N-HEPTANO", "N-OCTANO","N-NONANO", 
              "N-DECANO", "N-PENTADECANO", "CICLO-HEXANO", "BENZENO", "TOLUENO", "ÁGUA PURA", "GÁS OXIGÊNIO", "ARGÔNIO"]
SUBSTANCES = ["METHANE", "ETHANE", "CO2", "N2", "PROPANE", "N-BUTANE", "H2S", "N-PENTANE", "N-HEXANE", "N-HEPTANE", "N-OCTANE","N-NONANE",
               "N-DECAN", "N-PENTADECAN", "CYCLOHEXANE", "BENZENE", "TOLUENE", "PURE WATER", "OXYGEN GAS", "ARGON"]
SUSTANCIAS = ["METANO", "ETANO", "CO2", "N2", "PROPANO", "N-BUTANO", "H2S", "N-PENTANO", "N-HEXANO", "N-HEPTANO", "N-OCTANO","N-NONANO", 
              "N-DECANO", "N-PENTADECANO", "CICLO-HEXANO", "BENCENO", "TOLUENO", "AGUA PURA", "GAS OXIGENO", "ARGÓN"]
NUM_SUBSTANCIAS = len(elementos) # número de fluidos cadastrados
ESCALAS_DE_TEMPERATURA = ["CELSIUS", "FAHRENHEIT", "KELVIN"]

# Internacionalização
# Strings utilizadas para nomear os labels do aplicativo na ordem: português (codigo==0), inglês (codigo==1) e espanhol (codigo==2).
STRINGS = {"title": ["Massa Específica a", "Density at", "Desidad a"],
           "label_x": ["Pressão ", "Pressure", "Presión"],
           "label_y": ["Massa específica", "Density", "Densidad"],
           "composicao": ["Composição", "Composition", "Composición"],
           "substancia": ["Substância", "Substance", "Sustancia"],
           "fracao_molar": ["Fração Molar", "Molar fraction", "Fracción molar"],
           "temperatura": ["Temperatura", "Temperature", "Temperatura"]
        }

###   FUNÇÕES    

def input_composicao(composicao) -> list:
    # cria uma lista com as composiçoes
    a = list(composicao.values())
    subs = []
    cont = 0
    for i in a:
        if i == 0:
            cont += 1
        else:
            subs.append(elementos[cont])
            cont +=1
    return subs

def input_fracao(composicao) -> list:
    #cria uma lista com as fraçoes molares
    a = list(composicao.values())
    fracao = []
    cont = 0
    for i in a:
        if i == 0:
            cont += 1
        else:
            fracao.append(i)
            cont += 1
    return fracao

def lista_pressoes(p_inicial, p_final, passo) -> list:
    #cria uma lista com as pressoes de acordo com o passo escolhido
    pressoes = []
    pressoes.insert(0, p_inicial)
    a = int((p_final - p_inicial) / passo + 1)
    b = 1
    c = passo

    for i in pressoes:
        if len(pressoes) < a:
            pressoes.insert(b, c + p_inicial)
            pressoes[b] = round(pressoes[b],3)
            b += 1
            c += passo
    return pressoes

def conversao_atm (p_list) -> list:
    '''
    converte a pressao de atm para kpa

    :param p_list: lista com as pressoes em atm
    :type p_list: list
    :return:
    :rtype: list
    '''
    p_kpa = [i * 101.3 for i in p_list]
    return p_kpa

def matriz_kij (velementos,vsubs) -> list:
    '''
    Cria uma matriz com os Kij que serao utilizados no calculo
    :param velementos: lista com todos os elementos disponíveis
    :param vsubs: lista com os elementos utilizados
    :return:
    '''
    # criando matriz kij atual
    cont2 = []  # armazena os indices dos elementos da lista 'elementos' contidas na lista 'subs'
    k_ij = []  # matriz com os kij que estao na lista subs
    vet1 = []  # vai guardar os kij que estao na lista subs

    for i in range(len(vsubs)):
        k_ij.append([0] * len(vsubs))  # criando matriz com 0

    for i in range(len(velementos)):
        if velementos[i] in vsubs:
            cont2.append(i)

    for i in cont2:
        for j in cont2:
            vet1.append(kij[i][j])  # aqui foi criado o vetor unidimensional com os kij

    cont3 = 0
    for i in range(len(vsubs)):
        for j in range(len(vsubs)):
            k_ij[i][j] = vet1[cont3]  # aqui foi criada a matriz com o kij
            cont3 += 1
    return k_ij

def Subs2 (velementos,vsubs) -> list:
    '''
    cria nova lista de substancias a partir de 'subs'  de modo que fique na mesma ordem que a lista 'elementos', para facilitar no cálculo do aij

    :param velementos:
    :param vsubs:
    :return:
    '''
    subs2 = []
    for i in range(len(velementos)):
        if velementos[i] in vsubs:
            for j in range(len(vsubs)):
                if velementos[i] == vsubs[j]:
                    subs2.append(vsubs[j])
    return subs2

def fracao_molar_substancias (velementos, vsubs, vfracao_molar) -> list:
    '''
    cria nova lista de fraçao molar a partir de 'fracao molar e subs'  de modo que fique na mesma ordem que a lista 'elementos', para facilitar no cálculo do aij

    :param velementos: lista com todos os elementos disponiveis
    :param vsubs: lista com os elementos escolhidos
    :param vfracao_molar:fraçao molar dos elementos escolhidos
    :return: lista com fraçao molar na ordem correta para os calculos
    '''
    x = []
    for i in range(len(velementos)):
        if velementos[i] in vsubs:
            for j in range(len(vsubs)):
                if velementos[i] == vsubs[j]:
                    x.append(vfracao_molar[j])
    return x

def prop_criticas(subs2) -> list:
    '''
    cria listas para as propriedade criticas de cada elemento da mistura na ordem de elementos
    :return:
    '''
    massa, Pc,Tc,w  = [], [], [], []
    for i in range(len(subs2)):
        massa.append(subs2[i][0])
        Pc.append(subs2[i][1])
        Tc.append(subs2[i][2])
        w.append(subs2[i][3])
    return massa, Pc, Tc, w

def cont_massa_molar_mistura(vmassa, subs, x) -> list:
    '''
    contribuicao da massa molar de cada fluido
    :param vmassa: lista com massa molar de cada componente da mistura
    :return:
    '''
    contrib_molar_mistura = []
    for i in range(len(subs)):
        contrib_molar_mistura.append(x[i] * vmassa[i])
    return contrib_molar_mistura

def calculo_bi_PREOS(vsubs2, x) -> list:
    '''
    calucula os parametros bi da eq de Peng Robison
    :param vsubs2: lista com os elementos utilizados
    :return:
    '''
    r = 8.31447  # cte dos gases
    bi = []
    for i in range(len(vsubs2)):
        bi.append(0.0778 * r * vsubs2[i][2] / vsubs2[i][1])
        bi[i] = x[i] * bi[i]
    return bi

def calculo_ki_PREOS(vsubs2) -> list:
    '''
    calucula os parametros ki da eq de Peng Robison
    :param vsubs2: lista com os elementos utilizados
    :return:
    '''
    r = 8.31447  # cte dos gases
    ki = []
    for i in range(len(vsubs2)):
        ki.append(-0.26992 * (vsubs2[i][3]) ** 2 + 1.54226 * vsubs2[i][3] + 0.37464)
    return ki

def eq_cubica(b, c, d) -> list:
    '''
    resolve uma eq cubica retornando uma lista de raizes reais

    :param b: parametro b da eq cubica do tipo ax³ + bx² + cx + d = 0
    :type b:  float
    :param c: parametro c da eq cubica do tipo ax³ + bx² + cx + d = 0
    :type c: float
    :param d: parametro d da eq cubica do tipo ax³ + bx² + cx + d = 0
    :type d: float
    :return: retorna as raizes reais
    :rtype: list
    '''
    z = Symbol('z')
    Z = list(solveset(z ** 3 + b * (z ** 2) + c * z + d, z, domain=S.Reals))
    for i in range(len(Z)):
        Z[i] = float(Z[i])
    return Z

def Ai (vsubs2,vki,vt,r) -> list:
    '''
    calcula o termo ai de cada componente
    :param vsubs2: lista com substancias
    :param vki: termo ki dos elementos
    :param vt: temperatura em kelvin
    :return:
    '''
    ai = []
    for i in range(len(vsubs2)):
        ai.append((0.457235529 * (r * vsubs2[i][2]) ** 2) / vsubs2[i][1] * (1 + vki[i] * (1 - (vt / vsubs2[i][2]) ** 0.5)) ** 2)
    return ai

def calculo_aij(vk_ij,vai,subs) -> list:
    '''
    calcula o termo 'aij' da eq de Peng Robison, atraves da multiplicaçao dos termos das matrizes aij e kij
    :param vk_ij: matriz kij ja ajustada para os componentes utilizados
    :param vai: matriz 'ai'
    :return: matriz aij
    '''
    # criando matriz aij e a
    a_vet = []
    aij = [] #cria-se uma matriz aij com 0
    for i in range(len(subs)):
        aij.append([0] * len(subs))
        a_vet.append([0] * len(subs))

    #calculo do aij
    for i in range(len(subs)):
        for j in range(len(subs)):
            aij[i][j] = (1 - vk_ij[i][j]) * (vai[i] * vai[j]) ** 0.5

    return aij

def calculo_a (vsubs2,vx,vaij) -> float:
    # criando matriz aij e a
    a_vet = []
    for i in range(len(vsubs2)):
        a_vet.append([0] * len(vsubs2))

    a_lista = []  # lista que vai conter todos os elementos da matriz aij abaixo, para poder soma-lo e obter o a
    for i in range(len(vsubs2)):
        for j in range(len(vsubs2)):
            a_vet[i][j] = vx[i] * vx[j] * vaij[i][j]
            a_lista.append(a_vet[i][j])
    return sum(a_lista)

def stable_root(Zlist, pressure, A, B) -> float:
    '''
    define a raiz Z estavel a partir do calculo de fugacidade

    :param Zlist: lista com os valores de Z
    :type Zlist: list
    :param pressure: valor da pressao
    :type pressure: float
    :param A: parametro A da equaçao cubica de PR
    :type A: float
    :param B: parametro B da equaçao cubica de PR
    :type B: float
    :rtype: float
    '''
    fug = []
    for i in Zlist:
        fug.append(pressure * functions.exp(
            i - 1 - functions.log(i - B) - A / B / 2.8284 * functions.log((i + 2.4142 * B) / (i - 0.4142 * B))))
        menor = fug.index(min(fug))
        return Zlist[menor]

def massa_especifica_geral(b1, c1, d1, massa_molar_total, p, r, t) -> list:
    '''
    calcula a massa especfica para todos os resultados reais de Z
    :rtype: list
    '''
    Zvar = eq_cubica(b1, c1, d1)
    m = []
    for i in Zvar:
        m.append(massa_molar_total * p / (r * t * Zvar[0]))
        return m

def massa_especifica_estavel(r_estavel, press, r, t, massa_molar_total) -> float:
    '''
    calcula a massa especifica estavel a partir da raiz Z estavel
    :param r_estavel: raiz estavel
    :type r_estavel: float
    :param press: pressao tipo
    :type press: float
    :return: retorna massa especifica da raiz estavel
    :rtype: float
    '''
    m = massa_molar_total * press / (r * t * r_estavel)
    return m

def massa_especifica_isoterma(p_inicial, p_final, passo, a, r, t, b, massa_molar_total) -> list:
    '''
    calcula as massas especificas de acordo com a isoterma definida
    :return:
    '''
    pr_atm = lista_pressoes(p_inicial, p_final, passo)
    pr_kpa = conversao_atm(pr_atm)
    final = []
    for i in pr_kpa:
        A = (a * i) / pow(r, 2) / pow(t, 2)
        B = (b * i) / (r * t)
        b2 = -(1 - B)
        c2 = A - 3 * pow(B, 2) - 2 * B
        d2 = -(A * B - pow(B, 2) - pow(B, 3))
        a1 = eq_cubica(b2, c2, d2)
        a2 = stable_root(a1, i, A, B)
        a3 = massa_especifica_estavel(a2, i, r, t, massa_molar_total)
        valor = round(a3,3)
        final.append(valor)
    return final

def plot_isoterma(listaPressoes, listaMassaEspIsoterma, t, codigo_idioma) -> None:
    plt.plot(listaPressoes, listaMassaEspIsoterma)
    plt.title(STRINGS["title"][codigo_idioma] + ' %i K' % (t))
    plt.xlabel(STRINGS["label_x"][codigo_idioma] + ' (ATM)')
    plt.ylabel(STRINGS["label_y"][codigo_idioma] + ' (kg/m³)')
    plt.show()

def tabela_massa_especifica(pressoes, me) -> list:
    '''
    cria uma tabela com as massas especificas da isoterma deifinida
    :return:
    '''
    a = []
    a.append([0] * 2)
    for i in pressoes:
        a.append([0] * 2 )
    cont = 0
    cont1 = 1
    a[0][0]= 'ATM'
    a[0][1]= 'Kg/m³'
    for b in range(len(a)-1):
        for k in range(0,1):
            a[cont1][0] = pressoes[cont]
            a[cont1][1] = me[cont]
        cont += 1
        cont1 += 1
    '''for i in range(len(a)):
        for j in range(2):
            print(f'[{a[i][j]:^7}]', end='')
        print()'''
    return a

def salvar_txt(m_esp) -> None:
    '''
    cria um arquivo txt com as massas espeficas calculadas
    :param m_esp: lista em forma de tabela com as massas especificas
    :return:
    '''
    a = m_esp
    b = datetime.now().strftime('%Y_%m_%d-%H_%M_%S')

    for i in range(len(a)):
        for j in range(2):
            a[i][j] = str(a[i][j])

    fileobj = open("massa_esp %s.txt" %b, "w")
    for i in range(len(a)):
            fileobj.write(a[i][0] + ',' + a[i][1] + '\n')

    fileobj.close()

def obter_nome_padrao(codigo) -> str:
    '''
    Cria um nome padrão para o arquivo que será salvo
    :param : 
    :return nomePadraoArquivo: nome do arquivo
    '''

    data = datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    nomePadraoArquivo =  STRINGS["label_y"][codigo]+"-"+data+".csv"

    return nomePadraoArquivo

def to_tabela_composicao(composicao) -> list:
    '''
    Transforma o dicionário composição em uma tabela com a composição utilizada no cálculo
    :param composicao: lista em forma de tabela com as massas especificas e valores de pressao
    :return: tabela em forma de matriz com as composições
    '''

    elementos = list(composicao.keys())
    valores = list(composicao.values())
    tabelaComposicao = []

    for i in range(len(elementos)):
        if valores[i] != 0:
            tabelaComposicao.append([elementos[i], valores[i]])

    return tabelaComposicao

def salvar_csv(m_esp, temperatura, composicao, nomeArquivo, codigo) -> None:
    '''
    cria um arquivo de extensão .csv com as massas especificas calculadas
    :param m_esp: lista em forma de tabela com as massas especificas e valores de pressao
    :param nomeArquivo: nome do arquivo .csv
    :return:
    '''

    #transformando valores em string
    temperatura = str(temperatura)
    for i in range(len(composicao)):
        for j in range(2):
            composicao[i][j] = str(composicao[i][j])
    for i in range(len(m_esp)):
        for j in range(2):
            m_esp[i][j] = str(m_esp[i][j])

    #gravando valores no arquivo
    fileobj = open(nomeArquivo, "w")
    fileobj.write(STRINGS["composicao"][codigo]+"\n"+STRINGS["substancia"][codigo]+";"+STRINGS["fracao_molar"][codigo]+"\n")
    for i in range(len(composicao)):
        # coletar string correta de acordo com idioma
        subs = SUBSTANCIAS.index(composicao[i][0])
        if codigo == 1:
            subs = SUBSTANCES[subs]
        else:
            subs = SUSTANCIAS[subs]

        fileobj.write(subs + ";" + composicao[i][j] + "\n")

    fileobj.write("\n"+STRINGS["temperatura"][codigo]+"\n"+ temperatura + "\n\n"+STRINGS["label_y"][codigo]+"\n")

    for i in range(len(m_esp)):
        fileobj.write(m_esp[i][0] + ';' + m_esp[i][1] + '\n')

    fileobj.close()

def formatar_dados_arquivo(dados) -> list:
    '''
    Transforma strings lidas do arquivo em uma matriz de números
    :param : 
    :return [pressoes, m_esp]: 
    '''

    for i in range(len(dados)):
        dados[i] = dados[i].split(";")

    pressoes = []
    m_esp = []
    for i in range(1,len(dados)):
        pressoes.append(float(dados[i][0]))
        m_esp.append(float(dados[i][1]))

    return [pressoes, m_esp]

def ler_arquivo(nomeArquivo, codigo) -> list:
    '''
    Lê dados do arquivo
    :param : 
    :return data: dados do arquivo
    '''
    data = []
    with open(nomeArquivo, 'r') as file:
        line = file.readline()

        while line != STRINGS["temperatura"][codigo]+"\n" and line != "":
            line = file.readline()
    
        temperatura = file.readline().strip()

        while line != STRINGS["label_y"][codigo]+"\n" and line != "":
            line = file.readline()
            
        for line in file:
            data.append(line.strip())
        file.close()

    return temperatura, data

def converter_temperatura_kelvin(unidade, valor) -> float:
    '''
    Converte a temperatura fornecida em celsius ou fahrenheit para kelvin

    :param unidade: indica a unidade da temperatura
    :param valor: indica o valor da temperatura na unidade referida
    :return valor: valor da temperatura em kelvin
    '''

    #
    # Constantes utilizadas na conversão baseadas nos valores do NIST - National Institute of Standards and Technology
    #

    if unidade == ESCALAS_DE_TEMPERATURA[0]: #CELSIUS
        valor = valor + 273.15 
    elif unidade == ESCALAS_DE_TEMPERATURA[1]: #FAHRENHEIT
        celsius = (valor - 32)/1.8
        valor = celsius + 273.15
    return valor

def verificar_soma_fracao_molar(matrizComposicao) -> bool:
    '''
    Verifica se a soma das frações molares é diferente de 1.0

    :param matrizComposicao: matriz que contém nome e valor de cada substancia da composicao
    matrizComposicao[[nomeDaSubstancia, valorDaSubstancia],...]
    :return: true, se somatório é diferente de 1.0. false, caso contrário
    '''
    somaDaFracaoMolar = 0
    for substancia in matrizComposicao:
        somaDaFracaoMolar += substancia[1]
    
    if somaDaFracaoMolar != 1:
        return True
    
    return False

def formatar_input_composicao(matrizComposicao) -> list:
    '''
    Formata input da composicao da mistura para que fique na ordem utilizada pelo programa
    :param matrizComposicao: 
    :return composicaoFormatada: 
    '''

    composicaoFormatada = {}
    for substancia in SUBSTANCIAS:
        fracaoMolar = 0
        for i in range(len(matrizComposicao)):
            if matrizComposicao[i][0] == substancia:
                fracaoMolar = matrizComposicao[i][1]
                break
        
        composicaoFormatada[substancia] = fracaoMolar

    return composicaoFormatada

def calcular_pressao_unica(composicao, temperatura, pressao) -> float:
    '''
    Realiza o cálculo da massa específica quando é fornecido um valor de pressao
    :param composicao:
    :param temperatura:
    :param pressao: 
    :return es: massa específica
    '''

    subs = input_composicao(composicao)
    fracao_molar = input_fracao(composicao)  # fracao molar
    t = temperatura  # Temperatura em Kelvin
    pr = pressao  # Pressão em atm

    if not pr == 0:
        p = 101.3 * pr
    else: p = 0.00000001

    k_ij = matriz_kij(elementos, subs)      #criada matriz kij somente com os elementos utilizados

    subs2 = Subs2(elementos, subs)          #criada lista com os componentes da mistura na ordem correta

    x = fracao_molar_substancias(elementos, subs,
                                fracao_molar)  #criada lista com a fraçao molar de cada componente e na ordem correta

    massa, Pc, Tc, w = prop_criticas(subs)      #listas que contem a massa molar dos componentes e as propriedades criticas dos fluidos e fator acentrico

    contrib_molar_mistura = cont_massa_molar_mistura(massa, subs, x)     #criada lista com a contribuiçao molar de cada fluido
    massa_molar_total = sum(contrib_molar_mistura)              #massa molar total da mistura

    r = 8.31447  # cte dos gases

    # cálculo bi e ki
    bi = calculo_bi_PREOS(subs2, x)
    ki = calculo_ki_PREOS(subs2)
    ai = Ai(subs2, ki, t, r)     #lista com os termos ai
    b = sum(bi)                  #soma os ' bi ' para obter o b total

    aij = calculo_aij(k_ij, ai, subs)    #lista com os todos os termos aij calculados
    a = calculo_a(subs2,x,aij)           #soma de todos os termos aij

    #termos da equaçao cubica
    A = (a * p) / pow(r, 2) / pow(t, 2)
    B = (b * p) / (r * t)
    b1 = -(1 - B)
    c1 = A - 3 * pow(B, 2) - 2 * B
    d1 = -(A * B - pow(B, 2) - pow(B, 3))

    m = eq_cubica(b1,c1,d1)
    s = stable_root(m,p,A,B)
    es = massa_especifica_estavel(s,p,r,t,massa_molar_total)
    #print('%.1f atm =' %pr, '%.3f kg/m³' %es)

    es = round(es, 5)

    return es
    
def calcular_pressao_intervalo(composicao, temperatura, pressao_inicial, pressao_final, passo) -> list:
    '''
    Realiza o cálculo da massa específica quando é fornecido um intervalo de valores de pressao
    :param composicao:
    :param temperatura:
    :param pressao_inicial: 
    :param pressao_final: 
    :param passo: 
    :return pressoes, mEspIsoterma: lista das pressoes e massas específicas
    '''

    subs = input_composicao(composicao)
    fracao_molar = input_fracao(composicao)  # fracao molar
    t = temperatura  # Temperatura em Kelvin

    if pressao_inicial == 0:
        p_inicial = 0.00000001
    else:
        p_inicial = pressao_inicial
    p_final = pressao_final

    k_ij = matriz_kij(elementos, subs)      #criada matriz kij somente com os elementos utilizados

    subs2 = Subs2(elementos, subs)          #criada lista com os componentes da mistura na ordem correta

    x = fracao_molar_substancias(elementos, subs,
                                fracao_molar)  #criada lista com a fraçao molar de cada componente e na ordem correta

    massa, Pc, Tc, w = prop_criticas(subs)      #listas que contem a massa molar dos componentes e as propriedades criticas dos fluidos e fator acentrico

    contrib_molar_mistura = cont_massa_molar_mistura(massa, subs, x)     #criada lista com a contribuiçao molar de cada fluido
    massa_molar_total = sum(contrib_molar_mistura)              #massa molar total da mistura

    r = 8.31447  # cte dos gases

    # cálculo bi e ki
    bi = calculo_bi_PREOS(subs2, x)
    ki = calculo_ki_PREOS(subs2)
    ai = Ai(subs2, ki, t, r)     #lista com os termos ai
    b = sum(bi)                  #soma os ' bi ' para obter o b total

    aij = calculo_aij(k_ij, ai, subs)    #lista com os todos os termos aij calculados
    a = calculo_a(subs2,x,aij)           #soma de todos os termos aij

    pressoes = lista_pressoes(p_inicial, p_final, passo)
    mEspIsoterma = massa_especifica_isoterma(p_inicial, p_final, passo, a, r, t, b, massa_molar_total)
    
    #me = tabela_massa_especifica(pressoes, mEspIsoterma)

    return pressoes, mEspIsoterma



###   Funções ainda não utilizadas - em desenvolvimento
def fugacidade_liquida (subs2, x, t, r, p):
    bi = calculo_bi_PREOS(subs2, x)
    ki = calculo_ki_PREOS(subs2)
    b = sum(bi)  # soma os ' bi ' para obter o b total
    ai = Ai(subs2, ki, t, r)  # lista com os termos ai
    aij = calculo_aij(k_ij, ai)  # lista com os todos os termos aij calculados
    a = calculo_a(subs2,x,aij)
    A = (a * p) / pow(r, 2) / pow(t, 2)
    B = (b * p) / (r * t)
    b1 = -(1 - B)
    c1 = A - 3 * pow(B, 2) - 2 * B
    d1 = -(A * B - pow(B, 2) - pow(B, 3))
    z = eq_cubica(b1, c1, d1)
    zliq = min(z)

    lnphi = []

    for i in range(len(subs2)):
        somatorio_list = []
        for j in range(len(subs2)):
            som = x[j]*aij[i][j]
            somatorio_list.append(som)
        somatorio = sum(somatorio_list)

        lni = (bi[i]/b)*(zliq-1) - functions.log(zliq - B) - (A/(2*sqrt(2))) * ((2*somatorio/A) - bi[i]/b) * functions.log( (zliq + (1+sqrt(2)*B)) / (zliq +(1-sqrt(2)*B) ) )
        lnphi.append(lni)
        print(exp(lnphi[i]))
    return

def bubble_p(subs2,frac,p,t):
    '''
    Calcula a pressao do ponto de bolha

    :param subs2: lista com as propriedades criticas das substancias
    :type subs2: list
    :param frac: lista com as fraçoes molares
    :type frac: list
    :return:
    '''
    P = []
    ki_bubble = []
    for i in range(len(subs2)):
        Pisat = frac[i]*(functions.exp( functions.log(subs2[i][1]) + functions.log(10)*(1-subs2[i][2]/t)*(7+7*subs2[i][3])/3))
        P.append(Pisat)
        ki_b = functions.exp(functions.log(subs2[i][1]/p) + functions.log(10)*(7/3)*(1+subs2[i][3])*(1-subs2[i][2]/t))
        ki_bubble.append(ki_b)

        #Ki = exp[ln(Pc / P) + ln(10)(7 / 3)(1 + ω)(1 - Tc / T)]
        # Yi = Ki*Xi
        #[Massa molar(g / mol), Pressão crítica(KPa), Temperatura crítica(K), Fator acênctrico]
    return P, ki_bubble
