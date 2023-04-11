class asistencia:
    def __init__(self,):
        self.list = ["Ricardo", "Tomas", "Jonathan", "Dante", "Antoine", "Polo", "Joaquin"]
    def presente(self,list_present, name: str):
        self.list_present = list_present
        self.name = name
        if self.list_present.count(self.name) > 0:
            return f"{self.name} esta presente"
        else: return f"{self.name} no esta presente"
if __name__=='__main__':
    list_present = ["Ricardo", "Tomas", "Dante", "Antoine", "Joaquin"]
    Lucho = asistencia()
    Lucho.presente(list_present, "Polo")
    print(Lucho.presente(list_present, "Polo"))