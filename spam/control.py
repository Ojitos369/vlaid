from main import mostrar_codigo
from playsound import playsound as ps
import spam.escucha as escucha,os
from time import sleep
from pynput.keyboard import Key, Controller as kcontrol
from pynput.mouse import Button, Controller as mcontrol

def control():
    controlando = True
    sensibilidad = 20
    #ayuda_control()
    bip()
    while controlando:
        bip()
        os.system('cls')
        print("""Control...
para salir dí "salir de control\"""")
        control = escucha.escucha()
        control = control.lower()
        control = correccion_palabras(control)
        sensibilidad,controlando = control_principal(sensibilidad, control)
        del control
    bip()
    del(controlando)
    del(sensibilidad)

def control_opciones(keyboard,mouse,control):
    print('entro a control')
    if control == 'control click' or control == 'control pulsar' or control == 'control pulsa':
        keyboard.press(Key.ctrl)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.release(Key.ctrl)
    elif control == 'control f1':
        keyboard.press(Key.ctrl)
        keyboard.press(Key.f1)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.f1)
    elif control == 'control g':
        keyboard.press(Key.ctrl)
        keyboard.press('g')
        keyboard.release(Key.ctrl)
        keyboard.release('g')
    elif control == 'control borrado permanente':
        keyboard.press(Key.shift)
        keyboard.press(Key.delete)
        keyboard.release(Key.shift)
        keyboard.release(Key.delete)
    del keyboard
    del mouse
    del control

def ventanas_opciones(keyboard,control):
    if  control == 'ventanas abiertas' or control == 'ventanas activas' or control == 'ventanas activas':
        keyboard.press(Key.ctrl)
        keyboard.press(Key.alt)
        keyboard.press(Key.tab)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.alt)
        keyboard.release(Key.tab)
    if control == 'nueva ventana' or control == 'ventana nueva':
        keyboard.press(Key.ctrl)
        keyboard.press('n')
        keyboard.release(Key.ctrl)
        keyboard.release('n')
    if control == 'cerrar ventana':
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
        keyboard.release(Key.alt)
        keyboard.release(Key.f4)
    if control == 'maximizar ventana':
        keyboard.press(Key.alt)
        keyboard.press(Key.shift)
        keyboard.press(Key.space)
        keyboard.release(Key.alt)
        keyboard.release(Key.shift)
        keyboard.release(Key.space)
        keyboard.press('x')
        keyboard.release('x')
    del keyboard
    del control

