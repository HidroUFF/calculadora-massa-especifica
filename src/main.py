###################################################      ME-PREOS       #################################################

'''

Este programa tem como funcionalidade principal o cálculo da massa especifica de misturas gasosas,
através da resolução da equação de estado cúbica de Peng Robinson.


Desenvolvido por Mateus Pereira de Sousa e Valesca Moura de Sousa
Data de criação: 18/08/2020
Última revisão: 14/09/2021

'''

###################################################      REQUISITOS PARA O CÓDIGO       #################################################

'''

É necessário ter instalado:
Python 3.x
Bibliotecas: sympy, matplotlib e PyQt5

'''

###################################################      COMO INSTALAR OS REQUISITOS     #################################################

'''

Para instalar o Python acesse: https://www.python.org/downloads/

Para instalar as bibliotecas/pacotes via PIP:
    - Sympy: digite no CMD 'pip install sympy'

    - Matplotlib: digite no CMD 'pip install matplotlib'

    - PyQt5: digite no CMD 'pip install PyQt5'

Como instalar o PIP no Windows: https://www.youtube.com/watch?v=qrhwMJ-_cTs

'''

###################################################      ORIENTAÇÕES GERAIS     #########################################################

'''
1 - Certifique-se de que os requisitos foram instalados corretamente
2 - Não altere nenhuma palavra previamente escrita no código, mesmo que contenha erros ortográficos
3 - Qualquer sugestão ou dúvida no código, comunique o desenvolvedor ou responsável
4 - Sempre inicie a execução do programa através do arquivo 'main.py'

'''

###################################################     EXEMPLO DA ENTRADA DE DADOS DO PROGRAMA    ############################################################

''' COMPOSIÇAO DA MISTURA '''

#1.0 INFORME A FRAÇAO MOLAR DA MISTURA DESEJADA
#USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL
# O SOMATORIO DAS FRAÇOES MOLARES DEVE SER IGUAL A 1.0

'''  Exemplo:

composicao = {
    'METANO':  0.3,
    'ETANO':   0.3,
    'CO2':     0.1,
    'N2':      0.1,
    'PROPANO': 0.1,
    'NBUTANO': 0.1,
    'H2S':     0.0
}

'''

#1.1 INFORME A TEMPERATURA EM KELVIN
#USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL / EX: TEMPERATURA = 275.50

''' Exemplo:

TEMPERATURA = 287.15

'''

#1.2 OBTER A MASSA ESPECIFICA PARA MAIS DE UMA PRESSAO ? (0 = NAO / 1 = SIM) EX:OP1 = 0
#SE SIM, VÁ PARA #1.3 / SE NAO, VÁ PARA #1.4

''' Exemplo:

OP1 = 1

'''

#1.3 INFORME A PRESSAO INICIAL, A PRESSAO FINAL E O PASSO ENTRE ELAS. EX: PRESSAO_INICIAL = 1.5, PRESSAO_FINAL = 100.8 , PASSO = 4
#INFORME A PRESSAO EM ATM / #USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL

''' Exemplo:

PRESSAO_INICIAL = 0
PRESSAO_FINAL = 200
PASSO = 5

'''

#1.3.1 EXIBIR GRAFICO DA ISOTERMA ? (0 = NAO / 1 = SIM) EX:OP2 = 0

''' Exemplo:

OP2 = 1

'''

#1.3.2 SALVAR O RESULTADO EM NUM ARQUIVO .txt ? (0 = NAO / 1 = SIM) EX:OP3 = 0

''' Exemplo:

OP3 = 1

'''

#1.4 INFORME A PRESSAO EM ATM
#USAR PONTO FINAL " . " COMO SEPARADOR DECIMAL

''' Exemplo:

PRESSAO = 200

'''

from PyQt5 import QtCore, QtGui, QtWidgets
import gui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    MainWindow.setWindowIcon(icon)
    MainWindow.setIconSize(QtCore.QSize(16, 16))
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
