# Calculadora de Massa Específica

Esta aplicação tem como funcionalidade principal o cálculo da massa especifica de misturas gasosas, através da resolução da equação de estado cúbica de Peng Robinson.

## Tecnologia

Python 3
* Sympy
* Matplotlib
* PyQt5

## Como utilizar a calculadora
Para utilizar a aplicação basta informar a fração molar de cada substância que compõe a mistura, a temperatura em ATM, e o valor de pressão. A pressão pode ter um único valor ou uma faixa de valores. Para tal, informe os valores inicial, final e o passo entre eles. Ao realizar o cálculo para uma faixa de valores de pressão é possível gerar o gráfico da Isoterma ou salvar o resultado em um arquivo .csv (comma-separated values). Este arquivo pode ser utilizado posteriormente para gerar o gráfico diretamente, sem a necessidade de nova realização dos cálculos. Para utilizar esta funcionalidade conserve o formato original do arquivo, alterando apenas valores numéricos, se necessário.

### Orientações Gerais

* A soma das frações molares deve ser igual a 1.0.
* Utilize ponto (.) como separador decimal.
* Não utilize separador de milhar.
* O arquivo .csv deve ser separado por ponto e vírgula (;).
* Não modifique o cabeçalho do arquivo .csv, pois ele é utilizado pelo programa. Se modificado, pode levar a erros na leitura do arquivo e geração do gráfico a partir dele.
    * As palavras chaves utilizadas em determinadas linhas para identificar cada uma das colunas não deve ter nenhuma de suas letras alteradas.
    * Estrutura do arquivo: 
        * Primeira linha chave: Composição
        * Segunda linha chave: Substância;Fração Molar (lembrando que ; separa as colunas do arquivo)
        * Abaixo estão registrados nomes das substâncias selecionadas na primeira coluna e a fração molar destas substâncias na segunda coluna. Ex.: CO2;1.0
        * Terceira linha chave: Temperatura
        * Abaixo estará registrado algum valor de temperatura em Kelvin. Ex.: 100.0
        * Quarta linha chave: Massa Específica
        * Quinta linha chave: atm;kg/m³
        * Abaixo estão registrados valores de pressão e massa específica. Ex.: 1e-08;1533.491

## Execução da Calculadora de Massa Específica HidroUFF (Via arquivo executável)

* Basta realizar o download do arquivo **Calculadora de Massa Específica HidroUFF.exe**, que se encontra no diretório /bin, em seu computador e executá-lo. Não é necessário realizar qualquer instalação.
* O arquivo executável é compatível apenas com o sistema operacional Windows. 

## Instalação e execução (Via código fonte)

### Requisitos para a execução do código

* Python 3.x
* Sympy
* Matplotlib
* PyQt5

### Como instalar os requisitos

* Para instalar a linguagem Python, acesse: https://www.python.org/downloads/
* Para instalar as bibliotecas/pacotes via PIP:
    * Sympy: digite no CMD ```pip install sympy```
    * Matplotlib: digite no CMD ```pip install matplotlib```
    * PyQt5: digite no CMD ```pip install PyQt5```
* Como instalar o PIP no Windows: https://www.youtube.com/watch?v=qrhwMJ-_cTs

### Execução (Via código fonte)

* Realize o download do código fonte através do comando: git clone https://github.com/HidroUFF/calculadora-massa-especifica
* Certifique-se de que os requisitos foram instalados corretamente.
* Sempre inicie a execução do programa através do arquivo 'main.py', pois ele é o arquivo principal.
* Sempre inicie a realização dos comandos através do diretório raiz deste projeto (diretório onde o arquivo 'main.py' está).
* O arquivo 'imagesAndFonts_rc.py' contém as imagens e fontes utilizadas pela interface, recomenda-se não alterar este arquivo para não gerar inconsistências e erros.
* Podem haver algumas diferenças na interface de sistemas operacionais distintos.

### Adição de novas substâncias

* Para a realização da adição de novas substâncias é necessário adicionar ao arquivo **substancias.csv**, presente no diretório **/data**, o nome da substância em português, inglês e espanhol. Além disso, é necessário informar massa molar(g/mol), pressão crítica(KPa), temperatura crítica (K) e fator acênctrico.
* É preciso atualizar também o arquivo **kij.csv**, presente no diretório **/data**. Kij é um parâmetro de interação entre cada par de tipos de substâncias que pode ser formado (onde interações de mesma substância é sempre 0).
* Para que a adição seja persistida, execute o programa **csvToPy.py**, que se encontra no diretório **/utility**. Este utilitário irá gerar o arquivo **constant.py**, no diretório **/src**, que será utilizado pela aplicação.
* **Atenção:**
    * Ao inserir novos elementos no arquivo **substancias.csv**, siga a mesma ordem ao adicionar as propriedades nas linhas e colunas do arquivo **kij.csv**, e vice-versa, para manter a integridade e funcionamento da calculadora.
    * Não utilize caracteres especiais, tais como '()', '[]', '@', '#', '$' etc ao dar nome às substancias.
    * É necessário ter a biblioteca 'unidecode' instalada em seu computador. Utilize o comando ```pip install unidecode``` para realizar a instalação.

## Desenvolvimento

* Desenvolvido por:
    * Mateus Pereira de Sousa 
    * Valesca Moura de Sousa 
* Orientadores:
    * Felipe Pereira de Moura
    * Fernanda Gonçalves de Oliveira Passos
    * Rogério Fernandes de Lacerda
* Data de criação: 18/08/2020
* Última revisão: 14/09/2021
* Qualquer sugestão ou dúvida sobre a aplicação, comunique um dos responsáveis.

## Citando a Calculadora de Massa Específica HidroUFF

Se a Calculadora de Massa Específica HidroUFF contribuiu para algum projeto ou pesquisa que resultou em uma publicação, por favor, cite-a.

[![DOI](https://zenodo.org/badge/322632859.svg)](https://zenodo.org/badge/latestdoi/322632859)
