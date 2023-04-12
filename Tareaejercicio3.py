def vocal(texto):
    vocales = "a,e,i,o,u"
    contador_de_vocales = {"a": 0, "e": 0, "i": 0, "o": 0,"u": 0,}
    for letra in texto:
        if letra in vocales:
            contador_de_vocales[letra] += 1
    return contador_de_vocales 

texto = (input("ingresa tu texto para contar sus vocales:"))
contador_de_vocales = vocal(texto)
print(f"su texto, {texto}, tiene una cantidad de vocales de: {contador_de_vocales}")       