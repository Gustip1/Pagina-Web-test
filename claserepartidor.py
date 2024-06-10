class repartidor:
    __numero:int
    __nombre:str
    __dni:str

    def __init__(self,numero,nombre,dni):
        self.__numero=numero
        self.__nombre=nombre
        self.__dni=dni

    def get_numero(self):
        return self.__numero    
    
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni

    def __str__(self):
        return "Número: "+str(self.__numero)+"\nNombre: "+str(self.__nombre)+"\nDNI: "+str(self.__dni)