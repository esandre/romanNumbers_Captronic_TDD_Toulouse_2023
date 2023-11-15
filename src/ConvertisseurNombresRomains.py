class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, chiffre_arabe):
        if (chiffre_arabe + 1) % 5 == 0:
            suivant = cls.convertir(chiffre_arabe + 1)
            if len(suivant) == 2:
                return suivant[0] + "I" + suivant[1]
            return "I" + suivant
        if chiffre_arabe >= 10:
            return "X" + cls.convertir(chiffre_arabe - 10)
        elif chiffre_arabe >= 5:
            return "V" + cls.convertir(chiffre_arabe - 5)
        return "I" * chiffre_arabe
