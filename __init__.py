# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import traceback
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'DocReader' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32:
    sys.path.append(cur_path_x64)
else:
    sys.path.append(cur_path_x86)

import fitz

"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

try:

    if module == "read":

        path = GetParams("path")
        result = GetParams("result")
        page = GetParams("page")
        option = GetParams("option")
        
        doc = fitz.open(path)
        page = doc[int(page) - 1]

        if option == "1":
            fText = page.getText().replace('\ufb01',"fi")

        elif option == "2":
            text = page.getTextWords()
            position_in_y = []
            text_array = []
            
            for e in text:
                space = (e[2] - e[0] )/ len(e[4])
                if e[1] in position_in_y:
                    i = position_in_y.index(e[1])
                    text_position = round(e[0]/space)
                    text = text_array[i]
                    if (text_position < len(text)):
                        text = text[: text_position] + e[4] + text[text_position + len(e[4]):]
                        print(text)
                    else:
                        text += " "*(text_position - len(text)) + e[4]
                        print(text)
                        
                    text_array[i] = text
                else:                    
                    position_in_y.append(e[1])
                    position_in_y.sort()
                    text_array.insert(position_in_y.index(e[1]),e[4])

            fText = "\n".join(text_array)
    

        if result:
            SetVar(result, fText)
        


        
    if module == "readPDF":
        path = GetParams("path")
        result = GetParams("result")

        import subprocess
        
        binpath = base_path + 'modules' + os.sep + 'DocReader' + os.sep + 'bin' + os.sep
        
        res = subprocess.Popen([binpath + 'test.exe', path], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
        
        SetVar(result, res[0].decode())

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e