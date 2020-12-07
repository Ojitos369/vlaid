import speech_recognition as sr, os
def escucha():
    """
        Recibe entreda por voz y transforma a texto
    """
    modo = revision()
    
    grabando = True
    r = sr.Recognizer()
    #r.energy_threshold = 2500
    mensaje = ""

    while grabando:
        if modo:
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                #print('escuchando')
                mensaje = r.recognize_google(audio, language="es-Es")
                mensaje = mensaje.lower()
                grabando = False
            except:
                mensaje = ''
                #print('error de escucha')
        else:
            mensaje = input('Escribe: ')
            grabando = False
    print(mensaje)
    del grabando
    del modo
    del r
    return mensaje

def revision():
    modo = ''
    try:
        with open('./textos/modo_entrada.txt', 'r') as f:
            modo = f.read()
            f.close()
    except:
        pass
    if 'uno' in modo or '1' in modo:
        del modo
        return True
    elif 'dos' in modo or '2' in modo:
        del modo
        return False

def cambiar_modo():
    contestando = True
    respuesta = ''
    while contestando:
        os.system('cls')
        print("""
            Elige una opcion de ingreso.
            1.- Voz
            2.- Escritura
        """)
        respuesta = escucha()
        if 'uno' in respuesta or '1' in respuesta or'dos' in respuesta or '2' in respuesta:
            contestando = False
        else:
            print('Opcion No valida. Intenta nuevamente')
            os.system('pause')
    try:
        with open('./textos/modo_entrada.txt', 'w') as f:
            f.write(respuesta)
            f.close()
    except:
        pass
    del respuesta
    del contestando
