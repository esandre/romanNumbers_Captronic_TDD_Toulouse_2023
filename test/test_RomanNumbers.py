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

    @parameterized.expand([[5], [6], [7], [8]])
    def test_five_plus_unit(self, chiffre):
        # ETANT DONNE chiffre compris entre 5 et 7
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "V" suivi de <chiffre> - 5 fois "I"
        attendu = "V" + "I" * (chiffre - 5)
        self.assertEqual(attendu, nombres_romains)

    def test_neuf(self):
        # ETANT DONNE chiffre 9
        chiffre = 9
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "IX"
        attendu = "IX"
        self.assertEqual(attendu, nombres_romains)

    def test_ten(self):
        # ETANT DONNE le chiffre 10
        chiffre = 10

        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "X"
        self.assertEqual("X", nombres_romains)


if __name__ == '__main__':
    unittest.main()
