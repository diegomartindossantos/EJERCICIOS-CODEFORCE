
for x in (range(int(input("")))):
    palabra = str(input(""))
    if palabra:        
        if len(palabra) > 10: 
            letras_entre = len(palabra)-2
            primera_letra = list(palabra)[0]
            ultima_letra = list(palabra)[-1]
            print (primera_letra+str(letras_entre)+ultima_letra)
        else:
            print (palabra)
    else:
        break

