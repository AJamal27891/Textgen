# Textgen
Text generating application using different input sources CSV text and Json powered by [GPT-2 opent AI](https://openai.com/blog/better-language-models/). 

## Download instructions 
  > __Download and setup python environment :__ 
  
    - [Download python 3.6](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe)
    - Excute python-3.6.0-amd64.exe
    - To make sure it worked CMD type `python`. 
  > __Building a vertual env :__
  
     - type the following command in the CMD `c:\>python -m venv myenv c:\path\to\myenv`
     - Navigate to the `env\Scripts\activate`
  > __Download requirements :__
  
      - Navigate to the project folder and type ` pip install -r rquirements.txt`
      - pip install tensorflow==2.1

  > __Finally :__ navigate to the project folder run `python app.py`

## Project interface 
  > __Model options :__
    
      - Model size [ small = 117M , Medium = 325M, Large = 775M, extra larb= 15B]
      - Text size [the lenth of the generated output ]
      - Number of samples [ the number of samples needed to be generated ] 
      - click submit button to confirm the entry 
  > __Input Options :__ 
  
    - Input type [ CSV, TXT, textbox , Web ] 
    - select or clear input type
    - Click submit to get the output 
  > __Preview :__ 
 
    - preview frame to preview output after click select 
 
  >__Outuput :__ 
  
    - display the text generated from the entries. 