def general_opciones(keyboard,mouse,control):
    separado = control.split()
    cantidad = 0
    if control == 'copiar' or control == 'copia':
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release(Key.ctrl)
        keyboard.release('c')
    elif control == 'pegar' or control == 'pega':
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release(Key.ctrl)
        keyboard.release('v')
    elif control == 'cortar' or control == 'corta':
        keyboard.press(Key.ctrl)
        keyboard.press('x')
        keyboard.release(Key.ctrl)
        keyboard.release('x')
    elif control == 'anterior' or control == 'deshacer':
        keyboard.press(Key.ctrl)
        keyboard.press('z')
        keyboard.release(Key.ctrl)
        keyboard.release('z')
    elif  control == 'busqueda' or control == 'buscar':
        keyboard.press(Key.alt)
        keyboard.press('d')
        keyboard.release(Key.alt)
        keyboard.release('d')
    elif 'suprimir' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.delete)
                    keyboard.release(Key.delete)
                    cantidad -= 1
            else:
                keyboard.press(Key.delete)
                keyboard.release(Key.delete)
        except:
            keyboard.press(Key.delete)
            keyboard.release(Key.delete)
    elif 'borrar' in control or 'borra' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                    cantidad -= 1
            else:
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
        except:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
    elif 'arriba' in control or 'subir' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    cantidad -= 1
            else:
                keyboard.press(Key.up)
                keyboard.release(Key.up)
        except:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
    elif 'abajo' in control or 'bajar' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    cantidad -= 1
            else:
                keyboard.press(Key.down)
                keyboard.release(Key.down)
        except:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
    elif 'izquierda' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    cantidad -= 1
            else:
                keyboard.press(Key.left)
                keyboard.release(Key.left)
        except:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
    elif 'derecha' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    cantidad -= 1
            else:
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        except:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
    elif 'espacio' in control:
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.space)
                    keyboard.release(Key.space)
                    cantidad -= 1
            else:
                keyboard.press(Key.space)
                keyboard.release(Key.space)
        except:
            keyboard.press(Key.space)
            keyboard.release(Key.space)
    elif ('tabulacion' in control) or ('tabulación' in control) or ('tab' in control):
        try:
            if separado[1] == 'por' or separado[1] == '*':
                cantidad = int(conversor_num(separado[2]))
                while cantidad > 0:
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    cantidad -= 1
            else:
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
        except:
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
    elif control == 'inicio' or control == 'home':
        keyboard.press(Key.home)
    elif control == 'guardar':
        keyboard.press(Key.ctrl)
        keyboard.press('s')
        keyboard.release(Key.ctrl)
        keyboard.release('s')
    elif control == 'final' or control == 'fin':
        keyboard.press(Key.end)
        keyboard.release(Key.end)
    elif control == 'siguiente' or control == 'rehacer':
        keyboard.press(Key.ctrl)
        keyboard.press('y')
        keyboard.release(Key.ctrl)
        keyboard.release('y')
    elif control == 'enter' or control == 'aceptar':
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif control == 'cancelar':
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
    elif control=='posicion' or control=='posición':
        print(mouse.position)

    del keyboard
    del cantidad
    del separado
    del mouse
    del control

def click_opciones(mouse,control):
    separado = control.split()
    print(separado)
    sleep(5)
    if separado[0]=='click' or separado[0]=='pulsar' or separado[0]=='pulsa':
        try:
            if separado[1] == 'por' or separado[1] == '*':
                veces = int(conversor_num(separado[2]))
                mouse.click(Button.left, veces)
                del veces
        except:
            pass
    if control=='click' or control=='pulsar' or control=='pulsa':
        mouse.click(Button.left, 1)
    if control=='click derecho' or control=='pulsar derecho' or control=='pulsa derecho':
        mouse.click(Button.right, 1)
    if control=='doble pulsar' or control=='doble click':
        mouse.click(Button.left, 2)
    if control=='doble pulsar derecho' or control=='doble click derecho':
        mouse.click(Button.right, 2)
    if control=='presionar' or control=='presiona':
        mouse.press(Button.left)
    if control=='presionar derecho' or control=='presiona derecho':
        mouse.press(Button.right)
    if control=='soltar' or control=='suelta':
        mouse.click(Button.left, 1)
    if control=='soltar derecho' or control=='suelta derecho':
        mouse.click(Button.right, 1)
    del mouse
    del control

def correccion_texto_pulsar(control):
    dic = {
        'doble postal':'doble pulsar',
        'doublepulsar':'doble pulsar',
        'google pulsar':'doble pulsar',
        'google play':'doble click',
        'dobleclick':'doble click',
    }
    for i, j in dic.items(): 
        control = control.replace(i, j)
    del dic
    if 'mover a' in control:
        if not (('mover arriba' in control) or ('mover abajo' in control)):
            control = control.replace('mover a','mover')
    return control

def seleccionar_opciones(keyboard,control):
    if control == 'seleccionar todo' or control == 'selecciona todo':
        keyboard.press(Key.ctrl)
        keyboard.press(Key.end)
        keyboard.release(Key.end)
        keyboard.press(Key.shift)
        keyboard.press(Key.home)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.home)
    if control == 'seleccionar renglon' or control == 'selecciona renglon' or control == 'seleccionar renglón' or control == 'selecciona renglón' or control == 'seleccionar linea' or control == 'selecciona linea' or control == 'seleccionar línea' or control == 'selecciona línea':
        keyboard.press(Key.end)
        keyboard.release(Key.end)
        keyboard.press(Key.shift)
        keyboard.press(Key.home)
        keyboard.release(Key.shift)
        keyboard.release(Key.home)
    del keyboard
    del control

