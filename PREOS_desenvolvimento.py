###################################################      ME-PREOS       #################################################


'''

Este programa tem como funcionalidade principal o calculo da massa especifica de misturas gasosas ,
atraves da resoluçao da equaçao de estado cubica de Peng Robinson.


Desenvolvido por Mateus Pereira de Sousa
Data de criação: 18/08/2020
Última revisão: 01/10/2020

'''

###################################################      REQUISITOS PARA O CÓDIGO       #################################################
'''

É necessário ter instalado:
Python 3.x
Bibliotecas: sympy e matplotlib

'''

###################################################      COMO INSTALAR OS REQUISITOS     #################################################
'''

Para instalar o Python acesse: https://www.python.org/downloads/

Para instalar as bibliotecas/pacotes via PIP:
    - Sympy: digite no CMD: pip install sympy

    -  Matplotlib: digite no CMD: pip install matplotlib

Como instalar o PIP no Windows: https://www.youtube.com/watch?v=qrhwMJ-_cTs

'''

###################################################      ORIENTAÇÕES GERAIS     #########################################################
'''
1 - Confira se os requisitos foram instalados corretamente
2 - Preencha somente os dados referentes à "ENTRADA DE DADOS" e execute o código
3 - Não altere nenhuma palavra previamente escrita no código, mesmo que contenha erros ortográficos
4 - Qualquer sugestão ou dúvida no código, comunique o desenvolvedor ou responsável

'''

###################################################      ENTRADA DE DADOS     ############################################################

''' COMPOSIÇAO DA MISTURA '''

#1.0 DIGITE A FRAÇAO MOLAR DA MISTURA DESEJADA
#USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL
# O SOMATORIO DAS FRAÇOES MOLARES DEVE SER IGUAL A 1.0

composicao = {

     'METANO':  0.3
    ,'ETANO':   0.3
    ,'CO2':     0.1
    ,'N2':      0.0
    ,'PROPANO': 0.1
    ,'NBUTANO': 0.0
    ,'H2S':     0.0

    }
#1.1 DIGITE A TEMPERATURA EM KELVIN
#USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL / EX: TEMPERATURA = 275.50

TEMPERATURA = 287.15

#1.2 OBTER A MASSA ESPECIFICA PARA MAIS DE UMA PRESSAO ? (0 = NAO / 1 = SIM) EX:OP1 = 0
OP1 = 1  #SE SIM, VÁ PARA #1.3 / SE NAO, VÁ PARA #1.4

#1.3 DIGITE A PRESSAO INICIAL, A PRESSAO FINAL E O PASSO ENTRE ELAS. EX: PRESSAO_INICIAL = 1.5, PRESSAO_FINAL = 100.8 , PASSO = 4
#DIGITE A PRESSAO EM ATM / #USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL

PRESSAO_INICIAL = 0
PRESSAO_FINAL = 200
PASSO = 5

#1.3.1 EXIBIR GRAFICO DA ISOTERMA ? (0 = NAO / 1 = SIM) EX:OP2 = 0
OP2 = 1

#1.3.2 SALVAR O RESULTADO EM NUM ARQUIVO .txt ? (0 = NAO / 1 = SIM) EX:OP3 = 0
OP3 = 1

#1.4 DIGITE A PRESSAO EM ATM
#USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL
PRESSAO = 200


###################################################      PROGRAMA     #################################################


from sympy import solveset, S, Symbol, functions
import matplotlib.pyplot as plt
from datetime import datetime
from math import sqrt, exp

def Input_Composicao():
    #cria uma lista com as composiçoes
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

def Input_Fracao():
    #cira uma lista com as fraçoes molares
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

def Lista_Pressoes():
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

def Conversao_atm (p_list):
    '''
    converte a pressao de atm para kpa

    :param p_list: lista com as pressoes em atm
    :type p_list: list
    :return:
    :rtype: list
    '''
    p_kpa = [i * 101.3 for i in p_list]
    return p_kpa

def Matriz_Kij (velementos,vsubs):
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
    for i in range(len(subs)):
        for j in range(len(subs)):
            k_ij[i][j] = vet1[cont3]  # aqui foi criada a matriz com o kij
            cont3 += 1
    return k_ij

def Subs2 (velementos,vsubs):
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

def Fracao_Molar_Substancias (velementos, vsubs,vfracao_molar):
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

def Prop_Criticas():
    '''
    cria listas para as propriedade criticas de cada elemento da mistura na ordem de elementos
    :return:
    '''
    massa, Pc,Tc,w  = [], [], [], []
    for i in range(len(subs)):
        massa.append(subs2[i][0])
        Pc.append(subs2[i][1])
        Tc.append(subs2[i][2])
        w.append(subs2[i][3])
    return massa, Pc, Tc, w

