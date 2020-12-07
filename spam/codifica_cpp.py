from playsound import playsound as ps
import spam.escucha as escucha,os
from pynput.keyboard import Key, Controller as kcontrol
from pynput.mouse import Button, Controller as mcontrol
import spam.control as control

def main():    
    codificando = True
    control.bip()
    while codificando:
        #os.system('cls')
        print(""""Codificando ...
Para salir dí "Salir del codificador\"""")
        cod = escucha.escucha()
        print(cod)
        codificando = elecciones(cod,codificando)
        del cod
        control.bip()
    del codificando

def librerias_basicas(keyboard):
    librerias = """#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
"""
    keyboard.type(librerias)
    temp = control.control_principal(0,'enter')
    temp = control.control_principal(0,'enter')
    temp = control.control_principal(0,'enter')
    del librerias
    del temp

def siif(keyboard,cod):
    codigo = cod.split()
    datos = conversionif(codigo)
    sentencia = """if (%s %s %s)%s%s"""%(datos[0],datos[1],datos[2],'{','}')
    keyboard.type(sentencia)
    temp = control.control_principal(0,'izquierda')
    temp = control.control_principal(0,'enter')
    del datos
    del codigo
    del sentencia
    del temp
    del cod

def conversionif(dato):
    print(dato)
    datos = ['cero','uno','dos']
    datos[0] = (remplazo_caracteres_especiales(dato[1]))
    lugar = 0
    for ele in dato:
        lugar += 1
        if escondicional(ele):
            datos[1] = (condicional(ele))
            break
    if dato[lugar] == 'igual' or dato[lugar] == 'o' or dato[lugar] == 'ó':
        if dato[lugar] == 'o' or dato[lugar] == 'ó':
            if dato[lugar+1] == 'igual':
                if datos[1] == '<':
                    datos[1] = '<='
                if datos[1] == '>':
                    datos[1] = '>='
                lugar += 1
        elif dato[lugar] == 'igual':
            if datos[1] == '<':
                datos[1] = '<='
            if datos[1] == '>':
                datos[1] = '>='
        lugar += 1
    if dato[lugar] == 'que' or dato[lugar] == 'qué' or dato[lugar] == 'a':
        lugar += 1
    #datos[2] = (dato[(len(dato))-1])
    datos[2] = (remplazo_caracteres_especiales(dato[lugar]))
    del dato
    del lugar
    return datos

def escondicional(dato):
    condi = False
    if dato == 'igual':
        condi = True
    elif dato == 'mayor':
        condi = True
    elif dato == 'menor':
        condi = True
    elif dato == 'diferente':
        condi = True
    del dato
    return condi

def condicional(dato):
    if dato == 'igual':
        del dato
        return '=='
    elif dato == 'mayor':
        del dato
        return '>'
    elif dato == 'menor':
        del dato
        return '<'
    elif dato == 'diferente':
        del dato
        return '!='
    

def cout(keyboard,code):
    frase = code.split()
    frase.pop(0)
    print(frase)
    imprimir = 'cout<<'
    conc = False
    i = 0
    while i < len(frase):
        print(f'{i} menor {len(frase)}')
        cambiado = False
        if frase[i] == 'concatena' or frase[i] == 'concatenar':
            conc = True
            cambiado = True
        if not conc:
            imprimir += '"'+frase[i]+'"'
        else:
            if not cambiado:
                if not (frase[i] == 'con' or frase[i] == 'a'):
                    if ((frase[i] =='end' or frase[i] =='en') and frase[i+1] =='line') or (frase[i] =='salto' and frase[i+1] =='línea'):
                        imprimir += f'<<endl'
                        conc = False
                        i += 1
                    elif (frase[i] =='salto' and frase[i+1] =='de' and frase[i+2] =='línea'):
                        imprimir += f'<<endl'
                        conc = False
                        i += 2
                    else:
                        imprimir += f'<<{remplazo_caracteres_especiales(frase[i])}'
                        conc = False
                try:
                    if not ((frase[i+1] == 'concatena') or (frase[i+1] == 'concatenar')):
                        imprimir += '<<'
                except:
                    pass
        i += 1
    del conc
    imprimir += ';'
    imprimir = imprimir.replace('""',' ')
    keyboard.type(imprimir)
    del imprimir
    del i
    del keyboard
    del code

def remplazo_caracteres_especiales(palabra):
    dic = {
        'ñ': 'n',
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    for i, j in dic.items(): 
        palabra = palabra.replace(i, j)
    del dic
    return palabra

def funcion_main(keyboard):
    keyboard.type("""int main(){
system("pause");
return 0;
}""")
    temp = control.control_principal(0,'inicio')
    temp = control.control_principal(0,'arriba')
    temp = control.control_principal(0,'tab')
    temp = control.control_principal(0,'inicio')
    temp = control.control_principal(0,'arriba')
    temp = control.control_principal(0,'tab')
    temp = control.control_principal(0,'inicio')
    temp = control.control_principal(0,'arriba')
    temp = control.control_principal(0,'fin')
    temp = control.control_principal(0,'enter')
    temp = control.control_principal(0,'tab')
    del temp


def ayuda():
    pass

def elecciones(cod,codificando):
    keyboard = kcontrol()
    if cod == 'librerias basicas' or cod == 'librerías básicas':
        librerias_basicas(keyboard)
    if cod == 'función main' or cod == 'función principal':
        funcion_main(keyboard)
    if cod[:3] == 'si ' or cod[:3] == 'sí ' or cod[:3] == 'if ':
        siif(keyboard,cod)
    if cod[:8] == 'escribe ' or cod[:7] == 'salida ' or cod[:8] == 'imprime ' or cod[:9] == 'escribir ' or cod[:9] == 'imprimir ':
        cout(keyboard,cod)
    if cod == 'ayuda':
        ayuda()
    if (cod.split())[0] == 'control':
        control.control_principal(20,cod[8:])
    if 'dormir' in cod or 'sleep' in cod or 'duerme' in cod or 'duermete' in cod:
            control.dormir(cod)
    if cod == 'salir del codificador':
        codificando = False
    del keyboard
    return codificando
