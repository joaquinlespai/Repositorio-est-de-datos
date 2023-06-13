class Piladocumentos:
    def __init__(self):
        self.documentos = []

    def agregar_documentos(self, documento):
        self.documentos.append(documento)

    def descartar_documentos(self):
        if self.esta_vacia():
            print("La pila de documentos está vacía")
        else:
            documento_descartado = self.documentos.pop()
            print("Se ha descartado el documento:", documento_descartado)

    def esta_vacia(self):
        return len(self.documentos) == 0

papeleo = Piladocumentos()

papeleo.agregar_documentos("Informe final")
papeleo.agregar_documentos("Guía de Estudio")
papeleo.agregar_documentos("Tesis 4")
papeleo.agregar_documentos("Seminario Osorno")

while not papeleo.esta_vacia():
    papeleo.descartar_documentos