def Cont_Massa_Molar_Mistura(vmassa):
    '''
    contribuicao da massa molar de cada fluido
    :param vmassa: lista com massa molar de cada componente da mistura
    :return:
    '''
    contrib_molar_mistura = []
    for i in range(len(subs)):
        contrib_molar_mistura.append(x[i] * vmassa[i])
    return contrib_molar_mistura

def Calculo_bi_PREOS(vsubs2):
    '''
    calucula os parametros bi da eq de Peng Robison
    :param vsubs2: lista com os elementos utilizados
    :return:
    '''
    r = 8.31447  # cte dos gases
    bi = []
    for i in range(len(subs)):
        bi.append(0.0778 * r * vsubs2[i][2] / vsubs2[i][1])
        bi[i] = x[i] * bi[i]
    return bi

def Calculo_ki_PREOS(vsubs2):
    '''
    calucula os parametros ki da eq de Peng Robison
    :param vsubs2: lista com os elementos utilizados
    :return:
    '''
    r = 8.31447  # cte dos gases
    ki = []
    for i in range(len(subs)):
        ki.append(-0.26992 * (vsubs2[i][3]) ** 2 + 1.54226 * vsubs2[i][3] + 0.37464)
    return ki

def Eq_Cubica(b, c, d):
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

def Ai (vsubs2,vki,vt):
    '''
    calcula o termo ai de cada componente
    :param vsubs2: lista com substancias
    :param vki: termo ki dos elementos
    :param vt: temperatura em kelvin
    :return:
    '''
    ai = []
    for i in range(len(subs)):
        ai.append((0.457235529 * (r * vsubs2[i][2]) ** 2) / vsubs2[i][1] * (1 + vki[i] * (1 - (vt / vsubs2[i][2]) ** 0.5)) ** 2)
    return ai

def Calculo_Aij(vk_ij,vai):
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

def Calculo_a (vsubs2,vx,vaij):
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

def Stable_Root(Zlist, pressure, A, B):
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

def Massa_Especifica_Geral():
    '''
    calcula a massa especfica para todos os resultados reais de Z
    :rtype: list
    '''
    Zvar = Eq_Cubica(b1, c1, d1)
    m = []
    for i in Zvar:
        m.append(massa_molar_total * p / (r * t * Zvar[0]))
        return m

def Massa_Especifica_Estavel(r_estavel, press):
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

def Massa_Especifica_Isoterma():
    '''
    cacula as massas especificas de acordo com a isoterma definida
    :return:
    '''
    pr_atm = Lista_Pressoes()
    pr_kpa = Conversao_atm(pr_atm)
    final = []
    for i in pr_kpa:
        A = (a * i) / pow(r, 2) / pow(t, 2)
        B = (b * i) / (r * t)
        b2 = -(1 - B)
        c2 = A - 3 * pow(B, 2) - 2 * B
        d2 = -(A * B - pow(B, 2) - pow(B, 3))
        a1 = Eq_Cubica(b2, c2, d2)
        a2 = Stable_Root(a1, i, A, B)
        a3 = Massa_Especifica_Estavel(a2, i)
        valor = round(a3,3)
        final.append(valor)
    return final

def Plot_Isoterma():
    plt.plot(Lista_Pressoes(), Massa_Especifica_Isoterma())
    plt.title('Massa Específica a %i K' % (t))
    plt.xlabel('Pressão (atm)')
    plt.ylabel('Massa específica (kg/m³)')
    plt.show()

def Tabela_Massa_Especifica():
    '''
    cria uma tabela com as massas especificas da isoterma deifinida
    :return:
    '''
    a = []
    pressoes = Lista_Pressoes()
    me = Massa_Especifica_Isoterma()
    a.append([0] * 2)
    for i in pressoes:
        a.append([0] * 2 )
    cont = 0
    cont1 = 1
    a[0][0]= 'atm'
    a[0][1]= 'kg/m³'
    for b in range(len(a)-1):
        for k in range(0,1):
            a[cont1][0] = pressoes[cont]
            a[cont1][1] = me[cont]
        cont += 1
        cont1 += 1
    for i in range(len(a)):
        for j in range(2):
            print(f'[{a[i][j]:^7}]', end='')
        print()
    return a

def Salvar_txt(m_esp):
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


