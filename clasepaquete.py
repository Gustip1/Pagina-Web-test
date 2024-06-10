class paquete:
    __numero_envio:int
    __peso:float
    __nombre_destinatario:str
    __direccion_destinatario:str
    __entregado:bool
    __observaciones:str

    def __init__(self,numero,peso,destinatario,entregado,obserbaciones,direccion):
        self.__numero_envio=numero
        self.__peso=peso
        self.__nombre_destinatario=destinatario
        self.__direccion_destinatario=direccion
        self.__entregado=entregado
        self.__observaciones=obserbaciones
    
    def get_numero_envio(self):
        return self.__numero_envio
    
    def get_peso(self):
        return self.__peso          
    
    def get_nombre_destinatario(self):
        return self.__nombre_destinatario
    
    def get_direccion_destinatario(self):
        return self.__direccion_destinatario
    
    def get_entregado(self):
        return self.__entregado
    
    def get_observaciones(self):    
        return self.__observaciones

    def __str__(self):
        return "Número de envío: "+str(self.__numero_envio)+"\nPeso: "+str(self.__peso)+"\nDestinatario: "+str(self.__nombre_destinatario)+"\nDirección: "+str(self.__direccion_destinatario)+"\nEntregado: "+str(self.__entregado)+"\nObservaciones: "+str(self.__observaciones)