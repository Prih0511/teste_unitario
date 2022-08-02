class Marvel_viloes:
    def __init__(self, nome, poderes, perigo):
        self.nome = nome
        self.poderes = poderes
        self.perigo = perigo
        
    def get_nome(self):
        return self.nome


    def set_nome(self, nome):
        self.nome = nome


    def get_poder(self):
        return self.poderes


    def set_poder(self, poderes):
        self.poderes = poderes


    def get_perigo(self):
        return self.perigo


    def set_perigo(self, perigo):
        self.perigo = perigo


    def dominar_mundo(self, perigo):
        if perigo <= 2:
            return "Vilão Morto"

        elif perigo > 2 and perigo < 5:
            return "Vilão Preso"
        
        else:
            return "Vilão Dominou o Mundo"
