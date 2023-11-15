import unittest

from parameterized import parameterized

from ConvertissuerNombresRomains import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):
    @parameterized.expand([[1], [2], [3]])
    def test_unite(self, chiffre):
        # ETANT DONNE un <chiffre> compris entre 1 et
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "I" répété <chiffre> fois
        attendu = "I" * chiffre
        self.assertEqual(attendu, nombres_romains)

    def test_four(self):
        # ETANT DONNE 4
        chiffre = 4
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)
        # ALORS on obtient "IV"
        self.assertEqual("IV", nombres_romains)

    def test_five(self):
        # ETANT DONNE 5
        chiffre = 5
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)
        # ALORS on obtient "V"
        self.assertEqual("V", nombres_romains)

    def test_six(self):
        # ETANT DONNE 6
        chiffre = 6
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)
        # ALORS on obtient "VI"
        self.assertEqual("VI", nombres_romains)


if __name__ == '__main__':
    unittest.main()
