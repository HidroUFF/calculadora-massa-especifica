<div align='center'>
  <img align="center" alt="Logo" height="100" width="100" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/icon.ico">
</div>  

<h1 align="center">HidroUFF Density Calculator</h1>

<p align="center">
  This application's main feature is the calculation of the density of gas mixtures, through the resolution of Peng Robinson's cubic equation of state. Currently, there are 20 substances already registered in the tool and support for adding new substances by the user. In addition, the tool has an interface in English, Portuguese and Spanish.
</p> 

<p align="center"><strong>Version 1.3.0</strong></p>

<p align="center">
 <a href="#use">How to use</a> •
 <a href="#exe">Execution via executable file</a> •
 <a href="#code">Execution via source code</a> •
 <a href="#guidelines">General orientations</a> • 
 <a href="#add">Addition of substances</a> • 
 <a href="#demonstration">Demonstration</a> • 
 <a href="#technologies">Technology</a> •
 <a href="#author">Development</a> • 
 <a href="#quoting">Quoting</a>
</p>

<h2 id="use" align="justify">How to use</h2>
<p align="justify">
  To use the application, just inform the molar fraction of each substance that makes up the mixture, the temperature in ATM, and the pressure value. Pressure can be a single value or a range of values. To do so, inform the initial, final and step values between them. When performing the calculation for a range of pressure values, it is possible to generate the Isotherm graph or save the result in a .csv (comma-separated values) file. This file can be used later to generate the graph directly, without the need to perform the calculations again. To use this feature, keep the original file format, changing only numeric values if necessary.
</p> 

<h2 id="exe" align="justify">Execution via executable file</h2>
<p align="justify">
  <li>
    Just download the <strong>Calculadora de Massa Específica HidroUFF.exe</strong> file, located in the /bin directory, and run it. No installation is required.
  </li>
  <li>
    The executable file is only compatible with Windows operating system.
  </li>
</p> 

<h2 id="code" align="justify">Execution via source code</h2>
<h3 align="justify">Requirements</h3>

* Python 3.x
* Pip

After installing the Python language and the pip package installer, install the following dependencies through the terminal:

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
<h3 align="justify">Execution</h3>
<p align="justify">
  <li>
    Download the source code using the command: git clone https://github.com/HidroUFF/calculadora-massa-especifica
  </li>
  <li>
    Make sure the requirements are installed correctly. 
  </li>
  <li>
    Always start the program execution via the 'main.py' file, as this is the main file.
  </li>
  <li>
    Always start the execution of the commands through the root directory of this project (directory where the file 'main.py' is).
  </li>
  <li>
    The file 'imagesAndFonts_rc.py' contains the images and fonts used by the interface, it is recommended not to change this file so as not to generate inconsistencies and errors.
  </li>
  <li>
    There may be some differences in the interface of different operating systems.
  </li>
</p> 


<h2 id="guidelines" align="justify">General orientations</h2>

* The sum of the molar fractions must equal 1.0.
* Use period (.) as decimal separator.
* Do not use thousands separator.
* The .csv file must be separated by a semicolon (;).
* Do not modify the header of the .csv file as it is used by the program. If modified, it can lead to errors in reading the file and generating the graph from it.
    * The keywords used in certain lines to identify each column must not have any of its letters altered.
    * File structure:
        * First key line: Composition
        * Second key line: Substance; Molar Fraction (remembering that ; separates the columns of the file)
        * Below are registered names of selected substances in the first column and the molar fraction of these substances in the second column. E.g.: CO2;1.0
        * Third key line: Temperature
        * Below will be registered some temperature value in Kelvin. E.g.: 100.0
        * Fourth key line: Density
        * Fifth key line: atm;kg/m³
        * Below are recorded pressure and density values. E.g.: 1e-08;1533.491


<h2 id="add" align="justify">Addition of new substances</h2>
To carry out the addition of new substances, it is first necessary to follow the steps indicated in <a href="#code">Execution via source code</a>. After that, follow the step by step:

* Add to the **substancias.csv** file, present in the **/data** directory, the name of the substance in Portuguese, English and Spanish. In addition, it is necessary to inform molar mass (g/mol), critical pressure (KPa), critical temperature (K) and acentric factor.
* It is also necessary to update the **kij.csv** file, present in the **/data** directory. Kij is an interaction parameter between each pair of substance types that can be formed (where interactions of the same substance is always 0).
* In order for the addition to be persisted, run the **csvToPy.py** program, which is located in the **/utility** directory. This utility will generate the **constant.py** file, in the **/src** directory, which will be used by the application.
* **Attention:**
    * When inserting new elements in the **substancias.csv** file, follow the same order when adding the properties in the rows and columns of the **kij.csv** file, and vice versa, to maintain the integrity and functioning of the calculator .
    * Do not use special characters such as '()', '[]', '@', '#', '$' etc when naming substances.
    * You must have the 'unidecode' library installed on your computer. To perform the installation, use the command: 
 
 ```
 pip install unidecode
 ``` 
 
<h2 id="technologies" align="justify">Technology</h2>
<div align="center">
  <img align="center" alt="Python" height="50" width="50" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Qt" height="50" width="50" src="https://github.com/devicons/devicon/blob/master/icons/qt/qt-original.svg">
 </div>

* Python - version 3
* Python libraries:
  * PyQt5
  * Sympy
  * Matplotlib
  

<h2 id="demonstration" align="justify">Demonstration</h2>

* Enter the desired composition and temperature.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/input.PNG">
</div>

* If you want to calculate the specific mass for a single pressure, choose the **Single** option, enter the desired value and click on **Calculate**. The result will be displayed on the screen.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/single.PNG">
</div>

* If you want to calculate the specific mass for a range of pressure values, choose the **Range** option, enter the initial and final value and the step between them and click on the **Isotherm Graph** button to obtain a graph or the **Generate CSV** button to save the calculation results to a CSV file extension.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/range.PNG">
</div>

* Graph example.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/isothermGraph.PNG">
</div>

* Example CSV file.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/csv.PNG">
</div>

* It is possible to change the language through the lower left button, just click to switch between English, Spanish and Portuguese. In addition, there are three upper buttons on the right side of the interface that serve, respectively, to generate a graph of the isotherm from a CSV file previously generated by the application, consult help and obtain more information about the program.
<div align="center">
  <img align="center" src="https://raw.githubusercontent.com/HidroUFF/calculadora-massa-especifica/main/assets/menu.PNG">
</div>

<h2 id="author" align="justify">Development</h2>

* Developed by:
    * Mateus Pereira de Sousa 
    * Valesca Moura de Sousa
* Advisors:
    * Felipe Pereira de Moura
    * Fernanda Gonçalves de Oliveira Passos
    * Rogério Fernandes de Lacerda
* <a href="http://hidrouff.sites.uff.br/">HidroUFF Laboratory</a>
* Creation date: 08/18/2020
* Last revised: 09/14/2021
* Any suggestions or questions about the application, communicate one of the responsible.


<h2 id="quoting" align="justify">Quoting</h2>
If the HidroUFF Specific Mass Calculator contributed to any project or research that resulted in a publication, please cite it.

<div align="center"> 
  
  [![DOI](https://zenodo.org/badge/322632859.svg)](https://zenodo.org/badge/latestdoi/322632859)
  
</div>