def pestanias_opciones(keyboard,control):
    if len(control) < 15:
        pestania = control.split()
        try:
            no_pestania = str(conversor_num(pestania[1]))
            keyboard.press(Key.ctrl)
            keyboard.press(no_pestania)
            keyboard.release(Key.ctrl)
            keyboard.release(no_pestania)
            del no_pestania
        except:
            pass
        del pestania
    if control == 'cerrar pestaña':
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release(Key.ctrl)
        keyboard.release('w')
    if control == 'nueva pestaña' or control == 'pestaña nueva':
        keyboard.press(Key.ctrl)
        keyboard.press('t')
        keyboard.release(Key.ctrl)
        keyboard.release('t')
    if control == 'pestaña siguiente' or control == 'siguiente pestaña':
        keyboard.press(Key.ctrl)
        keyboard.press(Key.tab)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.tab)
    if control == 'pestaña anterior' or control == 'anterior pestaña':
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.press(Key.tab)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.tab)
    del keyboard
    del control

def sensibilidad_opciones(sensibilidad,control):
    sensi = control.split()
    if control == 'muestra sensibilidad':
        print(sensibilidad)
    try:
        if sensi[2] == 'por' or sensi[2] == '*':
            modifi = int(conversor_num(sensi[3]))
            if sensi[0] == 'mas' or sensi[0] == 'más':
                sensibilidad += modifi*10
            elif sensi[0] == 'menos':
                sensibilidad -= modifi*10
            del modifi
        else:
            if sensi[0] == 'configura':
                sensibilidad = int(conversor_num(sensi[2]))
    except:
        if sensi[0] == 'mas' or sensi[0] == 'más':
            sensibilidad += 10
        elif sensi[0] == 'menos':
            sensibilidad -= 10
    if sensibilidad < 1:
        sensibilidad = 1
    del sensi
    del control
    return sensibilidad

def scroll(mouse,control):
    separado = control.split()
    try:
        if separado[2] == 'por' or separado[2] == '*':
            num = int(conversor_num(separado[3]))
            if separado[1] == 'arriba' or separado[1] == 'subir':
                mouse.scroll(0, num)
            if separado[1] == 'abajo' or separado[1] == 'bajar':
                mouse.scroll(0, -num)
            if separado[1] == 'derecha':
                mouse.scroll(num, 0)
            if separado[1] == 'izquierda':
                mouse.scroll(-num, 0)
        else:
            if separado[1] == 'arriba' or separado[1] == 'subir':
                mouse.scroll(0, 2)
            if separado[1] == 'abajo' or separado[1] == 'bajar':
                mouse.scroll(0, -2)
            if separado[1] == 'derecha':
                mouse.scroll(2, 0)
            if separado[1] == 'izquierda':
                mouse.scroll(-2, 0)
    except:
        if separado[1] == 'arriba' or separado[1] == 'subir':
            mouse.scroll(0, 1)
        elif separado[1] == 'abajo' or separado[1] == 'bajar':
            mouse.scroll(0, -1)
        elif separado[1] == 'derecha':
            mouse.scroll(1, 0)
        elif separado[1] == 'izquierda':
            mouse.scroll(-1, 0)
    del mouse
    del separado
    del control


