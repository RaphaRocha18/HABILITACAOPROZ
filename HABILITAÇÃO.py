def categoria(rodas, pessoas, peso):
    if rodas == 2 or rodas == 3:
        print ("Categoria A")
    elif rodas == 4 and pessoas <= 8 and peso <= 3500:
        print ("Categoria B")
    elif rodas >= 4 and peso > 3500 and peso <= 6000:
        print ("Categoria C")
    elif rodas >= 4 and pessoas > 8:
        print ("Categoria D")
    elif rodas >= 4 and peso > 6000:
        return ("Categoria E")