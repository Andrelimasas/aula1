class no:
    def _init_(self,valor):
        self.valor
        self.proximo = None
class listaencadeada:
    def _init_(self):
        self.primeiro = None
    def adicionar(self,valor):
        novo_no = no(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while self.primeiro is not None:
                atual = atual.proximo
            atual.proximo = novo_no
