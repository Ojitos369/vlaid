from gtts import gTTS as gt
import os

def guarda(dato,name,ruta):
    audio = gt(text = dato, lang="es", slow=False)

    audio.save("%s.mp3" % os.path.join(ruta,name))
""" 
texto = input("Texto: ")
nombre = input("Nombre: ")

guarda(texto,nombre) """