def mover_opciones(sensibilidad,mouse,control):
    try:
        if 'coma' in control:
            control = control.replace('coma',' ')
        control = control.replace(',',' ')
        control = control.replace('+',' ')
        control = control.replace('-',' ')
        posicion = control.split()
        print(posicion)
        try:
            x = int(posicion[1])
            y = int(posicion[2])
            mouse.position = (x,y)
            del x
            del y
        except:
            try:
                if posicion[1] == 'abajo':
                    try:
                        if posicion[2] == 'por':
                            num = int(conversor_num(posicion[3]))*sensibilidad
                            mouse.move(0, num)
                            del num
                        else:
                            mouse.move(0, sensibilidad)
                    except:
                        mouse.move(0, sensibilidad)
                if posicion[1] == 'arriba':
                    try:
                        if posicion[2] == 'por':
                            num = int(conversor_num(posicion[3]))*sensibilidad
                            mouse.move(0, -num)
                            del num
                        else:
                            mouse.move(0, -sensibilidad)
                    except:
                        mouse.move(0, -sensibilidad)
                if posicion[1] == 'izquierda':
                    try:
                        if posicion[2] == 'por':
                            num = int(conversor_num(posicion[3]))*sensibilidad
                            mouse.move(-num, 0)
                            del num
                        else:
                            mouse.move(-sensibilidad, 0)
                    except:
                        mouse.move(-sensibilidad, 0)
                if posicion[1] == 'derecha':
                    try:
                        if posicion[2] == 'por':
                            num = int(conversor_num(posicion[3]))*sensibilidad
                            mouse.move(num, 0)
                            del num
                        else:
                            mouse.move(sensibilidad, 0)
                    except:
                        mouse.move(sensibilidad, 0)
            except:
                pass
        del posicion
    except:
        print('Orden mal indicada')
    del sensibilidad
    del mouse
    del control

def dormir(control):
    frase = control.split()
    if 'dormir' in frase[0] or 'sleep' in frase[0] or 'duerme' in frase[0] or 'duermete' in frase[0]:
        try:
            try:
                num = int(conversor_num(frase[2]))
                while num > 0:
                    sleep(1)
                    os.system("cls")
                    print(f'{num} para despertar')
                    num -= 1
                del num
            except:
                num = int(conversor_num(frase[1]))
                while num > 0:
                    sleep(1)
                    print(f'{num} para despertar')
                    num -= 1
                del num
        except:
            sleep(10)
    del frase
    del control

def lista_ordenes(sensibilidad,control):
    
    del control
    del sensibilidad

def bip():
    ps('./audios/bip.mp3')

def correccion_palabras(text):
    dic = {' sientos': '00',
        ' siento': '00',
        'craigslist pierda':  'izquierda',
        'escarabajo':  'abajo',
        'trabajo':  'abajo',
        'trabajó':  'abajo',
        'gral': 'scroll',
        'canal': 'scroll',
        'scrolling': 'scroll',
        'crush': 'scroll',
        'scroll': 'scroll',
        'skrull': 'scroll',
        'scrabble': 'scroll',
        'moder': 'mover',
        'mabel': 'mover',
        'va a ver': 'mover',
        'mover o': 'mover',
        'controló': 'control',
        'controlo': 'control',
    }
    for i, j in dic.items(): 
        text = text.replace(i, j)
    del dic
    if 'mover a' in text:
        if not (('mover arriba' in text) or ('mover abajo' in text)):
            text = text.replace('mover a','mover')
    return text

def conversor_num(text):
    if text == 'cero':
        text = '0'
    elif text == 'uno':
        text = '1'
    elif text == 'dos':
        text = '2'
    elif text == 'tres':
        text = '3'
    elif text == 'cuatro':
        text = '4'
    elif text == 'cinco':
        text = '5'
    elif text == 'seis':
        text = '6'
    elif text == 'siete':
        text = '7'
    elif text == 'ocho':
        text = '8'
    elif text == 'nueve':
        text = '9'
    elif text == 'diez':
        text = '10'
    elif text == 'díaz':
        text = '10'
    elif text == 'días':
        text = '10'
    return text

