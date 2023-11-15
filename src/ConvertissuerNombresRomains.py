class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, chiffre_arabe):
        if chiffre_arabe == 4:
            return "IV"
        return "I" * chiffre_arabe
