import calendar, random
from datetime import datetime
#import subprocess
from time import sleep
from googleapiclient.discovery import build
from playsound import playsound as ps
import errno, spam.gaudio as gd, spam.recursos as rc, webbrowser as wb, io, os
import spam.navegadores as nav, spam.control as control, spam.escucha as escucha, spam.codifica_cpp as cc


def main():
    os.system('color a')
    bucle = True
    entrada = False
    aux = False
    text = ''
    mostrar_ext = True
    nav_defecto = None
    nav.registrar_navegadores()
    usuario = ''
    usuario = leer_usuario()
    while bucle:
        #os.system('cls')
        os.system('cls')
        bienvenida()
        print('...')
        control.bip()
        text = escucha.escucha()
        text = transforma_vlaid(text)

        if "hola vlaid" in text:
            text,entrada,aux = hola_vlaid(text,usuario)
        
        if text=="salir":
            bucle, entrada = salir()
        if text=="control":
            control.control()
        while entrada:
            os.system('cls')
            print("""Main
Para salir dí "salir\"""")
            if not aux:
                control.bip()
                text = escucha.escucha()
                text = transforma_vlaid(text)
                aux = True
            
            if "hola vlaid" in text:
                text = text.replace('Hola vlaid', '')
            
            if text == 'ayuda':
                ayuda()
            if text == 'muéstrame tu código' or text == 'mostrar código':
                mostrar_codigo()
            if text == 'muestra tu carpeta' or text == 'muéstrame tu carpeta':
                mostrar_carpeta()
            if text == 'configurar usuario':
                usuario = nuevo_usuario()
            if text == 'eliminar usuario':
                eliminar_usuario()
            if ('cambiar modo' in text) or ('modificar modo' in text):
                escucha.cambiar_modo()
            if text == 'no mostrar':
                mostrar_ext = False
            if text == 'mostrar':
                mostrar_ext = True

            if ("abre" in text):
                abrir_sitio(text,nav_defecto)

            if 'dormir' in text or 'sleep' in text or 'duerme' in text or 'duermete' in text:
                control.dormir(text)

            if text=="salir":
                bucle, entrada = salir()

            if text == 'muéstrame tu actualización':
                actualizacion()

            if text=="ya llegamos":
                print('Bienvenidos')
                bienvenidos = "./audios/bienvenidos.mp3"
                ps(bienvenidos)
                del bienvenidos
            
            if text=='limpia la pantalla':
                os.system('cls')

            if text=='cántame una canción' or text=='canta una canción' or text=='canta':
                cantar_cancion()
            if text=='cuéntame un chiste' or text=='cuenta un chiste':
                contar_chiste()

            if 'busca' in text:
                text = text[6:]
                busqueda_google(text,nav_defecto)
            
            if text == 'qué día es' or text == 'qué hora es' or text == 'qué día es hoy':
                fechas(text)

            if 'reproduce ' in text:
                text = text[10:]
                reproducir_yt(text,mostrar_ext,nav_defecto)

            if text == 'codificar' or text == 'programar' or text == 'codifica':
                codificar(mostrar_ext)

            if text == 'configura navegador':
                #nav_defecto = configura_navegador()
                print('Estamos trabajando en ello...')
            
            if text == 'reiniciate' or text == 'reiniciar' or text == 'reinicio':
                reinicio_bot()
                bucle, entrada = salir()
            
            rc.recursos_funcion(text)
            
            if 'control' in text:
                entrarControl(text)
            if ('gracias' in text) or ('Gracias' in text):
                denada = './audios/denada.mp3'
                ps(denada)
                entrada = False
                del denada
            
            aux = False
    os.system('start /textos/libera.vbe')
    os.system('start ipconfig /flushdns')
    os.system('cls')
    del bucle
    del entrada
    del aux
    del nav_defecto
    del usuario
    del text
    del mostrar_ext