def ayuda_control():
    instrucciones = """
        Escribe: Escribe lo que deigas acontinuacion.
            Ejemplo: Escribe hola buenas tarde:
                Escribira: buenas tardes
        Ventanas abiertas: Muestra las ventanas que tienes abiertas
        Enter: Pulsa enter
        Tabulacion/tab: Pulsa tabulacion
        Cancelar: Pulsa esc
        Posicion: Muestra la posicion del cursor
        Click/pulsar: click simple izquierdo
        Click/pulsar derecho: click simple derecho
        Doble click: Doble click izquierdo
        Doble click derecho: Doble click derecho
        Presionar: Mantiene pulsado el boton izquierdo
        Soltar: Deja de mantener pulsado el boton izquierdo
        Presionar derecho: Mantiene pulsado el boton derecho
        Soltar derecho: Deja de mantener pulsado el boton derecho
        Mover: Mueve el cursor
            Muestra sensibilidad: Muestra la sensibilidad con la que se mueve el cursor
            Mas/menos sensibilidad: aumenta o disminuye la sensibilidad en 10:
                mas/menos sensibilidad por n: aumenta o disminuye la sensibilidad en 10n; siendo n un numero
            configura sensibilidad n: configura la sensibilidad al n indicado; siendo n un numero
            Mover x coma/,/- y: mueve el cursor a la cantidad de pixeles indicados:
                Ejemplo: mueve 0 coma 0:
                    movera el cursor al inicio de la pantalla (derecha, arriba)
            Mover arriba/abajo/derecha/izquierda: Movera a la direccion indicada de acuerdo a la sensibilidad configurada
        Copiar: ctrl+c
        Pegar: ctrl+v
        Cortar: ctrl+x
        Regresar: ctrl+z
        Siguiente/Avanzar: ctrl+y

        salir de control: Sale de control
    """
    leyendo = True
    while leyendo:
        os.system('cls')
        print(instrucciones)
        print('Cuando termine de leer diga "Listo"')
        if (escucha.escucha())=='listo':
            leyendo = False
    del leyendo
    del instrucciones

def control_principal(sensibilidad,control):
    controlando = True
    mouse = mcontrol()
    keyboard = kcontrol()
    if 'escribe' in control or 'escribir' in control:
            control = control[8:]
            keyboard.type(control)
    else:
        control = correccion_palabras(control)
        control = correccion_texto_pulsar(control)
        controlseparado = control.split()        
        if controlseparado[0] == 'control':
            control_opciones(keyboard,mouse,control)
        if control == 'ayuda':
            ayuda_control()
        if controlseparado[0] == 'dormir' or controlseparado[0] == 'sleep' or controlseparado[0] == 'duerme' or controlseparado[0] == 'duermete':
            dormir(control)
        if conversor_num(controlseparado[0]) == '1':
            lista_ordenes(sensibilidad,controlseparado)
        elif controlseparado[0] == 'click' or controlseparado[0] == 'pulsar' or controlseparado[0] == 'pulsa' or controlseparado[0] == 'presionar' or controlseparado[0] == 'presiona' or controlseparado[0] == 'suelta' or controlseparado[0] == 'soltar':
            click_opciones(mouse,control)
        elif 'click' in control or 'pulsar' in control:
            click_opciones(mouse,control)
        elif 'sensibilidad' in control:
            sensibilidad = sensibilidad_opciones(sensibilidad,control)
        elif 'ventana' in control:
            ventanas_opciones(keyboard,control)
        elif 'seleccionar' in control:
            seleccionar_opciones(keyboard,control)
        elif control == 'muéstrame tu código' or control == 'mostrar código':
            mostrar_codigo()
        elif 'pestaña' in control:
            pestanias_opciones(keyboard,control)
        elif controlseparado[0] == 'scroll':
            scroll(mouse,control)
        elif controlseparado[0] == 'mover':
            mover_opciones(sensibilidad,mouse,control)
        else:
            general_opciones(keyboard,mouse,control)
        if control=='salir de control':
                controlando = False
        del controlseparado
    del control
    del(mouse)
    del(keyboard)
    return sensibilidad, controlando
