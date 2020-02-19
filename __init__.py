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
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'DocReader' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import fitz
"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "read":

    path = GetParams("path")
    result = GetParams("result")
    try:
        doc = fitz.open(path)
        page = doc[0]
        text = page.getText()

        if result:
            SetVar(result, text)
    
    except Exception as e:
        PrintException()
        raise e

    


