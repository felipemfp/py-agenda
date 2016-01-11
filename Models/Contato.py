class Contato(object):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def __repr__(self):
        return "%s: %s" % (self.__nome, self.__telefone)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != "":
            self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if telefone != "":
            self.__telefone = telefone