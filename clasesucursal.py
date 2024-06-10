class sucursal:
    __numero:int
    __provincia:str
    __direccion:str
    __localidad:str

    def __init__(self,numero,provincia,direccion,localidad):
        self.__numero=numero
        self.__provincia=provincia
        self.__direccion=direccion
        self.__localidad=localidad

    def get_numero(self):
        return self.__numero    
    
    def get_provincia(self):

        return self.__provincia

    def get_direccion(self):
        return self.__direccion

    def get_localidad(self):
        return self.__localidad
    
    def __str__(self):
        return "Número: "+str(self.__numero)+"\nProvincia: "+str(self.__provincia)+"\nDirección: "+str(self.__direccion)+"\nLocalidad: "+str(self.__localidad)