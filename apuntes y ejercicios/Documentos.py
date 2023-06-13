class Piladocumentos:
    def __init__(self):
        self.documentos = []

    def agregar_documentos(self, documentos):
        self.documentos.append(documentos)

    def descartar_documentos(self):
        if self.esta_vacia():
            print("la pila de documentos esta vacia")
        else:
            documento_descartado = self.documentos.pop()
            print("se ha descartado el libro:", documento_descartado )

    def esta_vacia(self):
        return len(self.documentos) == 0
    
def Imprimir_pila(pila):
    print("La cantidad de documentos en la pila es: ")
    for documento in reversed (pila.documentos):
        print(documento)
    print()
    
papeleo = Piladocumentos()

papeleo.agregar_documentos("Informe final")
papeleo.agregar_documentos("Guia de Estudio")
papeleo.agregar_documentos("Tesis 4")
papeleo.agregar_documentos("Seminario Osorno")

Imprimir_pila(papeleo)

papeleo.agregar_documentos("Avance de tesis")
papeleo.agregar_documentos("Proyecto integrador")

Documentofinal = papeleo.documentos [-2]
print("El documento superior final es: ", Documentofinal)
print()

papeleo.descartar_documentos()

Imprimir_pila(papeleo)

if papeleo.esta_vacia():
    print("La pila de documentos se encuentra vacia")
else:
    print("La pila de documentos no se encuentra vacia")