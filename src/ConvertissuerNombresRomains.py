class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, chiffre_arabe):
        if chiffre_arabe == 4:
            return "IV"
        elif chiffre_arabe == 5:
            return "V"
        return "I" * chiffre_arabe
