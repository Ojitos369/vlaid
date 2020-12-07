from playsound import playsound as ps
import webbrowser as wb, speech_recognition as sr

def escucha():
    """
        Recibe entreda por voz y transforma a texto
    """
    grabando = True
    r = sr.Recognizer()
    mensaje = ""

    while grabando:
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
    
    return mensaje

def recursos_funcion(text):
    if (text=="ando caliente"):
        cal()

    if ("una paja o que" in text) or ("una paja o qué" in text):
        pj()

def cal():
    print("Quieres ayuda con eso?")
    ayuda = ("./audios/ayuda.mp3")
    ps(ayuda)
    respuesta = escucha()
    if ("si" in respuesta) or ("sí" in respuesta):
        wb.open("https://www.pornhub.com")


def pj():
    print('Claro, vamos a eso')
    claro = "./audios/claro.mp3"
    ps(claro)
    wb.open("https://www.pornhub.com")