def bienvenida():
    instrucciones = """
        Asistente en desarrollo. Actualmente solo disponible en modo de prueba

        Para empezar a interactuar con di "Hola Vlaid"
        para salir di "Salir"
        Funciones Principales:
            Busca: Busca lo indicado en google
            Reproduce: Te da una lista de 3 opciones para reproducir en youtube
            Abre: Abre la pagina que le indiques
            Control: di "control" y espera el bip
                Ayuda: para detallar las funciondes de control
            Configurar usuario:
                Puedes configurar tu nombre de usuario con "configurar usuario"
                    Pedira nombre y despues confirmacion.. (Este proceso puede demorar un poco)
                    Si le dices que si, se guardara el usuario. de lo contrario te lo volvera a solicitar
                Puedes eliminar tu nombre de usuario con "Eliminar usuario"
        

        Funciones desarrollándose:
            Codificar: te ayuda a codificar en el lenguaje seleccionado
                Lenguaje actualmente en desarrollo c++

        Próximas funciones
            Módulo Resolver y Codificar en proceso
        
        Funciones de desarrollador
            reiniciate/reinicio/reiniciar: Reinicia la bot para probar las nuevas funciones
            mostrar codigo/muestrame tu codigo: Abre la carperta del programa en Visual Studio Code
                pd: Se debe de tener visual studio code instalado

        Funciones Ocultas... Te toca buscarlas a ti
    """

    print(instrucciones)
    del instrucciones

def hola_vlaid(text,usuario):
    """
        Recibe un texto para cortar y regresa el inicio del programa

        text str texto a cortar
        return regreso, los datos para iniciar el programa
    """
    os.system('cls')
    print(f'Hola {usuario} en que puedo ayudarte: ')
    ps('./audios/hola.mp3')
    try:
        ps('./audios/usuario.mp3')
    except:
        pass
    ps('./audios/ayudarte.mp3')
    text = (text[11:])
    entrada = True
    aux = True
    regreso = (text,entrada,aux)
    return regreso

def leer_usuario():
    usuario = ''
    try:
        with open('./textos/usuario.txt', 'r') as f:
            usuario = f.read()
            f.close()
    except:
        pass
    return usuario

def nuevo_usuario():
    configurando = True
    nuevo = ''
    while configurando:
        try:
            os.remove('./audios/usuario.mp3')
        except:
            pass
        try:
            os.remove('./textos/usuario.txt')
        except:
            pass
        print('Como quieres que te llame a partir de ahora?...')
        ps('./audios/nuevousuario.mp3')
        nuevo = escucha.escucha()
        with open('./textos/usuario.txt', 'w') as f:
            f.write(str(nuevo))
            f.close()
        dir = (os.path.dirname(__file__)).replace('\\','/')
        dir = (f'{dir}/audios/')
        gd.guarda(nuevo,'usuario',dir)
        print(f'Es correcto: {nuevo}?')
        ps('./audios/usuario.mp3')
        ps('./audios/correcto.mp3')
        res = escucha.escucha()
        if 'si' in res or 'sí' in res:
            configurando = False
        del res
        del f
        del dir
    del configurando
    return nuevo

def eliminar_usuario():
    try:
        os.remove('./audios/usuario.mp3')
    except:
        pass
    try:
        os.remove('./textos/usuario.txt')
    except:
        pass

def codificar(mostrar):
    menu = """Elige en que lenguaje vas a codificar:
    1.- C++ --En desarrollo
    2.- Python --Proximamente
    3.- Javascript --Proximamente
    4.- Html --Proximamente
    5.- Css --Proximamente
    6.- Cancelar"""
    print(menu)
    if mostrar:
            dir = (os.path.dirname(__file__)).replace('\\','/')
            dir = (f'{dir}/textos/opcionesCod.txt')
            os.system(f'start {dir}')
            #os.system(dir)
    ps('./audios/opcion.mp3')
    opcion = escucha.escucha()
    opcion = conversor_num(opcion)
    if mostrar:
            os.system('start taskkill /F /IM notepad.exe')
    if opcion == '1':
        del opcion
        cc.main()

