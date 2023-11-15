class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, chiffre_arabe):
        if chiffre_arabe == 9:
            return "IX"
        elif chiffre_arabe >= 5:
            return "V" + cls.convertir(chiffre_arabe - 5)
        elif chiffre_arabe == 4:
            return "IV"
        return "I" * chiffre_arabe
