import datetime
class transpase:
    __numero_transporte:int
    __fecha_hora_salida:datetime
    __fecha_hora_llegada:datetime

    def __init__(self,numero,fecha_hora_salida,fecha_hora_llegada):
        self.__numero_transporte=numero
        self.__fecha_hora_salida=fecha_hora_salida
        self.__fecha_hora_llegada=fecha_hora_llegada
        
    def get_numero_transporte(self):
        return self.__numero_transporte
    
    def get_fecha_hora_salida(self):
        return self.__fecha_hora_salida
    
    def get_fecha_hora_llegada(self):
        return self.__fecha_hora_llegada

    def __str__(self):
        return "Número de transporte: "+str(self.__numero_transporte)+"\nFecha de salida: "+str(self.__fecha_hora_salida)+"\nFecha de llegada: "+str(self.__fecha_hora_llegada)