def cantar_cancion():
    canciones = ['sinrencor','tunovio']
    num = random.randint(0,len(canciones)-1)
    print(num)
    if num < 0:
        num = 0
    print(num)
    ps(f'./audios/{canciones[num]}.mp3')


def contar_chiste():
    chistes = ['']
    num = random.randint(0,len(chistes)-1)

def mostrar_codigo():
    try:
        dir = (os.path.dirname(__file__)).replace('\\','/')
        #dir = (f'{dir}/textos/opcionesCod.txt')
        os.system(f'start code {dir}')
    except:
        control.bip()
        print('no se encontro visual studio code')
        ps('./audios/noseencontro.mp3')
        ps('./audios/visualstudiocode.mp3')
        sleep(5)

def mostrar_carpeta():
    try:
        dir = (os.path.dirname(__file__)).replace('\\','/')
        #dir = (f'{dir}/textos/opcionesCod.txt')
        os.system(f'cd {dir}')
        os.system(f'explorer {dir}')
    except:
        control.bip()
        print('error inesperado')
        sleep(5)

def configura_navegador():
    os.system('cls')
    print("""
        Selecciona una opcion por teclado
        1.- firefox
        2.- google chrome
        3.- opera
        4.- edge
    """)
    opc = int(input())
    if opc == 1:
        return 'firefox %s'
    elif opc == 2:
        return 'google-chrome %s'
    elif opc == 3:
        return 'opera %s'
    elif opc == 4:
        return 'edge %s'
    else:
        return None

def transforma_vlaid(mensaje):
    """
        Recibe una para transformar palabras a vlade
        mensaje str cualquier cadena
        return mensaje str cadena convertida con vlaid
    """
    dic = {
        'plate': 'vlaid',
        'gley': 'vlaid',
        'blade': 'vlaid',
        'blaze': 'vlaid',
        'blady': 'vlaid',
        'play': 'vlaid',
    }
    for i, j in dic.items(): 
        mensaje = mensaje.replace(i, j)
    del dic
    #print(mensaje)
    return mensaje

def entrarControl(text):
    if text == 'control':
        control.control()
    else:
        try:
            if (text.split())[0] == 'control' and type((text.split())[1]) == 'str':
                control.control_principal(text[8:])
        except:
            pass
    del text

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
    
    return text

def abrir_sitio(text,navdef):
    audio_sitio = False
    abriendo = "./audios/abriendo.mp3"
    pagina = (text[4:]).lower()
    page = ''
    sitio = pagina.replace(' ','')
    sitio = cc.remplazo_caracteres_especiales(sitio)
    if (sitio=="ashiracorp"):
        sitio = "asiracorp"
    if(sitio=="whatsapp"):
        page = "web.whatsapp.com"
    else:
        page = "www."+sitio+".com"
    
    dice = f'./audios/{sitio}.mp3'
    try:
        with open(dice) as f:
            audio_sitio = True
    except IOError as e:
        # Raise the exception if it is not ENOENT (No such file or directory)
        if e.errno != errno.ENOENT:
            raise
        # No such file or directory
    
    try:
        if not audio_sitio:
            ruta = './audios'
            gd.guarda(sitio,sitio,ruta)
            del ruta
    except:
        pass
    ps(abriendo)
    ps(dice)
    wb.get(navdef).open_new(page)
    del audio_sitio
    del abriendo
    del navdef
    del page
    del pagina
    del sitio
    del dice

def fechas(text):
    try:
        os.remove('./audios/fecha.mp3')
    except:
        pass
    fecha = ''
    dir = (os.path.dirname(__file__)).replace('\\','/')
    dir = (f'{dir}/audios/')
    now = datetime.now()
    if text == 'qué día es' or text == 'qué día es hoy':
        fecha += (f'Hoy es {now.day} de {now.month} del {now.year}')
        c = calendar.TextCalendar(calendar.SUNDAY)
        c.prmonth(now.year, now.month)
    if text == 'qué hora es':
        fecha += (f'Son las {now.hour} con {now.minute} minutos')
    gd.guarda(fecha,'fecha',dir)
    ps(dir+'fecha.mp3')
    os.remove('./audios/fecha.mp3')
    text = escucha.escucha()
    del fecha
    del now
    del dir
    del text


