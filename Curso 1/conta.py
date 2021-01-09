class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def __valida_saque(self, valor):
        valor_valido = self.__saldo + self.__limite
        return valor <= valor_valido

    def saca(self, valor):
        if self.__valida_saque(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou do limite'.format(valor))
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "107"}