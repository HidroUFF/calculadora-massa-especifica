# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QRegExp
from PyQt5.QtGui import QFontDatabase, QRegExpValidator
from PyQt5.QtWidgets import QFileDialog
from platform import system
import calculadora
import verificacaoDeEntrada
import imagesAndFonts_rc


class Ui_MainWindow(object):

    SOMA_FRAME = 40 #altura dos frames adicionados a area de rolagem da composicao de mistura
    #matriz com os elementos dinamicos da interface refentes a composicao da mistura
    #cada linha corresponde a um vetor = [frame, comboBox, lineEdit, pushButton]
    matrizSubstancias = []
    indiceBotoes = 0 #indice dos botoes adicionados dinamicamente
    
    # Internacionalização
    # Strings utilizadas para nomear os labels do aplicativo na ordem: português (codigo==0), inglês (codigo==1) e espanhol (codigo==2).
    codigo = 0 # Default == 0 => português
    STRINGS = {
        "substancias": [calculadora.SUBSTANCIAS, calculadora.SUBSTANCES, calculadora.SUSTANCIAS],
        "title": ["Calculadora de Massa Específica HidroUFF", "HidroUFF Density Calculator", "Calculadora de Densidad HidroUFF"],
        "label_calcMassaEsp": ["Calculadora de Massa Específica", "Density Calculator", "Calculadora de Densidad"],
        "pushButton_grafico": ["Gerar gráfico a partir de arquivo CSV","Generate graph from CSV file","Generar gráfico a partir de archivo CSV"],
        "pushButton_ajuda": ["Ajuda", "Help", "Ayuda"],
        "pushButton_sobre": ["Sobre", "About", "Sobre el software"],
        "label_resultadoPressao": ["Resultado:", "Result:", "Resultado:"],
        "pushButton_calcular": ["Calcular", "Calculate", "Calcular"],
        "pushButton_limparCampos": ["Limpar campos", "Clear fields", "Limpiar los campos"],
        "label_erro": ["Erro", "Error", "Error"],
        "label_compMist": ["Composição da Mistura: ", "Mix composition: ", "Composición: "],
        "pushButton_infoCompMist": [
                                        "Informe a fração molar da mistura desejada.\n"
                                        "O somatório das frações deve ser igual a 1.0",
                                        "Enter the molar fraction of the desired mixture.\n"
                                        "The sum of fractions must equal 1.0",
                                        "Ingrese la fracción molar de la mezcla deseada.\n"
                                        "La suma de fracciones debe ser igual a 1.0"
                                        ],
        "pushButton_add": ["Adicionar substância", "Add substance", "Agregar sustancia"],
        "pushButton_add_tootip": ["Adicionar substância à composição", "Add substance to composition", "Agregar sustancia a la composición"],
        "label_temperatura": ["Informe a temperatura:", "Enter the temperature:", "Ingrese la temperatura:"],
        "label_pressao": ["Informe o(s) valor(es) da pressão (ATM):  ", "Enter the pressure value(s) (ATM): ", "Ingrese los valores de presión (ATM): "],
        "pushButton_infoPressao": [
                                        "Escolha \"Única\" se deseja realizar o cálculo para\n"
                                        "um valor de pressão e \"Intervalo\" caso deseje\n"
                                        "calcular para uma faixa de valores de pressão.",
                                        "Choose \"Single pressure\" if you want to perform the calculation\n"
                                        "for a pressure value and \"Pressure range\" if desired\n"
                                        "calculate for a range of pressure values.",
                                        "Elija \"Única\" si desea realizar el cálculo para \n"
                                        "un valor de presión e \"Intervalo\" si lo desea \n"
                                        "calcular para un intervalo de valores de presión."
                                        ],
        "radioButton_unica": ["Única", "Single", "Única"],
        "radioButton_intervalo": ["Intervalo", "Range", "Intervalo"],
        "pushButton_salvarResultado": ["Gerar CSV", "Generate CSV", "Generar CSV"],
        "pushButton_salvarResultado_tooltip": ["Calcular e salvar resultado em arquivo CSV", 
                                                "Calculate and save result in CSV file", 
                                                "Calcular y guardar el resultado en un archivo CSV"],
        "pushButton_gerarGrafico": ["Gráfico da Isoterma", "Isotherm Graph","Gráfico de isotermas"],
        "pushButton_gerarGrafico_tooltip": ["Calcular e gerar gráfico da Isoterma",
                                                "Calculate and generate Isotherm graph",
                                                "Calcular y generar gráfico de isotermas"],
        "lineEdit_pressaoFinal": ["FINAL", "FINAL", "FINAL"],
        "lineEdit_pressaoInicial": ["INICIAL", "INITIAL", "INICIAL"],
        "lineEdit_passo": ["PASSO", "RANGE","INTERVALO"],
        "idioma_tooltip": ["Idioma", "Language", "Idioma"],
        "label_ajuda": ["Ajuda", "Help", "Ayuda"],
        "label_ajuda_2": [
                "Para utilizar a aplicação basta informar a composição da\n"+
                "mistura, a temperatura em ATM, e o valor de pressão.\n"+
                "A pressão pode ter um único valor ou uma faixa de valores.\n"+
                "Para tal, informe os valores inicial, final e o passo entre eles.\n"+
                "\n"+
                "Ao realizar o cálculo para uma faixa de valores de pressão\n"+
                "é possível gerar o gráfico da Isoterma ou salvar o resultado\n"+
                "em um arquivo CSV (comma-separated values). Este arquivo\n"+
                "pode ser utilizado posteriormente para gerar o gráfico\n"+
                "diretamente. Para utilizar esta funcionalidade conserve o\n"+
                "formato original do arquivo, alterando apenas valores\n"+
                "numéricos, se necessário.\n"+
                "\n"+
                "Orientações gerais:\n"+
                "- A soma das frações molares deve ser igual a 1.0.\n"+
                "- Utilize ponto (.) como separador decimal.\n"+
                "- Não utilize separador de milhar.\n"+
                "- O arquivo CSV deve ser separado por ponto e vírgula (;).\n"+
                "- Não modifique o cabeçalho do arquivo CSV. Se modificado,\n"+
                "pode levar a erros na geração do gráfico.",
                #Inglês
                "To use the application, just inform the composition of\n"+
                "mix, temperature in ATM, and pressure value.\n"+
                "The pressure can be a single value or a range of values.\n"+
                "To do this, enter the initial, final and the range between them.\n"+
                "\n"+
                "When performing the calculation for a range of pressure values\n"+
                "it is possible to generate the Isotherm graph or save the result\n"+
                "in a CSV (comma-separated values) file. This file\n"+
                "can be used later to generate the graph\n"+
                "directly. To use this feature save the\n"+
                "original file format, changing values ​​only\n"+
                "numeric if necessary.\n"+
                "\n"+
                "General guidelines:\n"+
                "- The sum of the molar fractions must equal 1.0.\n"+
                "- Use period (.) as decimal separator.\n"+
                "- Do not use thousands separator.\n"+
                "- The CSV file must be separated by a semicolon (;).\n"+
                "- Do not modify the CSV file header. If modified,\n"+
                "may lead to errors in graph generation.",
                # Espanhol
                "Para usar la aplicación, solo informa la composición de \n" +
                "mezcla, temperatura en ATM y valor de presión.\n" +
                "La presión puede ser un valor único o un intervalo de valores. \n" +
                "Para hacer esto, ingrese el inicio, el final y el intervalo entre ellos. \n" +
                "\n" +
                "Al realizar el cálculo para un intervalo de valores de presión \n" +
                "es posible generar el gráfico de isotermas o guardar el resultado \n" +
                "en un archivo CSV (comma-separated values). Este archivo\n" +
                "se puede usar más tarde para generar el gráfico\n" +
                "directamente. Para utilizar esta función, guarde el\n" +
                "formato de archivo original, solo cambiar valores\n" +
                "numérico si es necesario.\n" +
                "\n" +
                "Directrices generales: \n" +
                "- La suma de las fracciones molares debe ser igual a 1.0. \n" +
                "- Utilice punto (.) Como separador decimal. \n" +
                "- No utilice separador de miles.\n" +
                "- El archivo CSV debe estar separado por un punto y coma (;). \n" +
                "- No modifique el encabezado del archivo CSV. Si se modifica, \n" +
                "puede dar lugar a errores en la generación de gráficos."
                ],
        "label_sobre": ["Sobre", "About", "Sobre el software"],
        "label_sobre_2": [
                "Calculadora de Massa Específica HidroUFF\nVersão 1.2.0\n\n"+
                "Esta aplicação tem como funcionalidade principal o cálculo \nda massa específica de misturas gasosas, "+
                "através da\n resolução da equação de estado cúbica de Peng Robinson.\n \n"+
                "Desenvolvedores:\nMateus Pereira de Sousa\nValesca Moura de Sousa\n"+
                "Orientadores:\nFernanda Gonçalves de Oliveira Passos\nRogério Fernandes de Lacerda\nFelipe Pereira de Moura\n"+
                "Última revisão: 11/08/2021",
                "HydroUFF Density Calculator\nVersion 1.2.0\n\n"+
                "This application's main functionality is to calculate \nthe density of gas mixtures, "+
                "by solving\n Peng Robinson's cubic equation of state.\n \n"+
                "Developers:\nMateus Pereira de Sousa\nValesca Moura de Sousa\n"+
                "Advisors:\nFernanda Gonçalves de Oliveira Passos\nRogério Fernandes de Lacerda\nFelipe Pereira de Moura\n"+
                "Last Revision: 08/11/2021",
                "Calculadora de densidad HydroUFF\nVersión 1.2.0\n\n" +
                "La funcionalidad principal de esta aplicación es calcular \nla densidad de mezclas de gases" +
                "resolviendo \n la ecuación cúbica de estado de Peng Robinson. \n\n" +
                "Desarrolladores:\nMateus Pereira de Sousa\nValesca Moura de Sousa\n" +
                "Asesores:\nFernanda Gonçalves de Oliveira Passos\nRogério Fernandes de Lacerda\nFelipe Pereira de Moura\n" +
                "Última revisión: 11/08/2021"
                ],
        "salvar_resultado": ["Salvar resultado", "Save result", "Salvar"],
        "arquivo": ["Arquivo csv", "CSV file", "Archivo csv"],
        "selec_arquivo": ["Selecione o arquivo", "Choose file", "Elija el archivo"],
        "erro_campos_brancos": ["Preencha todos os campos", "Fill in all fields", "Complete todos los campos"],
        "erro_subs_repetidas": [
                "Não é possível selecionar a mesma substância mais de uma vez",
                "It is not possible to select the same substance more than once",
                "No es posible seleccionar la misma sustancia más de una vez"
        ],
        "erro_fracao_molar": [
                "A soma das frações molares deve ser igual a 1.0",
                "The sum of the molar fractions must equal 1.0",
                "La suma de las fracciones molares debe ser igual a 1.0"
        ],
        "erro_formato": ["Dados em formato incorreto!", "Data in incorrect format!", "¡Datos en formato incorrecto!"]
     } 

    def onClicked(self) -> bool:
        '''
        Verifica se o radio button foi clicado e exibe o frame correspondente
        :param self: 
        :return: 
        '''

        if self.radioButton_unica.isChecked():
                self.frame_emBranco.hide()
                self.frame_pressaoIntervalo.hide()
                self.frame_pressaoUnica.show()
                return True
        elif self.radioButton_intervalo.isChecked():
                self.frame_emBranco.hide()
                self.frame_pressaoUnica.hide()
                self.frame_pressaoIntervalo.show()
                return True
        else: 
                return False

    def limparCampos(self) -> None:
            '''
            Limpa os campos preenchidos
       
            :param self: 
            :return: 
            '''

            self.lineEdit_passo.clear()
            self.lineEdit_pressao.clear()
            self.lineEdit_pressaoInicial.clear()
            self.lineEdit_pressaoFinal.clear()
            self.lineEdit_temperatura.clear()
            for substancia in self.matrizSubstancias:
                    substancia[2].clear()
            self.label_resultadoPressao.setText("Resultado:")

    def mostrarMsgmDeErro(self, mensagem) -> None:
            '''
            Mostra uma mensagem de erro na tela
       
            :param self:
            :param mensagem: string mostrada na tela 
            :return: 
            '''
            self.label_erro.setText(mensagem)
            self.frame_erro.show()

    def input(self) -> list:
        '''
        Lê os dados informados na interface e verifica se há algum problema com os dados

        :param self: 
        :return inputs: inputs = [composicao, temperatura, pressao] 
        '''
        
        #leitura dos campos
        composicao = [] #composicao = [nome da substancia, valor da substancia]
        for i in range(len(self.matrizSubstancias)):
                temp = [self.matrizSubstancias[i][1].currentText(), self.matrizSubstancias[i][2].text()]
                composicao.append(temp)
        
        unidadeDaTemperatura = self.comboBox_temperatura.currentText()
        valorDaTemperatura = self.lineEdit_temperatura.text()
        temperatura = [unidadeDaTemperatura, valorDaTemperatura]
        
        pressao = [] 
        pressaoUnica = False #calculo será realizado para uma única pressao ou um intervalo?
        if self.radioButton_unica.isChecked():
                pressao = self.lineEdit_pressao.text() #pressao = valor; se pressaoUnica True
                pressaoUnica = True
        elif self.radioButton_intervalo.isChecked():
                inicial = self.lineEdit_pressaoInicial.text()
                final = self.lineEdit_pressaoFinal.text()
                passo = self.lineEdit_passo.text()
                pressao = [inicial, final, passo] #pressao = [p.inicial, p.final, passo] ; se pressaoUnica False
                
        inputs = [composicao, temperatura, pressao]

        #checar se existem campos em branco, duplicados ou se a soma é diferente de 1.0 na composicao da mistura
        temCamposEmBranco = verificacaoDeEntrada.verificar_campos_em_branco(inputs,pressaoUnica)
        if temCamposEmBranco:
                #print("Existem campos em branco")
                self.mostrarMsgmDeErro(self.STRINGS["erro_campos_brancos"][self.codigo]) #Mostrar erro
                return ""
        temSubstanciasRepetidas = verificacaoDeEntrada.verificar_substancias_repetidas(inputs[0])
        if temSubstanciasRepetidas:
                #print("Existem substâncias repetidas")
                self.mostrarMsgmDeErro(self.STRINGS["erro_subs_repetidas"][self.codigo]) #Mostrar erro
                return ""

        # transformar strings em números
        for subs in composicao:
                subs[1] = float(subs[1])

        valorDaTemperatura = float(valorDaTemperatura)

        if pressaoUnica:
                pressao = float(pressao)
        else:
                for p in range(len(pressao)): 
                        pressao[p] = float(pressao[p])

        inputs[0] = composicao
        inputs[1] = calculadora.converter_temperatura_kelvin(unidadeDaTemperatura, valorDaTemperatura)
        inputs[2] = pressao

        somaDiferenteDeUm = calculadora.verificar_soma_fracao_molar(inputs[0])
        if somaDiferenteDeUm:
                #print("Soma != 1")
                self.mostrarMsgmDeErro(self.STRINGS["erro_fracao_molar"][self.codigo])
                return ""

        # formatar input (composicao) para o formato utilizado pela calculadora
        subs = self.STRINGS["substancias"][self.codigo]
        for i in range(len(inputs[0])):
                indice = subs.index(inputs[0][i][0])
                inputs[0][i][0] = self.STRINGS["substancias"][0][indice] # regastar palavra chave em português para ser utilizada pelo app
        inputFormatado = calculadora.formatar_input_composicao(inputs[0])
        inputs[0] = inputFormatado
        
        return inputs

    def calcular(self) -> None: 
        '''
        Lê dados da interface, obtem o resultado para o cálculo quando há uma única pressão e exibe na tela

        :param self: 
        :return: 
        '''
        
        self.frame_erro.hide() #fechar qualquer frame de erro possivelmente aberto
        dados = self.input() #ler dados formatados
        
        if dados != "":
                composicao = dados[0]
                temperatura = dados[1]
                pressao = dados[2]
                resultado = calculadora.calcular_pressao_unica(composicao, temperatura, pressao)
                self.label_resultadoPressao.setText("Massa específica: "+str(resultado)+" kg/m³")

    def salvarResultado(self) -> None:
            '''
            Lê dados da interface, obtem o resultado para o cálculo quando há um intervalo de valores de pressao e salva resultado em arquivo CSV

            :param self: 
            :return: 
            '''

            self.frame_erro.hide() #fechar qualquer frame de erro possivelmente aberto
            dados = self.input() #ler dados formatados

            if dados != "":
                nomePadraoArquivo = calculadora.obter_nome_padrao(self.codigo)
                file_Name = QFileDialog.getSaveFileName(None, self.STRINGS["salvar_resultado"][self.codigo], QDir.currentPath()+"//"+nomePadraoArquivo, self.STRINGS["arquivo"][self.codigo] + " (*.csv)")

                if file_Name[0] != "":
                        composicao = dados[0]
                        temperatura = dados[1]
                        pressaoInicial = dados[2][0]
                        pressaoFinal = dados[2][1]
                        passo = dados[2][2]

                        pressoes, massaEspecificaIsoterma = calculadora.calcular_pressao_intervalo(composicao, temperatura, pressaoInicial, pressaoFinal, passo)
                        resultado = calculadora.tabela_massa_especifica(pressoes, massaEspecificaIsoterma)
                        composicao = calculadora.to_tabela_composicao(composicao)
                        calculadora.salvar_csv(resultado, temperatura, composicao, file_Name[0], self.codigo)

    def gerarGraficoDaIsoterma(self) -> None:
            '''
            Lê dados da interface, obtem o resultado para o cálculo quando há um intervalo de valores de pressao e gera o grafico da isoterma

            :param self: 
            :return: 
            '''

            self.frame_erro.hide() #fechar qualquer frame de erro possivelmente aberto
            dados = self.input() #ler dados formatados
            
            if dados != "":
                    composicao = dados[0]
                    temperatura = dados[1]
                    pressaoInicial = dados[2][0]
                    pressaoFinal = dados[2][1]
                    passo = dados[2][2]

                    pressoes, massaEspecificaIsoterma = calculadora.calcular_pressao_intervalo(composicao, temperatura, pressaoInicial, pressaoFinal, passo)
                    calculadora.plot_isoterma(pressoes, massaEspecificaIsoterma, temperatura, self.codigo)
                    #print("Gráfico gerado")
    
    def filtrar(self) -> list:
            '''
            Obtem indice dos items já selecionados nos comboBox existentes

            :param self: 
            :return aux: vetor com indices dos items já selecionados nos comboBox existentes
            '''

            aux = []
            for s in self.matrizSubstancias:
                    index = s[1].currentIndex()
                    aux.append(index)
            
            return aux

    def getIndiceAtual(self) -> int:
            '''
            Obtem indice do próximo item ainda não selecionado nos comboBox existentes

            :param self: 
            :return indice: indice do próximo item ainda não selecionado nos comboBox existentes
            '''

            opcoesSelecionadas = self.filtrar()
            indice = 0
            for i in range(calculadora.NUM_SUBSTANCIAS):
                    if i not in opcoesSelecionadas:
                            indice = i
                            return indice
        
    def gerarGraficoAPartirDeArq(self) -> None:
        '''
        Abre caixa de diálogo de arquivo para que o usuário escolha um arquivo .csv separado por ";" com duas colunas:
        a primeira com valores de presssão e a segunda com valores da massa específica e gera o grafico da isoterma

        :param self: 
        :return: 
        '''

        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setFilter(QDir.Files)
        fileDialog.setNameFilter('*.csv')
        fileDialog.setWindowTitle(self.STRINGS["selec_arquivo"][self.codigo])

        data = ""
        file_name = ""
        if fileDialog.exec_():
                file_name = fileDialog.selectedFiles()

        if file_name != "":
                if file_name[0].endswith('.csv'):
                        temperatura, data = calculadora.ler_arquivo(file_name[0], self.codigo)        
                        if verificacaoDeEntrada.verificar_arquivo(data, temperatura):
                                data = calculadora.formatar_dados_arquivo(data)
                                calculadora.plot_isoterma(data[0], data[1], float(temperatura), self.codigo)
                        else:
                                self.mostrarMsgmDeErro(self.STRINGS["erro_formato"][self.codigo])
                        
    def add(self) -> None:
        '''
        Adiciona frames dinamicamente para novas substancias

        :param self: 
        :return: 
        '''
        
        if len(self.matrizSubstancias) < calculadora.NUM_SUBSTANCIAS:
                if len(self.matrizSubstancias) >= 3:
                        #aumentar tamanho do frame conteúdo da scroll area
                        self.frame.setMinimumHeight(self.frame.height()+self.SOMA_FRAME)

                # desativar comboBox anteriores
                for substancia in self.matrizSubstancias:
                        substancia[1].setEnabled(False)

                #criando nova substancia para a composicao
                _translate = QtCore.QCoreApplication.translate
                frame_substancia = QtWidgets.QFrame(self.frame)
                frame_substancia.setGeometry(QtCore.QRect(0, 40*len(self.matrizSubstancias), 318, 40))
                frame_substancia.setMinimumSize(QtCore.QSize(318, 40))
                frame_substancia.setMaximumSize(QtCore.QSize(318, 40))
                frame_substancia.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame_substancia.setFrameShadow(QtWidgets.QFrame.Raised)
                frame_substancia.setObjectName("frame_substancia")
                horizontalLayout = QtWidgets.QHBoxLayout(frame_substancia)
                horizontalLayout.setObjectName("horizontalLayout")

                pushButton_closeFrameSubstancia = QtWidgets.QPushButton(frame_substancia)
                pushButton_closeFrameSubstancia.setMinimumSize(QtCore.QSize(20, 20))
                pushButton_closeFrameSubstancia.setMaximumSize(QtCore.QSize(20, 20))
                idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-SemiBold.ttf")
                nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
                font = QtGui.QFont(nameFont)
                font.setPointSize(9)
                pushButton_closeFrameSubstancia.setFont(font)
                pushButton_closeFrameSubstancia.setStyleSheet("QPushButton{\n"
                "    border-radius: 10px;\n"
                "    background-color: rgb(6, 38, 101);\n"
                "    color: rgb(255, 255, 255);\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "    border: 1.5px solid rgb(8, 118, 196);\n"
                "}\n"
                "\n"
                "QPushButton:pressed{\n"
                "    background-color: rgb(8, 118, 196);\n"
                "}")
                pushButton_closeFrameSubstancia.setObjectName("pushButton_closeFrameSubstancia"+str(self.indiceBotoes))
                self.indiceBotoes += 1
                horizontalLayout.addWidget(pushButton_closeFrameSubstancia)
                pushButton_closeFrameSubstancia.setText(_translate("MainWindow", "X"))
                pushButton_closeFrameSubstancia.clicked.connect(lambda: self.delete(pushButton_closeFrameSubstancia))
                comboBox_substancias = QtWidgets.QComboBox(frame_substancia)
                comboBox_substancias.setMinimumSize(QtCore.QSize(115, 20))
                comboBox_substancias.setMaximumSize(QtCore.QSize(115, 20))
                comboBox_substancias.setStyleSheet("border: 1px solid rgb(6, 38, 101);\n"
                "border-radius: 5px;\n"
                "background-color: rgb(244, 244, 244);\n"
                "color: rgb(6, 38, 101);")
                comboBox_substancias.setDuplicatesEnabled(False)
                comboBox_substancias.setObjectName("comboBox_substancias")
                substancias = sorted(self.STRINGS["substancias"][self.codigo])
                for i in range (len(substancias)):
                        comboBox_substancias.addItem(str(i))
                        comboBox_substancias.setItemText(i, _translate("MainWindow", substancias[i]))
                
                opcoesSelecionadas = self.filtrar()
                for i in opcoesSelecionadas:
                        comboBox_substancias.model().item(i).setEnabled(False)
                        if system() == "Windows":
                                comboBox_substancias.model().item(i).setForeground(QtGui.QColor("grey"))
                        else:
                                comboBox_substancias.model().item(i).setBackground(QtGui.QColor("grey"))
                        
                
                currentIndex = self.getIndiceAtual()
                comboBox_substancias.setCurrentIndex(currentIndex)

                horizontalLayout.addWidget(comboBox_substancias)
                lineEdit_valorDaSubstancia = QtWidgets.QLineEdit(frame_substancia)
                lineEdit_valorDaSubstancia.setMinimumSize(QtCore.QSize(115, 20))
                lineEdit_valorDaSubstancia.setMaximumSize(QtCore.QSize(115, 20))
                onlyDouble = QRegExpValidator(QRegExp("[0-9]{1,20}[.][0-9]{1,20}"))
                lineEdit_valorDaSubstancia.setValidator(onlyDouble)
                idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
                nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
                font = QtGui.QFont(nameFont)
                font.setPointSize(8)
                lineEdit_valorDaSubstancia.setFont(font)
                lineEdit_valorDaSubstancia.setStyleSheet("QLineEdit{\n"
                "    border: 1px solid rgb(6, 38, 101);\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(244, 244, 244);\n"
                "}\n"
                "\n"
                "QLineEdit:hover{\n"
                "    border: 1px solid rgb(8, 118, 196);\n"
                "}")
                lineEdit_valorDaSubstancia.setText("")
                lineEdit_valorDaSubstancia.setAlignment(QtCore.Qt.AlignCenter)
                lineEdit_valorDaSubstancia.setPlaceholderText("Ex.: 0.3")
                lineEdit_valorDaSubstancia.setObjectName("lineEdit_valorDaSubstancia")
                horizontalLayout.addWidget(lineEdit_valorDaSubstancia)
                
                #tornar frame visivel
                frame_substancia.show()

                #adicinar substancia ao vetor substancias
                #substancia = [frame, comboBox, lineEdit]
                self.matrizSubstancias.append([frame_substancia, comboBox_substancias, lineEdit_valorDaSubstancia, pushButton_closeFrameSubstancia])

    def getBotaoClicado(self, botao) -> int:
        '''
        Encontra qual dos botoes dinamicos foi clicado

        :param self: 
        :return i: indice do botao dinamico clicado
        '''

        botaoClicado = botao.objectName()
        for i in range(len(self.matrizSubstancias)):
                if self.matrizSubstancias[i][3].objectName() == botaoClicado:
                        return i
    
    def delete(self, botao) -> None:
        '''
        Deleta frames das substancias adicionadas dinamicamente 

        :param self: 
        :return: 
        '''

        #obter indice do botao clicado
        botaoClicado = self.getBotaoClicado(botao)

        if len(self.matrizSubstancias) > 3:
                #diminuir tamanho do frame conteúdo da scroll area
                self.frame.setMinimumHeight(self.frame.height()-self.SOMA_FRAME)
        
        #apagar frame
        self.matrizSubstancias[botaoClicado][0].hide()
        #remover substancia do vetor
        self.matrizSubstancias.pop(botaoClicado)

        #subir frames que estavam abaixo do frame excluido
        for i in range(botaoClicado, len(self.matrizSubstancias)):
                self.matrizSubstancias[i][0].setGeometry(QtCore.QRect(0, 40*i, 322, 40))

    def ajuda(self) -> None:
        '''
        Exibe a tela ajuda

        :param self: 
        :return: 
        '''

        self.frame_erro.hide()
        self.frame_sobre.hide()
        self.frame_ajuda.show()
        self.frame_baseParaAjudaESobre.show()

    def sobre(self) -> None:
        '''
        Exibe a tela sobre o software

        :param self: 
        :return: 
        '''

        self.frame_erro.hide()
        self.frame_ajuda.hide()
        self.frame_sobre.show()
        self.frame_baseParaAjudaESobre.show()

    def fecharTela(self) -> None:
        '''
        Fecha a tela sobre o software ou tela de ajuda

        :param self: 
        :return: 
        '''

        self.frame_baseParaAjudaESobre.hide()
            
    def setarIdioma(self, MainWindow) -> None:
        idioma = self.pushButton_idioma.text()

        if idioma == "En":
            label_idioma = "Es"
            self.codigo = 1
        elif idioma == "Es":
            label_idioma = "Pt"
            self.codigo = 2
        else:
            label_idioma = "En"
            self.codigo = 0

        # limpar tela
        for i in range(len(self.matrizSubstancias)):
             self.matrizSubstancias[i][0].hide()
        self.matrizSubstancias = []
        self.limparCampos()
        self.frame_erro.hide()

        self.retranslateUi(MainWindow)
        self.pushButton_idioma.setText(label_idioma)  
        
    def setupUi(self, MainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 550)
        MainWindow.setMinimumSize(QtCore.QSize(500, 550))
        MainWindow.setMaximumSize(QtCore.QSize(500, 550))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        self.font = QtGui.QFont(nameFont)
        self.font.setPointSize(10)
        MainWindow.setFont(self.font)
        MainWindow.setStyleSheet("/*VERTICAL SCROLLBAR*/\n"
        "QScrollBar:vertical{\n"
        "    border: none;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    width: 15px;\n"
        "    margin: 15px 0 15px 0;\n"
        "    border-radius: 0px;\n"
        "}\n"
        "\n"
        "QScrollBar::handle:vertical{\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    min-height:30px;\n"
        "    border-radius: 7px;\n"
        "}\n"
        "\n"
        "QScrollBar::handle:hover{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QScrollBar::handle:pressed{\n"
        "    background-color: rgb(6, 38, 101);\n"
        "}\n"
        "\n"
        "\n"
        "QScrollBar:sub-line:vertical{\n"
        "    border: none;    \n"
        "    border-top-left-radius: 7px;\n"
        "    border-top-right-radius: 7px;\n"
        "    height: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    subcontrol-position: top;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar:sub-line:vertical:hover{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QScrollBar:sub-line:vertical:pressed{\n"
        "    background-color:  rgb(6, 38, 101);\n"
        "}\n"
        "\n"
        "QScrollBar:add-line:vertical{\n"
        "    border: none;    \n"
        "    border-bottom-left-radius: 7px;\n"
        "    border-bottom-right-radius: 7px;\n"
        "    height: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    subcontrol-position: bottom;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar:add-line:vertical:hover{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QScrollBar:add-line:vertical:pressed{\n"
        "    background-color: rgb(6, 38, 101);\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_principal = QtWidgets.QFrame(self.centralwidget)
        self.frame_principal.setGeometry(QtCore.QRect(0, 0, 500, 550))
        self.frame_principal.setMinimumSize(QtCore.QSize(500, 550))
        self.frame_principal.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_principal.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_principal.setObjectName("frame_principal")
        self.frame_superior = QtWidgets.QFrame(self.frame_principal)
        self.frame_superior.setGeometry(QtCore.QRect(0, 0, 500, 50))
        self.frame_superior.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_superior.setMaximumSize(QtCore.QSize(500, 50))
        self.frame_superior.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.label_calcMassaEsp = QtWidgets.QLabel(self.frame_superior)
        self.label_calcMassaEsp.setGeometry(QtCore.QRect(30, 8, 240, 50))
        self.label_calcMassaEsp.setMinimumSize(QtCore.QSize(240, 50))
        self.label_calcMassaEsp.setMaximumSize(QtCore.QSize(240, 50))
        idFontTitle = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Bold.ttf")
        nameFontTitle = QFontDatabase.applicationFontFamilies(idFontTitle)[0]
        fontTitle = QtGui.QFont(nameFontTitle)
        fontTitle.setBold(True)
        fontTitle.setPointSize(11)
        self.label_calcMassaEsp.setFont(fontTitle)
        self.label_calcMassaEsp.setStyleSheet("color: rgb(6, 38, 101);")
        self.label_calcMassaEsp.setObjectName("label_calcMassaEsp")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_superior)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 10, 141, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.barra_menu = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.barra_menu.setContentsMargins(0, 0, 0, 0)
        self.barra_menu.setSpacing(0)
        self.barra_menu.setObjectName("barra_menu")
        self.pushButton_grafico = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_grafico.setMinimumSize(QtCore.QSize(33, 33))
        self.pushButton_grafico.setMaximumSize(QtCore.QSize(33, 33))
        self.pushButton_grafico.setStatusTip("")
        self.pushButton_grafico.setWhatsThis("")
        self.pushButton_grafico.setAccessibleName("")
        self.pushButton_grafico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_grafico.setAutoFillBackground(False)
        self.pushButton_grafico.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius:16px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "    background-image: url(:/grafico/grafico.png);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.4px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    border: 1.6px solid rgb(8, 118, 196);\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
        self.pushButton_grafico.setText("")
        self.pushButton_grafico.setCheckable(False)
        self.pushButton_grafico.setChecked(False)
        self.pushButton_grafico.setAutoDefault(False)
        self.pushButton_grafico.setObjectName("pushButton_grafico")
        self.barra_menu.addWidget(self.pushButton_grafico)
        self.pushButton_ajuda = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_ajuda.setMinimumSize(QtCore.QSize(33, 33))
        self.pushButton_ajuda.setMaximumSize(QtCore.QSize(33, 33))
        self.pushButton_ajuda.setStatusTip("")
        self.pushButton_ajuda.setWhatsThis("")
        self.pushButton_ajuda.setAccessibleName("")
        self.pushButton_ajuda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_ajuda.setAutoFillBackground(False)
        self.pushButton_ajuda.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius:16px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "    background-image: url(:/ajuda/ajuda.png);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.4px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    border: 1.6px solid rgb(8, 118, 196);\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
        self.pushButton_ajuda.setText("")
        self.pushButton_ajuda.setCheckable(False)
        self.pushButton_ajuda.setChecked(False)
        self.pushButton_ajuda.setAutoDefault(False)
        self.pushButton_ajuda.setObjectName("pushButton_ajuda")
        self.barra_menu.addWidget(self.pushButton_ajuda)
        self.pushButton_sobre = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_sobre.setMinimumSize(QtCore.QSize(33, 33))
        self.pushButton_sobre.setMaximumSize(QtCore.QSize(33, 33))
        self.pushButton_sobre.setStatusTip("")
        self.pushButton_sobre.setWhatsThis("")
        self.pushButton_sobre.setAccessibleName("")
        self.pushButton_sobre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_sobre.setAutoFillBackground(False)
        self.pushButton_sobre.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius:16px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "    background-image: url(:/sobre/sobre.png);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.4px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    border: 1.6px solid rgb(8, 118, 196);\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
        self.pushButton_sobre.setText("")
        self.pushButton_sobre.setCheckable(False)
        self.pushButton_sobre.setChecked(False)
        self.pushButton_sobre.setAutoDefault(False)
        self.pushButton_sobre.setObjectName("pushButton_sobre")
        self.barra_menu.addWidget(self.pushButton_sobre)
        self.frame_conteudo = QtWidgets.QFrame(self.frame_principal)
        self.frame_conteudo.setGeometry(QtCore.QRect(0, 50, 500, 500))
        self.frame_conteudo.setMinimumSize(QtCore.QSize(500, 450))
        self.frame_conteudo.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_conteudo.setStatusTip("")
        self.frame_conteudo.setAccessibleDescription("")
        self.frame_conteudo.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame_conteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conteudo.setObjectName("frame_conteudo")
        self.frame_pressaoUnica = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_pressaoUnica.setGeometry(QtCore.QRect(15, 315, 470, 91))
        self.frame_pressaoUnica.setMinimumSize(QtCore.QSize(470, 0))
        self.frame_pressaoUnica.setMaximumSize(QtCore.QSize(470, 16777215))
        self.frame_pressaoUnica.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pressaoUnica.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pressaoUnica.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: 0px solid rgb(236, 236, 236);\n")
        self.frame_pressaoUnica.setObjectName("frame_pressaoUnica")
        self.label_resultadoPressao = QtWidgets.QLabel(self.frame_pressaoUnica)
        self.label_resultadoPressao.setGeometry(QtCore.QRect(50, 70, 381, 20))
        self.label_resultadoPressao.setMinimumSize(QtCore.QSize(150, 20))
        self.label_resultadoPressao.setMaximumSize(QtCore.QSize(500, 20))
        self.label_resultadoPressao.setFont(self.font)
        self.label_resultadoPressao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_resultadoPressao.setStyleSheet("color: rgb(6, 38, 101);")
        self.label_resultadoPressao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultadoPressao.setObjectName("label_resultadoPressao")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_pressaoUnica)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 30, 381, 32))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_pressaoUnica = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_pressaoUnica.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_pressaoUnica.setSpacing(0)
        self.gridLayout_pressaoUnica.setObjectName("gridLayout_pressaoUnica")
        self.pushButton_calcular = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_calcular.setMinimumSize(QtCore.QSize(150, 20))
        self.pushButton_calcular.setMaximumSize(QtCore.QSize(150, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_calcular.setFont(font)
        self.pushButton_calcular.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_calcular.setObjectName("pushButton_calcular")
        self.gridLayout_pressaoUnica.addWidget(self.pushButton_calcular, 0, 0, 1, 1)
        self.pushButton_limparCampos_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_limparCampos_3.setMinimumSize(QtCore.QSize(150, 20))
        self.pushButton_limparCampos_3.setMaximumSize(QtCore.QSize(150, 20))
        self.pushButton_limparCampos_3.setToolTip("")
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_limparCampos_3.setFont(font)
        self.pushButton_limparCampos_3.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_limparCampos_3.setObjectName("pushButton_limparCampos_3")
        self.gridLayout_pressaoUnica.addWidget(self.pushButton_limparCampos_3, 0, 1, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.frame_pressaoUnica)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 0, 381, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_pressaoUnica2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_pressaoUnica2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_pressaoUnica2.setSpacing(0)
        self.gridLayout_pressaoUnica2.setObjectName("gridLayout_pressaoUnica2")
        self.onlyDouble = QRegExpValidator(QRegExp("[0-9]{1,20}[.][0-9]{1,20}"))
        self.lineEdit_pressao = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_pressao.setMinimumSize(QtCore.QSize(150, 20))
        self.lineEdit_pressao.setMaximumSize(QtCore.QSize(150, 20))
        self.lineEdit_pressao.setValidator(self.onlyDouble)
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.lineEdit_pressao.setFont(font)
        self.lineEdit_pressao.setStyleSheet("QLineEdit{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 5px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 1px solid rgb(8, 118, 196);\n"
        "}")
        self.lineEdit_pressao.setText("")
        self.lineEdit_pressao.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pressao.setObjectName("lineEdit_pressao")
        self.gridLayout_pressaoUnica2.addWidget(self.lineEdit_pressao, 0, 0, 1, 1)
        self.frame_erro = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_erro.setGeometry(QtCore.QRect(65, 460, 370, 30))
        self.frame_erro.setMinimumSize(QtCore.QSize(370, 30))
        self.frame_erro.setMaximumSize(QtCore.QSize(370, 30))
        self.frame_erro.setStyleSheet("background-color: rgb(252, 142, 135);\n"
        "border-radius: 8px;\n"
        "\n"
        "\n"
        "")
        self.frame_erro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_erro")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_erro)
        self.horizontalLayout_2.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_erro = QtWidgets.QLabel(self.frame_erro)
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-SemiBold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.label_erro.setFont(font)
        self.label_erro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erro.setObjectName("label_erro")
        self.horizontalLayout_2.addWidget(self.label_erro)
        self.pushButton_closeErro = QtWidgets.QPushButton(self.frame_erro)
        self.pushButton_closeErro.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_closeErro.setMaximumSize(QtCore.QSize(18, 18))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-SemiBold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(9)
        self.pushButton_closeErro.setFont(font)
        self.pushButton_closeErro.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(236, 236, 236);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "")
        self.pushButton_closeErro.setObjectName("pushButton_closeErro")
        self.horizontalLayout_2.addWidget(self.pushButton_closeErro)
        self.frame_composicaoDaMistura = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_composicaoDaMistura.setGeometry(QtCore.QRect(15, 2, 470, 181))
        self.frame_composicaoDaMistura.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_composicaoDaMistura.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_composicaoDaMistura.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: none;\n")
        self.frame_composicaoDaMistura.setObjectName("frame_composicaoDaMistura")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_composicaoDaMistura)
        self.scrollArea.setGeometry(QtCore.QRect(77, 30, 327, 120))
        self.scrollArea.setMinimumSize(QtCore.QSize(327, 120))
        self.scrollArea.setMaximumSize(QtCore.QSize(327, 120))
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
        "    border: none;\n"
        "    background: rgb(236, 236, 236);\n"
        "}")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 381, 120))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(327, 40))
        self.frame.setMaximumSize(QtCore.QSize(327, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: none;\n")
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_composicaoDaMistura)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 0, 383, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layout_compMist = QtWidgets.QGridLayout(self.layoutWidget1)
        self.layout_compMist.setContentsMargins(0, 0, 220, 0)
        self.layout_compMist.setSpacing(0)
        self.layout_compMist.setObjectName("layout_compMist")
        self.label_compMist = QtWidgets.QLabel(self.layoutWidget1)
        """ self.label_compMist.setMinimumSize(QtCore.QSize(150, 20))
        self.label_compMist.setMaximumSize(QtCore.QSize(150, 20)) """
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(10)
        self.label_compMist.setFont(font)
        self.label_compMist.setStyleSheet("color: rgb(6, 38, 101);")
        self.label_compMist.setObjectName("label_compMist")
        self.layout_compMist.addWidget(self.label_compMist, 0, 0, 1, 1)
        self.pushButton_infoCompMist = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_infoCompMist.setMinimumSize(QtCore.QSize(12, 12))
        self.pushButton_infoCompMist.setMaximumSize(QtCore.QSize(12, 12))
        self.pushButton_infoCompMist.setStatusTip("")
        self.pushButton_infoCompMist.setWhatsThis("")
        self.pushButton_infoCompMist.setAccessibleName("")
        self.pushButton_infoCompMist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_infoCompMist.setAutoFillBackground(False)
        self.pushButton_infoCompMist.setStyleSheet("QPushButton{\n"
                "    border: 1px solid rgb(6, 38, 101);\n"
                "    border-radius:6px;\n"
                "    padding: 15px;\n"
                "    background-color: rgb(244, 244, 244);\n"
                "    background-image: url(:/info/info.png);\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "    border: 1.4px solid rgb(8, 118, 196);\n"
                "}")
        self.pushButton_infoCompMist.setText("")
        self.pushButton_infoCompMist.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_infoCompMist.setCheckable(False)
        self.pushButton_infoCompMist.setChecked(False)
        self.pushButton_infoCompMist.setAutoDefault(False)
        self.pushButton_infoCompMist.setObjectName("pushButton_infoCompMist")
        self.layout_compMist.addWidget(self.pushButton_infoCompMist, 0, 1, 1, 1)
        self.label_compMist_espaco = QtWidgets.QLabel(self.layoutWidget1)
        self.layout_compMist.addWidget(self.label_compMist_espaco, 0, 2)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_composicaoDaMistura)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 150, 381, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layout_botoesComposicao = QtWidgets.QGridLayout(self.layoutWidget2)
        self.layout_botoesComposicao.setContentsMargins(0, 0, 0, 0)
        self.layout_botoesComposicao.setSpacing(0)
        self.layout_botoesComposicao.setObjectName("layout_botoesComposicao")
        self.pushButton_add = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_add.setMinimumSize(QtCore.QSize(326, 20))
        self.pushButton_add.setMaximumSize(QtCore.QSize(326, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.layout_botoesComposicao.addWidget(self.pushButton_add, 0, 0, 1, 1)
        self.frame_temperatura = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_temperatura.setGeometry(QtCore.QRect(15, 185, 470, 61))
        self.frame_temperatura.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_temperatura.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_temperatura.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: 0px solid rgb(236, 236, 236);\n")
        self.frame_temperatura.setObjectName("frame_temperatura")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.frame_temperatura)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(50, 0, 381, 61))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_temperatura = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_temperatura.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_temperatura.setSpacing(0)
        self.verticalLayout_temperatura.setObjectName("verticalLayout_temperatura")
        self.gridLayout_temperatura = QtWidgets.QGridLayout()
        self.gridLayout_temperatura.setSpacing(0)
        self.gridLayout_temperatura.setObjectName("gridLayout_temperatura")
        self.label_temperatura = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_temperatura.setMinimumSize(QtCore.QSize(60, 20))
        self.label_temperatura.setMaximumSize(QtCore.QSize(500, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(10)
        self.label_temperatura.setFont(font)
        self.label_temperatura.setStyleSheet("color: rgb(6, 38, 101);")
        self.label_temperatura.setObjectName("label_temperatura")
        self.gridLayout_temperatura.addWidget(self.label_temperatura, 0, 0, 1, 1)
        self.verticalLayout_temperatura.addLayout(self.gridLayout_temperatura)
        self.gridLayout_temperatura_2 = QtWidgets.QGridLayout()
        self.gridLayout_temperatura_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_temperatura_2.setSpacing(0)
        self.gridLayout_temperatura_2.setObjectName("gridLayout_temperatura_2")
        self.comboBox_temperatura = QtWidgets.QComboBox(self.verticalLayoutWidget_9)
        self.comboBox_temperatura.setMinimumSize(QtCore.QSize(115, 20))
        self.comboBox_temperatura.setMaximumSize(QtCore.QSize(115, 20))
        self.comboBox_temperatura.setStyleSheet("border: 1px solid rgb(6, 38, 101);\n"
        "border-radius: 5px;\n"
        "background-color: rgb(244, 244, 244);\n"
        "color: rgb(6, 38, 101);")
        self.comboBox_temperatura.setDuplicatesEnabled(False)
        self.comboBox_temperatura.setObjectName("comboBox_temperatura")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.comboBox_temperatura.addItem("")
        self.gridLayout_temperatura_2.addWidget(self.comboBox_temperatura, 0, 0, 1, 1)
        self.lineEdit_temperatura = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.lineEdit_temperatura.setMinimumSize(QtCore.QSize(115, 20))
        self.lineEdit_temperatura.setMaximumSize(QtCore.QSize(115, 20))
        self.onlyDouble = QRegExpValidator(QRegExp("[-+]?[0-9]{1,20}[.][0-9]{1,20}"))
        self.lineEdit_temperatura.setValidator(self.onlyDouble)
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.lineEdit_temperatura.setFont(font)
        self.lineEdit_temperatura.setStyleSheet("QLineEdit{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 5px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 1px solid rgb(8, 118, 196);\n"
        "}")
        self.lineEdit_temperatura.setText("")
        self.lineEdit_temperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_temperatura.setObjectName("lineEdit_temperatura")
        self.gridLayout_temperatura_2.addWidget(self.lineEdit_temperatura, 0, 1, 1, 1)
        self.verticalLayout_temperatura.addLayout(self.gridLayout_temperatura_2)
        self.frame_pressao = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_pressao.setGeometry(QtCore.QRect(15, 246, 470, 71))
        self.frame_pressao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pressao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pressao.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: 0px solid rgb(236, 236, 236);\n")
        self.frame_pressao.setObjectName("frame_pressao")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.frame_pressao)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(50, 0, 381, 66))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_pressao = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_pressao.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_pressao.setSpacing(0)
        self.verticalLayout_pressao.setObjectName("verticalLayout_pressao")
        self.gridLayout_pressao = QtWidgets.QGridLayout()
        self.gridLayout_pressao.setContentsMargins(-1, -1, 130, -1)
        self.gridLayout_pressao.setSpacing(0)
        self.gridLayout_pressao.setObjectName("gridLayout_pressao")
        self.label_pressao = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_pressao.setMinimumSize(QtCore.QSize(60, 20))
        self.label_pressao.setMaximumSize(QtCore.QSize(240, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(10)
        self.label_pressao.setFont(font)
        self.label_pressao.setStyleSheet("color: rgb(6, 38, 101);")
        self.label_pressao.setObjectName("label_pressao")
        self.gridLayout_pressao.addWidget(self.label_pressao, 0, 0, 1, 1)
        self.pushButton_infoPressao = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_infoPressao.setMinimumSize(QtCore.QSize(12, 12))
        self.pushButton_infoPressao.setMaximumSize(QtCore.QSize(12, 12))
        self.pushButton_infoPressao.setStatusTip("")
        self.pushButton_infoPressao.setWhatsThis("")
        self.pushButton_infoPressao.setAccessibleName("")
        self.pushButton_infoPressao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_infoPressao.setAutoFillBackground(False)
        self.pushButton_infoPressao.setStyleSheet("QPushButton{\n"
                "    border: 1px solid rgb(6, 38, 101);\n"
                "    border-radius:6px;\n"
                "    padding: 15px;\n"
                "    background-color: rgb(244, 244, 244);\n"
                "    background-image: url(:/info/info.png);\n"
                "}\n"
                "\n"
                "QPushButton:hover{\n"
                "    border: 1.4px solid rgb(8, 118, 196);\n"
                "}")
        self.pushButton_infoPressao.setText("")
        self.pushButton_infoPressao.setCheckable(False)
        self.pushButton_infoPressao.setChecked(False)
        self.pushButton_infoPressao.setAutoDefault(False)
        self.pushButton_infoPressao.setObjectName("pushButton_infoPressao")
        self.gridLayout_pressao.addWidget(self.pushButton_infoPressao, 0, 1, 1, 1)
        self.label_pressao_espaco = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.gridLayout_pressao.addWidget(self.label_pressao_espaco, 0, 2)
        self.verticalLayout_pressao.addLayout(self.gridLayout_pressao)
        self.gridLayout_radioButtonPressao = QtWidgets.QGridLayout()
        self.gridLayout_radioButtonPressao.setSpacing(0)
        self.gridLayout_radioButtonPressao.setObjectName("gridLayout_radioButtonPressao")
        self.radioButton_unica = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.radioButton_unica.setMinimumSize(QtCore.QSize(70, 20))
        self.radioButton_unica.setMaximumSize(QtCore.QSize(70, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(9)
        self.radioButton_unica.setFont(font)
        self.radioButton_unica.setStyleSheet("color: rgb(6, 38, 101);")
        self.radioButton_unica.setObjectName("radioButton_unica")
        self.gridLayout_radioButtonPressao.addWidget(self.radioButton_unica, 0, 0, 1, 1)
        self.radioButton_intervalo = QtWidgets.QRadioButton(self.verticalLayoutWidget_10)
        self.radioButton_intervalo.setMinimumSize(QtCore.QSize(70, 20))
        self.radioButton_intervalo.setMaximumSize(QtCore.QSize(70, 20))
        self.radioButton_intervalo.setFont(font)
        self.radioButton_intervalo.setStyleSheet("color: rgb(6, 38, 101);")
        self.radioButton_intervalo.setObjectName("radioButton_intervalo")
        self.gridLayout_radioButtonPressao.addWidget(self.radioButton_intervalo, 0, 1, 1, 1)
        self.verticalLayout_pressao.addLayout(self.gridLayout_radioButtonPressao)
        self.widget_logo = QtWidgets.QWidget(self.frame_conteudo)
        self.widget_logo.setGeometry(QtCore.QRect(350, 460, 118, 25))
        self.widget_logo.setMinimumSize(QtCore.QSize(118, 25))
        self.widget_logo.setMaximumSize(QtCore.QSize(118, 25))
        self.widget_logo.setStyleSheet("background-image: url(:/hidrouff/hidrouff.png);")
        self.widget_logo.setObjectName("widget_logo")


        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-SemiBold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        fontSemiBold = QtGui.QFont(nameFont)
        fontSemiBold.setPointSize(9)

        self.pushButton_idioma = QtWidgets.QPushButton(self.frame_conteudo)
        self.pushButton_idioma.setGeometry(QtCore.QRect(30, 460, 25, 25))
        self.pushButton_idioma.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_idioma.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_idioma.setFont(fontSemiBold) 
        self.pushButton_idioma.setStyleSheet("QPushButton{\n"
                                        "    border: 1px solid rgb(6, 38, 101);\n"
                                        "    border-radius: 12px;\n"
                                        "    padding: 2px;\n"
                                        "    background-color: rgb(6, 38, 101);\n"
                                        "    color: rgb(255,255,255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 1.5px solid rgb(8, 118, 196);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgb(8, 118, 196);\n"
                                        "}")
        self.pushButton_idioma.setCheckable(False)
        self.pushButton_idioma.setChecked(False)
        self.pushButton_idioma.setAutoDefault(False)
        self.pushButton_idioma.setObjectName("pushButton_idioma")

        self.frame_emBranco = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_emBranco.setGeometry(QtCore.QRect(15, 310, 470, 130))
        self.frame_emBranco.setMinimumSize(QtCore.QSize(470, 130))
        self.frame_emBranco.setMaximumSize(QtCore.QSize(470, 16777215))
        self.frame_emBranco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_emBranco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_emBranco.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: 0px solid rgb(236, 236, 236);\n")
        self.frame_emBranco.setObjectName("frame_emBranco")
        self.pushButton_limparCampos = QtWidgets.QPushButton(self.frame_emBranco)
        self.pushButton_limparCampos.setGeometry(QtCore.QRect(77, 40, 326, 20))
        self.pushButton_limparCampos.setMinimumSize(QtCore.QSize(326, 20))
        self.pushButton_limparCampos.setMaximumSize(QtCore.QSize(326, 20))
        self.pushButton_limparCampos.setToolTip("")
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_limparCampos.setFont(font)
        self.pushButton_limparCampos.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_limparCampos.setObjectName("pushButton_limparCampos")
        self.frame_pressaoIntervalo = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_pressaoIntervalo.setGeometry(QtCore.QRect(15, 310, 470, 120))
        self.frame_pressaoIntervalo.setMinimumSize(QtCore.QSize(470, 0))
        self.frame_pressaoIntervalo.setMaximumSize(QtCore.QSize(470, 16777215))
        self.frame_pressaoIntervalo.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame_pressaoIntervalo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pressaoIntervalo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pressaoIntervalo.setStyleSheet("background-color: rgb(236, 236, 236);\n"
        "border: 0px solid rgb(236, 236, 236);\n")
        self.frame_pressaoIntervalo.setObjectName("frame_pressaoIntervalo")
        self.layoutWidget_5 = QtWidgets.QWidget(self.frame_pressaoIntervalo)
        self.layoutWidget_5.setGeometry(QtCore.QRect(50, 40, 381, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_botoesPIntervalo = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_botoesPIntervalo.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_botoesPIntervalo.setSpacing(0)
        self.gridLayout_botoesPIntervalo.setObjectName("gridLayout_botoesPIntervalo")
        self.pushButton_salvarResultado = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_salvarResultado.setMinimumSize(QtCore.QSize(150, 20))
        self.pushButton_salvarResultado.setMaximumSize(QtCore.QSize(150, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_salvarResultado.setFont(font)
        self.pushButton_salvarResultado.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_salvarResultado.setObjectName("pushButton_salvarResultado")
        self.gridLayout_botoesPIntervalo.addWidget(self.pushButton_salvarResultado, 0, 1, 1, 1)
        self.pushButton_gerarGrafico = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_gerarGrafico.setMinimumSize(QtCore.QSize(150, 20))
        self.pushButton_gerarGrafico.setMaximumSize(QtCore.QSize(150, 20))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_gerarGrafico.setFont(font)
        self.pushButton_gerarGrafico.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_gerarGrafico.setObjectName("pushButton_gerarGrafico")
        self.gridLayout_botoesPIntervalo.addWidget(self.pushButton_gerarGrafico, 0, 0, 1, 1)
        self.pushButton_limparCampos_2 = QtWidgets.QPushButton(self.frame_pressaoIntervalo)
        self.pushButton_limparCampos_2.setGeometry(QtCore.QRect(77, 70, 326, 20))
        self.pushButton_limparCampos_2.setMinimumSize(QtCore.QSize(326, 20))
        self.pushButton_limparCampos_2.setMaximumSize(QtCore.QSize(326, 20))
        self.pushButton_limparCampos_2.setToolTip("")
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.pushButton_limparCampos_2.setFont(font)
        self.pushButton_limparCampos_2.setStyleSheet("QPushButton{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 6px;\n"
        "    padding: 15px;\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255,255,255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    border: 1.5px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(8, 118, 196);\n"
        "}")
        self.pushButton_limparCampos_2.setObjectName("pushButton_limparCampos_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_pressaoIntervalo)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 0, 381, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_pressaoIntervalo = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_pressaoIntervalo.setContentsMargins(14, 0, 13, 0)
        self.gridLayout_pressaoIntervalo.setSpacing(0)
        self.gridLayout_pressaoIntervalo.setObjectName("gridLayout_pressaoIntervalo")
        self.lineEdit_pressaoFinal = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_pressaoFinal.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_pressaoFinal.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_pressaoFinal.setValidator(self.onlyDouble)
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.lineEdit_pressaoFinal.setFont(font)
        self.lineEdit_pressaoFinal.setStyleSheet("QLineEdit{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 5px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 1px solid rgb(8, 118, 196);\n"
        "}")
        self.lineEdit_pressaoFinal.setText("")
        self.lineEdit_pressaoFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pressaoFinal.setObjectName("lineEdit_pressaoFinal")
        self.gridLayout_pressaoIntervalo.addWidget(self.lineEdit_pressaoFinal, 0, 1, 1, 1)
        self.lineEdit_passo = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_passo.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_passo.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_passo.setValidator(self.onlyDouble)
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.lineEdit_passo.setFont(font)
        self.lineEdit_passo.setStyleSheet("QLineEdit{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 5px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 1px solid rgb(8, 118, 196);\n"
        "}")
        self.lineEdit_passo.setText("")
        self.lineEdit_passo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_passo.setObjectName("lineEdit_passo")
        self.gridLayout_pressaoIntervalo.addWidget(self.lineEdit_passo, 0, 2, 1, 1)
        self.lineEdit_pressaoInicial = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_pressaoInicial.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_pressaoInicial.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_pressaoInicial.setValidator(self.onlyDouble)
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(8)
        self.lineEdit_pressaoInicial.setFont(font)
        self.lineEdit_pressaoInicial.setStyleSheet("QLineEdit{\n"
        "    border: 1px solid rgb(6, 38, 101);\n"
        "    border-radius: 5px;\n"
        "    background-color: rgb(244, 244, 244);\n"
        "}\n"
        "\n"
        "QLineEdit:hover{\n"
        "    border: 1px solid rgb(8, 118, 196);\n"
        "}")
        self.lineEdit_pressaoInicial.setText("")
        self.lineEdit_pressaoInicial.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pressaoInicial.setObjectName("lineEdit_pressaoInicial")
        self.gridLayout_pressaoIntervalo.addWidget(self.lineEdit_pressaoInicial, 0, 0, 1, 1)
        self.frame_baseParaAjudaESobre = QtWidgets.QFrame(self.frame_conteudo)
        self.frame_baseParaAjudaESobre.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.frame_baseParaAjudaESobre.setMinimumSize(QtCore.QSize(500, 450))
        self.frame_baseParaAjudaESobre.setMaximumSize(QtCore.QSize(500, 450))
        self.frame_baseParaAjudaESobre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_baseParaAjudaESobre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_baseParaAjudaESobre.setObjectName("frame_baseParaAjudaESobre")
        self.frame_ajuda = QtWidgets.QFrame(self.frame_baseParaAjudaESobre)
        self.frame_ajuda.setGeometry(QtCore.QRect(10, 0, 480, 400))
        self.frame_ajuda.setMinimumSize(QtCore.QSize(480, 450))
        self.frame_ajuda.setMaximumSize(QtCore.QSize(480, 450))
        self.frame_ajuda.setStyleSheet("background-color: rgb(6, 38, 101);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "")
        self.frame_ajuda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ajuda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ajuda.setObjectName("frame_ajuda")
        self.pushButton_closeAjuda = QtWidgets.QPushButton(self.frame_ajuda)
        self.pushButton_closeAjuda.setGeometry(QtCore.QRect(450, 10, 18, 18))
        self.pushButton_closeAjuda.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_closeAjuda.setMaximumSize(QtCore.QSize(18, 18))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-SemiBold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(9)
        self.pushButton_closeAjuda.setFont(font)
        self.pushButton_closeAjuda.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px;\n"
        "    color: rgb(6, 38, 101);\n"
        "    background-color: rgb(236, 236, 236);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(236, 236, 236);\n"
        "    border: 1.4px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "")
        self.pushButton_closeAjuda.setObjectName("pushButton_closeAjuda")
        self.label_ajuda = QtWidgets.QLabel(self.frame_ajuda)
        self.label_ajuda.setGeometry(QtCore.QRect(20, 0, 240, 40))
        self.label_ajuda.setMinimumSize(QtCore.QSize(240, 40))
        self.label_ajuda.setMaximumSize(QtCore.QSize(240, 40))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Bold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(11)
        font.setBold(True)
        self.label_ajuda.setFont(font)
        self.label_ajuda.setStyleSheet("color: rgb(255,255,255);")
        self.label_ajuda.setObjectName("label_ajuda")
        self.line = QtWidgets.QFrame(self.frame_ajuda)
        self.line.setGeometry(QtCore.QRect(15, 40, 450, 1))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_ajuda_2 = QtWidgets.QLabel(self.frame_ajuda)
        self.label_ajuda_2.setGeometry(QtCore.QRect(40, 45, 400, 400))
        self.label_ajuda_2.setMinimumSize(QtCore.QSize(400, 400))
        self.label_ajuda_2.setMaximumSize(QtCore.QSize(400, 400))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(10)
        self.label_ajuda_2.setFont(font)
        self.label_ajuda_2.setStyleSheet("color: rgb(255,255,255);")
        self.label_ajuda_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ajuda_2.setObjectName("label_ajuda_2")
        self.frame_sobre = QtWidgets.QFrame(self.frame_baseParaAjudaESobre)
        self.frame_sobre.setGeometry(QtCore.QRect(10, 0, 480, 400))
        self.frame_sobre.setMinimumSize(QtCore.QSize(480, 450))
        self.frame_sobre.setMaximumSize(QtCore.QSize(480, 450))
        self.frame_sobre.setStyleSheet("background-color: rgb(6, 38, 101);\n"
        "border-radius: 10px;\n"
        "\n"
        "\n"
        "")
        self.frame_sobre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sobre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sobre.setObjectName("frame_sobre")
        self.pushButton_closeSobre = QtWidgets.QPushButton(self.frame_sobre)
        self.pushButton_closeSobre.setGeometry(QtCore.QRect(450, 10, 18, 18))
        self.pushButton_closeSobre.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_closeSobre.setMaximumSize(QtCore.QSize(18, 18))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-SemiBold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(9)
        self.pushButton_closeSobre.setFont(font)
        self.pushButton_closeSobre.setStyleSheet("QPushButton{\n"
        "    border-radius: 5px;\n"
        "    color: rgb(6, 38, 101);\n"
        "    background-color: rgb(236, 236, 236);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(236, 236, 236);\n"
        "    border: 1.4px solid rgb(8, 118, 196);\n"
        "}\n"
        "\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(6, 38, 101);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "")
        self.pushButton_closeSobre.setObjectName("pushButton_closeAjuda")
        self.label_sobre = QtWidgets.QLabel(self.frame_sobre)
        self.label_sobre.setGeometry(QtCore.QRect(20, 0, 240, 40))
        self.label_sobre.setMinimumSize(QtCore.QSize(240, 40))
        self.label_sobre.setMaximumSize(QtCore.QSize(240, 40))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Bold.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(11)
        font.setBold(True)
        self.label_sobre.setFont(font)
        self.label_sobre.setStyleSheet("color: rgb(255,255,255);")
        self.label_sobre.setObjectName("label_sobre")
        self.line_sobre = QtWidgets.QFrame(self.frame_sobre)
        self.line_sobre.setGeometry(QtCore.QRect(15, 40, 450, 1))
        self.line_sobre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_sobre.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_sobre.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_sobre.setObjectName("line_sobre")
        self.label_sobre_2 = QtWidgets.QLabel(self.frame_sobre)
        self.label_sobre_2.setGeometry(QtCore.QRect(40, 70, 400, 300))
        self.label_sobre_2.setMinimumSize(QtCore.QSize(400, 300))
        self.label_sobre_2.setMaximumSize(QtCore.QSize(400, 300))
        idFont = QFontDatabase.addApplicationFont(":/fonts/OpenSans-Regular.ttf")
        nameFont = QFontDatabase.applicationFontFamilies(idFont)[0]
        font = QtGui.QFont(nameFont)
        font.setPointSize(10)
        self.label_sobre_2.setFont(font)
        self.label_sobre_2.setStyleSheet("color: rgb(255,255,255);")
        self.label_sobre_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sobre_2.setObjectName("label_sobre_2")
        self.widget_logoHidroUFF = QtWidgets.QWidget(self.frame_sobre)
        self.widget_logoHidroUFF.setGeometry(QtCore.QRect(410, 380, 50, 50))
        self.widget_logoHidroUFF.setMinimumSize(QtCore.QSize(50, 50))
        self.widget_logoHidroUFF.setMaximumSize(QtCore.QSize(50, 50))
        self.widget_logoHidroUFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget_logoHidroUFF.setStyleSheet("background-image: url(:/hidrouff/hidroufflogo.png);")
        self.widget_logoHidroUFF.setObjectName("widget_logoHidroUFF")
        self.widget_logoUFF = QtWidgets.QWidget(self.frame_sobre)
        self.widget_logoUFF.setGeometry(QtCore.QRect(350, 374, 50, 56))
        self.widget_logoUFF.setMinimumSize(QtCore.QSize(50, 56))
        self.widget_logoUFF.setMaximumSize(QtCore.QSize(50, 56))
        self.widget_logoUFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget_logoUFF.setStyleSheet("background-image: url(:/uff/ufflogo.png);")
        self.widget_logoUFF.setObjectName("widget_logoUFF")

        self.widget_logo.raise_()
        self.pushButton_idioma.raise_()
        self.frame_pressaoUnica.raise_()
        self.frame_erro.raise_()
        self.frame_composicaoDaMistura.raise_()
        self.frame_temperatura.raise_()
        self.frame_pressao.raise_()
        self.frame_pressaoIntervalo.raise_()
        self.frame_emBranco.raise_()
        self.frame_baseParaAjudaESobre.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #
        # FUNCTIONS
        #

        #Fechar popup
        self.pushButton_closeErro.clicked.connect(lambda: self.frame_erro.hide())
        self.frame_erro.hide()

        #Limpar todos os campos
        self.pushButton_limparCampos.clicked.connect(self.limparCampos)
        self.pushButton_limparCampos_2.clicked.connect(self.limparCampos)
        self.pushButton_limparCampos_3.clicked.connect(self.limparCampos)

        #Mostrar frame apropriado de acordo com radio button selecionado - pressao
        self.radioButton_unica.toggled.connect(self.onClicked)
        self.radioButton_intervalo.toggled.connect(self.onClicked)
        
        #Conectar funções aos botões
        self.pushButton_salvarResultado.clicked.connect(self.salvarResultado)
        self.pushButton_gerarGrafico.clicked.connect(self.gerarGraficoDaIsoterma)
        self.pushButton_calcular.clicked.connect(self.calcular)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_ajuda.clicked.connect(self.ajuda)
        self.pushButton_closeAjuda.clicked.connect(self.fecharTela)
        self.frame_baseParaAjudaESobre.hide()
        self.pushButton_sobre.clicked.connect(self.sobre)
        self.pushButton_closeSobre.clicked.connect(self.fecharTela)
        self.frame_baseParaAjudaESobre.hide()
        self.pushButton_grafico.clicked.connect(self.gerarGraficoAPartirDeArq)
        self.pushButton_idioma.clicked.connect(lambda: self.setarIdioma(MainWindow))

    def retranslateUi(self, MainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.STRINGS["title"][self.codigo]))
        self.label_calcMassaEsp.setText(_translate("MainWindow", self.STRINGS["label_calcMassaEsp"][self.codigo]))
        self.pushButton_grafico.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_grafico"][self.codigo]))
        self.pushButton_ajuda.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_ajuda"][self.codigo]))
        self.pushButton_sobre.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_sobre"][self.codigo]))
        self.label_resultadoPressao.setText(_translate("MainWindow", self.STRINGS["label_resultadoPressao"][self.codigo]))
        self.pushButton_calcular.setText(_translate("MainWindow", self.STRINGS["pushButton_calcular"][self.codigo]))
        self.pushButton_limparCampos_3.setText(_translate("MainWindow", self.STRINGS["pushButton_limparCampos"][self.codigo]))
        self.lineEdit_pressao.setPlaceholderText(_translate("MainWindow", "100.8"))
        self.label_erro.setText(_translate("MainWindow", self.STRINGS["label_erro"][self.codigo]))
        self.pushButton_closeErro.setText(_translate("MainWindow", "X"))
        self.label_compMist.setText(_translate("MainWindow", self.STRINGS["label_compMist"][self.codigo]))
        self.pushButton_infoCompMist.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_infoCompMist"][self.codigo]))
        self.pushButton_add.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_add_tootip"][self.codigo]))
        self.pushButton_add.setText(_translate("MainWindow", self.STRINGS["pushButton_add"][self.codigo]))
        self.label_temperatura.setText(_translate("MainWindow", self.STRINGS["label_temperatura"][self.codigo]))
        for i in range(len(calculadora.ESCALAS_DE_TEMPERATURA)):
                self.comboBox_temperatura.setItemText(i, _translate("MainWindow", calculadora.ESCALAS_DE_TEMPERATURA[i]))
        self.comboBox_temperatura.setCurrentIndex(2) #Kelvin
        self.lineEdit_temperatura.setPlaceholderText(_translate("MainWindow", "275.50"))
        self.label_pressao.setText(_translate("MainWindow", self.STRINGS["label_pressao"][self.codigo]))
        self.pushButton_infoPressao.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_infoPressao"][self.codigo]))
        self.radioButton_unica.setText(_translate("MainWindow", self.STRINGS["radioButton_unica"][self.codigo]))
        self.radioButton_intervalo.setText(_translate("MainWindow", self.STRINGS["radioButton_intervalo"][self.codigo]))
        self.pushButton_limparCampos.setText(_translate("MainWindow", self.STRINGS["pushButton_limparCampos"][self.codigo]))
        self.pushButton_salvarResultado.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_salvarResultado_tooltip"][self.codigo]))
        self.pushButton_salvarResultado.setText(_translate("MainWindow", self.STRINGS["pushButton_salvarResultado"][self.codigo]))
        self.pushButton_gerarGrafico.setToolTip(_translate("MainWindow", self.STRINGS["pushButton_gerarGrafico_tooltip"][self.codigo]))
        self.pushButton_gerarGrafico.setText(_translate("MainWindow", self.STRINGS["pushButton_gerarGrafico"][self.codigo]))
        self.pushButton_limparCampos_2.setText(_translate("MainWindow", self.STRINGS["pushButton_limparCampos"][self.codigo]))
        self.lineEdit_pressaoFinal.setPlaceholderText(_translate("MainWindow", self.STRINGS["lineEdit_pressaoFinal"][self.codigo]))
        self.lineEdit_passo.setPlaceholderText(_translate("MainWindow", self.STRINGS["lineEdit_passo"][self.codigo]))
        self.lineEdit_pressaoInicial.setPlaceholderText(_translate("MainWindow", self.STRINGS["lineEdit_pressaoInicial"][self.codigo]))
        self.pushButton_closeAjuda.setText(_translate("MainWindow", "X"))
        self.pushButton_idioma.setText(_translate("MainWindow", "En"))
        self.pushButton_idioma.setToolTip(_translate("MainWindow", self.STRINGS["idioma_tooltip"][self.codigo]))
        self.label_ajuda.setText(_translate("MainWindow", self.STRINGS["label_ajuda"][self.codigo]))
        self.label_ajuda_2.setText(_translate("MainWindow", self.STRINGS["label_ajuda_2"][self.codigo]))
        self.pushButton_closeSobre.setText(_translate("MainWindow", "X"))
        self.label_sobre.setText(_translate("MainWindow", self.STRINGS["label_sobre"][self.codigo]))
        self.label_sobre_2.setText(_translate("MainWindow", self.STRINGS["label_sobre_2"][self.codigo]))
