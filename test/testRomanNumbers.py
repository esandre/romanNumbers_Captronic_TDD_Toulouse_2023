import unittest

from ConvertissuerNombresRomains import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):
    def test_un(self):
        # ETANT DONNE le chiffre 1
        chiffre = 1

        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "I"
        self.assertEqual("I", nombres_romains)


if __name__ == '__main__':
    unittest.main()
