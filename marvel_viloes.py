#Criar uma classe chamada "MarvelViloes" onde terão os atributos nome(str), poderes(list), perigo(int).
class MarvelViloes:
    def viloes(self, nome, poderes, perigo):
        self.nome = nome
        self.poderes = poderes
        self.perigo = perigo
        
       
#A classe deve conter os métodos Getters e Setters de cada atributo. (Exemplo: def get_nome, def set_nome)
    def get_nome(self):
        return self.__nome


    def set_nome(self, nome):
        self.__nome = nome


    def get_poder(self):
        return self.__poderes


    def set_poder(self, poderes):
        self.__poderes = poderes


    def get_perigo(self):
        return self.__perigo


    def set_perigo(self, perigo):
        self.__perigo = perigo


#O atributo perigo deve receber valores somente entre 0 a 5.
    def fraquesa(self):
        for p in range(0, 5):
            self.__perigo = p

#A classe MarvelViloes deve conter um método chamado "dominar_mundo()".
    def dominar_mundo():

#- "dominar_mundo()" deve realizar uma validação do perigo do vilão com as seguintes condicionais:

#- Para perigo de menor ou igual a 2 retornar "Vilão Morto"

#- Para perigo maior que 2 e menor que 5 retornar "Vilão Preso"

#- Para perigo igual a 5 retornar "Vilão Dominou o Mundo"




#Critérios para testes unitários:

#1. Deverá ter no mínimo 3 vilões

#2. Deve conter as validações dos Setters e Getters

#3. Deve ter ao menos 3 testes das condicionais para o método "dominar_mundo"
