class Data:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    def formatada(self):
        print("{:02}/{:02}/{}".format(self.__dia, self.__mes, self.__ano))
    

