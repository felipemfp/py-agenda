class Contato(object):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def tostring(self):
        return "%s: %s" % (self.__nome, self.__telefone)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        if telefone != "":
            self.__telefone = telefone

    nome = property(fget=get_nome, fset=set_nome)
    telefone = property(fget=get_telefone, fset=set_telefone)
