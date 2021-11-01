<div align='center'>
  <img align="center" alt="Logo" height="100" width="100" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/icon.ico">
</div>  

<h1 align="center">Calculadora de Massa Específica HidroUFF</h1>

<p align="center">
  Esta aplicação tem como funcionalidade principal o cálculo da massa especifica de misturas gasosas, através da resolução da equação de estado cúbica de Peng Robinson. Atualmente, existem na ferramenta 20 substâncias já cadastradas e suporte para adição de novas substâncias pelo usuário. Além disso, a ferramenta possui interface nos idiomas inglês, português e espanhol.
</p> 

<p align="center"><strong>Versão 1.3.0</strong></p>

<p align="center">
 <a href="#use">Como utilizar</a> •
 <a href="#exe">Execução via arquivo executável</a> •
 <a href="#code">Execução via código fonte</a> •
 <a href="#guidelines">Orientações Gerais</a> • 
 <a href="#add">Adição de substâncias</a> • 
 <a href="#demonstration">Demonstração</a> • 
 <a href="#technologies">Tecnologia</a> •
 <a href="#author">Desenvolvimento</a> • 
 <a href="#quoting">Citando</a>
</p>

<h2 id="use" align="justify">Como utilizar</h2>
<p align="justify">
  Para utilizar a aplicação basta informar a fração molar de cada substância que compõe a mistura, a temperatura em ATM, e o valor de pressão. A pressão pode ter um único valor ou uma faixa de valores. Para tal, informe os valores inicial, final e o passo entre eles. Ao realizar o cálculo para uma faixa de valores de pressão é possível gerar o gráfico da Isoterma ou salvar o resultado em um arquivo .csv (comma-separated values). Este arquivo pode ser utilizado posteriormente para gerar o gráfico diretamente, sem a necessidade de nova realização dos cálculos. Para utilizar esta funcionalidade conserve o formato original do arquivo, alterando apenas valores numéricos, se necessário.
</p> 

<h2 id="exe" align="justify">Execução via arquivo executável</h2>
<p align="justify">
  <li>
    Basta realizar o download do arquivo <strong>Calculadora de Massa Específica HidroUFF.exe</strong>, que se encontra no diretório /bin, e executá-lo. Não é necessário realizar qualquer instalação. 
  </li>
  <li>
    O arquivo executável é compatível apenas com o sistema operacional Windows. 
  </li>
</p> 

<h2 id="code" align="justify">Execução via código fonte</h2>
<h3 align="justify">Pré-requisitos</h3>

* Python 3.x
* Pip

Após a instalação da linguagem Python e do instalador de pacotes pip, instale as seguintes dependências através do terminal:
* Sympy

```
pip install sympy
```

* Matplotlib

```
pip install matplotlib
```

* PyQt5

```
pip install PyQt5
```
<h3 align="justify">Execução</h3>
<p align="justify">
  <li>
    Realize o download do código fonte através do comando: git clone https://github.com/HidroUFF/calculadora-massa-especifica
  </li>
  <li>
    Certifique-se de que os requisitos foram instalados corretamente. 
  </li>
  <li>
    Sempre inicie a execução do programa através do arquivo 'main.py', pois ele é o arquivo principal.
  </li>
  <li>
    Sempre inicie a realização dos comandos através do diretório raiz deste projeto (diretório onde o arquivo 'main.py' está).
  </li>
  <li>
    O arquivo 'imagesAndFonts_rc.py' contém as imagens e fontes utilizadas pela interface, recomenda-se não alterar este arquivo para não gerar inconsistências e erros.
  </li>
  <li>
    Podem haver algumas diferenças na interface de sistemas operacionais distintos. 
  </li>
</p> 


<h2 id="guidelines" align="justify">Orientações gerais</h2>

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


<h2 id="add" align="justify">Adição de novas substâncias</h2>
Para a realização da adição de novas substâncias é necessário primeiro seguir os passos indicados em <a href="#code">Execução via código fonte</a>. Após isso, siga o passo a passo: 

