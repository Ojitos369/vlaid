from getpass import getuser
import webbrowser as wb
from webbrowser import register

def registrar_navegadores():
    usuario=getuser()
    ff_path=''
    try:
        ff_path = wb.get("C:/Program Files/Mozilla Firefox/firefox.exe")
        wb.register('firefox', None, ff_path)
    except:
        pass
    try:
        ff_path = ("C:/Program Files/Google/Chrome/Application/chrome.exe")
        wb.register('google-chrome', None, ff_path)
    except:
        pass
    try:
        ff_path = (f'C:/Users/{usuario}/AppData/Local/Programs/Opera/launcher.exe')
        wb.register('opera', None, ff_path)
    except:
        pass
    try:
        ff_path = (f'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
        wb.register('edge', None, ff_path)
    except:
        pass
    del ff_path
    del usuario

def nav_predeterminado():
    browser = None
    nav = ''
    browsers = ('mozilla','firefox','netscape','galeon','epiphany','skipstone','kfmclient','konqueror','kfm','mosaic','opera','grail','links','elinks','lynx','w3m','windows-default','macosx','safari','google-chrome','chrome','chromium','chromium-browser')
    browser = wb.get()
    print(browser)
    for b in browsers:
        try:
            browser = wb.get(b)
            print(browser)
        except wb.Error:
            pass
        else:
            if b is None:
                print("Navegador por defecto.")
            else:
                nav = ("%s"%b)
                print("Navegador '%s'." % b)
                
    print(nav)
    print("%s"%(wb.get('google-chrome')))
    del browser
    del browsers