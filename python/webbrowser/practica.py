import webbrowser

browser = None
browsers = {"firefox", "opera", "safari", "google-chrome"}
for b in browsers :
    try :
        browser = webbrowser.open("https://www.instagram.com/brujeriatech/")
    except webbrowser.Error :
        if b is None :
            print("No tienes un navegador")
        else :
            print("El navegador '%s' no se ha encontrado" % b)
    else :
        if b is None :
            print("Navegador por defecto")
        else :
            print (b)