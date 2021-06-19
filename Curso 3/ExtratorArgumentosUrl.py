class ExtratorArgumentosUrl:
    def __init__(self, url) -> None:
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError('Url Inválida!!')
    
    @staticmethod
    def urlEhValida(url):
        if url and url.startswith('https://bytebank.com'):
            return True
        else:
            return False
    
    def extraiArgumentos(self):

        busca_modelo_origem = 'moedaorigem='.lower()
        busca_modelo_destino = 'moedadestino='.lower()

        index_origem_inicio = self.encontraIndiceInicial(busca_modelo_origem)
        index_origem_final = self.url.find('&')

        moedaOrigem = self.url[index_origem_inicio:index_origem_final]

        if moedaOrigem == 'moedadestino':
            self.trocaMoedaOrigen()
            index_origem_inicio = self.encontraIndiceInicial(busca_modelo_origem)
            index_origem_final = self.url.find('&')
            moedaOrigem = self.url[index_origem_inicio:index_origem_final]
        
        index_destino_inicio = self.encontraIndiceInicial(busca_modelo_destino)
        index_destino_final = self.url.find('&valor')
        moedaDestino = self.url[index_destino_inicio:index_destino_final]

        return moedaOrigem, moedaDestino
    
    def encontraIndiceInicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)
    
    def trocaMoedaOrigen(self):
        self.url = self.url.replace('moedadestino', 'real', 1)
    
    def extraiValor(self):
        buscaValor = "valor="
        index_inicio_valor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[index_inicio_valor:]
        return valor 


url = 'https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500'

argumentoUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaFinal = argumentoUrl.extraiArgumentos()
valor = argumentoUrl.extraiValor()
# print(moedaOrigem, moedaFinal, valor)

urlByteBank = 'https://bytebank.com'
url1 = 'https://buscasites.com/busca?q=https://bytebank.com'
url2 = 'https://bitebank.com'
url3 = 'https://bytebank.com/cambio/test/teste'

print(url1.startswith(urlByteBank))