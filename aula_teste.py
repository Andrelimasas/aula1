class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = 
        
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        
    def insercao(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            auxiliar = self.cabeca
            while auxiliar.proximo is not None:
                auxiliar = auxiliar.proximo
            auxiliar.proximo = novo_no
            
    def imprimir(self):
        auxiliar = self.cabeca
        while auxiliar is not None:
            print(auxiliar.valor)
            auxiliar = auxiliar.proximo
    

if __name__ == "__main__":

    lista = ListaEncadeada()
    
    lista.insercao(10)
    lista.insercao(20)
    lista.insercao(30)
    lista.insercao(40)
    
    lista.imprimir()
    