def busqueda_google(busqueda,navdef):
    """
        Abre el navegador para realizar una busqueda en google

        busqueda str con la frase a buscar en google
        regresa none
    """
    link_busqueda = 'https://www.google.com/search?q='
    busqueda = busqueda.replace(' ', '+')
    link_busqueda += busqueda
    wb.get(navdef).open_new(link_busqueda)
    del link_busqueda
    del busqueda

def busqueda_yt(busqueda):
    #DEVELOPER_KEY = "AIzaSyCYoDmqWaM7LC6ElJQXKhLYQAjMd6SuCbA" #ojitos
    DEVELOPER_KEY = "AIzaSyCbtkU9RkUXuVJxwNYTD7ceO5LfS6cVcaM" #wenceslao
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=busqueda,
        part="id,snippet",
        maxResults=3
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s"% (search_result["snippet"]["title"]))
            videos.append(f'https://www.youtube.com/watch?v={(search_result["id"]["videoId"])}')
        
    del DEVELOPER_KEY
    del YOUTUBE_API_SERVICE_NAME
    del YOUTUBE_API_VERSION
    del youtube
    del search_response
    return videos

def reinicio_bot():
    dir = (os.path.dirname(__file__)).replace('\\','/')
    dir = (f'{dir}/main.py')
    os.system(dir)
    del dir

def reproducir_yt(text,mostrar,navdef):
    try:
        lista = busqueda_yt(text)
        presentacion = """"""
        archivo = './textos/opciones.txt'
        auxtemp=0
        dir=''
        lista_num = 1
        for id in lista:
            if auxtemp%2==0:
                presentacion += (f'{lista_num}.- Video: {id}\n').replace('&quot','')
                lista_num += 1
            else:
                presentacion += (f'link: {id}\n\n')

            auxtemp += 1
        with io.open(archivo, "w", encoding="utf-8") as f:
            f.write(presentacion)
        print(text,'\n\n',presentacion,'Elige una opcion: ')
        ps('./audios/opcion.mp3')
        if mostrar:
            dir = (os.path.dirname(__file__)).replace('\\','/')
            dir = (f'{dir}/textos/opciones.txt')
            os.system(f'start {dir}')
            #os.system(dir)
        seleccionando = True
        while seleccionando:
            print('...')
            opc=escucha.escucha()
            #opc=input('opcion: ')
            print(opc)
            if ('uno' in opc) or ('1' in opc):
                wb.get(navdef).open(lista[1])
                seleccionando = False
            elif ('dos' in opc) or ('2' in opc):
                wb.get(navdef).open(lista[3])
                seleccionando = False
            elif ('tres' in opc) or ('3' in opc):
                wb.get(navdef).open(lista[5])
                seleccionando = False
            elif ('ninguna' in opc):
                seleccionando = False
            del opc
        
        #subprocess.call('taskkill /F /IM notepad.exe',shell=True)
        if mostrar:
            os.system('start taskkill /F /IM notepad.exe')
            os.remove('./textos/opciones.txt')
        del lista
        del presentacion
        del archivo
        del auxtemp
        del lista_num
        del seleccionando
        del mostrar
        del dir
    except:
        print('Couota de youtube excedida')

def actualizacion():
    print('este es otro mensaje')
    sleep(5)

def ayuda():
    leyendo = True
    while leyendo:
        os.system('cls')
        bienvenida()
        print('Cuando termine de leer diga "Listo"')
        if (escucha.escucha())=='listo':
            leyendo = False
    del leyendo


def salir():
    """ print('Adios, nos vemos luego')
    adios = "./audios/adios.mp3"
    ps(adios)
    del adios """
    bucle=False
    entrada = False
    return (bucle,entrada)


if __name__ == "__main__":
    main()