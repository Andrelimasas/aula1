class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir (self, dado):
        novo_no = No(dado)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.anterior = atual
    
    def percorrer_frente(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")

def inversao(self):
    atual = self.primeiro
    final = None

    while atual  is not None:
        finsl = atual
        atual.anterior, atual.proximo = atual.prioximo,atual.anterior
        atual = atual.anterior
    self.primeiro = atual

listaDupla = ListaDuplamenteEncadeada()
listaDupla.inserir(10)
listaDupla.inserir(20)
listaDupla.inserir(30)
listaDupla.inserir(40)
listaeurpla