class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, chiffre_arabe):
        if (chiffre_arabe + 1) % 5 == 0:
            suivant = cls.convertir(chiffre_arabe + 1)
            return cls.__insert_between(suivant, "I")
        if chiffre_arabe >= 10:
            return "X" + cls.convertir(chiffre_arabe - 10)
        elif chiffre_arabe >= 5:
            return "V" + cls.convertir(chiffre_arabe - 5)
        return "I" * chiffre_arabe

    @classmethod
    def __insert_between(cls, string, insertion):
        if len(string) == 2:
            return string[0] + insertion + string[1]
        return insertion + string