# TABELA Kij
kij = [
    [0, 0.00224, 0.1, 0.036, 0.00683, 0.0123, 0.085, ],
    [0.00224, 0, 0.1298, 0.050, 0.00126, 0.0041, 0.084, ],
    [0.1, 0.1298, 0, -0.02, 0.135, 0.1298, 0.1, ],
    [0.036, 0.05, -0.02, 0, 0.08, 0.09, 0.1676, ],
    [0.00683, 0.00126, 0.135, 0.08, 0.00, 0.00082, 0.075, ],
    [0.01230, 0.004100, 0.12980, 0.090, 0.000820, 0.0, 0.06, ],
    [0.085, 0.084, 0.1, 0.1676, 0.075, 0.06, 0.0, ],

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

elementos = [metano, etano, co2, n2, propano, nbutano, h2s]

# INPUTS
subs = Input_Composicao()
fracao_molar = Input_Fracao()  # fracao molar
t = TEMPERATURA  # Temperatura em Kelvin
if OP1:
    if PRESSAO_INICIAL == 0:
        p_inicial = 0.00000001
    else:
        p_inicial = PRESSAO_INICIAL
    p_final = PRESSAO_FINAL
    passo = PASSO

pr = PRESSAO  # Pressão em atm

if not pr == 0:
    p = 101.3 * pr
else: p = 0.00000001


k_ij = Matriz_Kij(elementos, subs)      #criada matriz kij somente com os elementos utilizados

subs2 = Subs2(elementos, subs)          #criada lista com os componentes da mistura na ordem correta

x = Fracao_Molar_Substancias(elementos, subs,
                             fracao_molar)  #criada lista com a fraçao molar de cada componente e na ordem correta

massa, Pc, Tc, w = Prop_Criticas()      #listas que contem a massa molar dos componentes e as propriedades criticas dos fluidos e fator acentrico

contrib_molar_mistura = Cont_Massa_Molar_Mistura(massa)     #criada lista com a contribuiçao molar de cada fluido
massa_molar_total = sum(contrib_molar_mistura)              #massa molar total da mistura

r = 8.31447  # cte dos gases


# cálculo bi e ki
bi = Calculo_bi_PREOS(subs2)
ki = Calculo_ki_PREOS(subs2)
ai = Ai(subs2, ki, t)     #lista com os termos ai
b = sum(bi)               #soma os ' bi ' para obter o b total


aij = Calculo_Aij(k_ij, ai)    #lista com os todos os termos aij calculados
a = Calculo_a(subs2,x,aij)                      #soma de todos os termos aij

#termos da equaçao cubica
A = (a * p) / pow(r, 2) / pow(t, 2)
B = (b * p) / (r * t)
b1 = -(1 - B)
c1 = A - 3 * pow(B, 2) - 2 * B
d1 = -(A * B - pow(B, 2) - pow(B, 3))

if OP1:
    me = Tabela_Massa_Especifica()
    if OP3:
        sv = Salvar_txt(me)
else:
    m = Eq_Cubica(b1,c1,d1)
    s = Stable_Root(m,p,A,B)
    es = Massa_Especifica_Estavel(s,p)
    print('%.1f atm =' %pr, '%.3f kg/m³' %es)
if OP2:
    iso = Plot_Isoterma()

def Fugacidade_Liquida ():
    bi = Calculo_bi_PREOS(subs2)
    ki = Calculo_ki_PREOS(subs2)
    b = sum(bi)  # soma os ' bi ' para obter o b total
    ai = Ai(subs2, ki, t)  # lista com os termos ai
    aij = Calculo_Aij(k_ij, ai)  # lista com os todos os termos aij calculados
    a = Calculo_a(subs2,x,aij)
    A = (a * p) / pow(r, 2) / pow(t, 2)
    B = (b * p) / (r * t)
    b1 = -(1 - B)
    c1 = A - 3 * pow(B, 2) - 2 * B
    d1 = -(A * B - pow(B, 2) - pow(B, 3))
    z = Eq_Cubica(b1, c1, d1)
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



def Bubble_P(subs2,frac):
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
    for i in range(len(subs)):
        Pisat = frac[i]*(functions.exp( functions.log(subs2[i][1]) + functions.log(10)*(1-subs2[i][2]/t)*(7+7*subs2[i][3])/3))
        P.append(Pisat)
        ki_b = functions.exp(functions.log(subs2[i][1]/p) + functions.log(10)*(7/3)*(1+subs2[i][3])*(1-subs2[i][2]/t))
        ki_bubble.append(ki_b)

        #Ki = exp[ln(Pc / P) + ln(10)(7 / 3)(1 + ω)(1 - Tc / T)]
        # Yi = Ki*Xi
        #[Massa molar(g / mol), Pressão crítica(KPa), Temperatura crítica(K), Fator acênctrico]
    return P, ki_bubble



