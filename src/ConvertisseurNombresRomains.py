class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, chiffre_arabe):
        if (chiffre_arabe + 1) % 5 == 0:
            return "I" + cls.convertir(chiffre_arabe + 1)
        if chiffre_arabe == 10:
            return "X"
        elif chiffre_arabe >= 5:
            return "V" + cls.convertir(chiffre_arabe - 5)
        return "I" * chiffre_arabe