* Adicione ao arquivo **substancias.csv**, presente no diretório **/data**, o nome da substância em português, inglês e espanhol. Além disso, é necessário informar massa molar(g/mol), pressão crítica(KPa), temperatura crítica (K) e fator acênctrico.
* É preciso atualizar também o arquivo **kij.csv**, presente no diretório **/data**. Kij é um parâmetro de interação entre cada par de tipos de substâncias que pode ser formado (onde interações de mesma substância é sempre 0).
* Para que a adição seja persistida, execute o programa **csvToPy.py**, que se encontra no diretório **/utility**. Este utilitário irá gerar o arquivo **constant.py**, no diretório **/src**, que será utilizado pela aplicação.
* **Atenção:**
    * Ao inserir novos elementos no arquivo **substancias.csv**, siga a mesma ordem ao adicionar as propriedades nas linhas e colunas do arquivo **kij.csv**, e vice-versa, para manter a integridade e funcionamento da calculadora.
    * Não utilize caracteres especiais, tais como '()', '[]', '@', '#', '$' etc ao dar nome às substancias.
    * É necessário ter a biblioteca 'unidecode' instalada em seu computador. Para realizar a instalação, utilize o comando: 
 
 ```
 pip install unidecode
 ``` 
 
<h2 id="technologies" align="justify">Tecnologia</h2>
<div align="center">
  <img align="center" alt="Python" height="50" width="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Qt" height="50" width="50" src="https://github.com/devicons/devicon/blob/master/icons/qt/qt-original.svg">
 </div>

* Python - versão 3
* Bibliotecas python:
  * PyQt5
  * Sympy
  * Matplotlib
  

<h2 id="demonstration" align="justify">Demonstração</h2>

* Informe a composição e temperatura desejadas.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/input.PNG">
</div>

* Se deseja calcular a massa específica para uma única pressão, escolha a opção **Única**, informe o valor desejado e clique em **Calcular**. O resultado será exibido na tela.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/single.PNG">
</div>

* Caso deseje calcular a massa específica para um intervalo de valores de pressão, escolha a opção **Intervalo**, informe o valor inicial, final e o passo entre eles e clique no botão **Gráfico da Isoterma** para obter um gráfico ou no botão **Gerar CSV** para salvar os resultados dos cálculos em um arquivo de extensão CSV.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/range.PNG">
</div>

* Exemplo de gráfico.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/isothermGraph.PNG">
</div>

* Exemplo de arquivo CSV.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/csv.PNG">
</div>

* É possível modificar o idioma através do botão inferior esquerdo, basta clicar para alternar entre inglês, espanhol e português. Além disso, existem três botões superiores no lado direito da interface que servem, respectivametente, para gerar gráfico da isoterma a partir de arquivo CSV previamente gerado pela aplicação, consultar ajuda e obter mais informações sobre o programa.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/menu.PNG">
</div>

<h2 id="author" align="justify">Desenvolvimento</h2>

* Desenvolvido por:
    * Mateus Pereira de Sousa 
    * Valesca Moura de Sousa
* Orientadores:
    * Felipe Pereira de Moura
    * Fernanda Gonçalves de Oliveira Passos
    * Rogério Fernandes de Lacerda
* <a href="http://hidrouff.sites.uff.br/">Laboratório HidroUFF</a>
* Data de criação: 18/08/2020
* Última revisão: 14/09/2021
* Qualquer sugestão ou dúvida sobre a aplicação, comunique um dos responsáveis.


<h2 id="quoting" align="justify">Citando</h2>
Se a Calculadora de Massa Específica HidroUFF contribuiu para algum projeto ou pesquisa que resultou em uma publicação, por favor, cite-a.

<div align="center"> 
  
  [![DOI](https://zenodo.org/badge/322632859.svg)](https://zenodo.org/badge/latestdoi/322632859)
  
</div>