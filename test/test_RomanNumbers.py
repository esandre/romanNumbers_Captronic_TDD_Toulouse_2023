import unittest

from parameterized import parameterized

from ConvertisseurNombresRomains import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):
    @parameterized.expand([[1], [2], [3]])
    def test_unite(self, chiffre):
        # ETANT DONNE un <chiffre> compris entre 1 et
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "I" répété <chiffre> fois
        attendu = "I" * chiffre
        self.assertEqual(attendu, nombres_romains)

    @parameterized.expand([[4], [9]])
    def test_unite_avant_quinte(self, chiffre):
        # ETANT DONNE un <chiffre> dont le suivant est multiple de 5
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient la représentation du suivante précédée de "I"
        attendu = "I" + ConvertisseurNombresRomains.convertir(chiffre + 1)
        self.assertEqual(attendu, nombres_romains)

    @parameterized.expand([[5], [6], [7], [8]])
    def test_five_plus_unit(self, chiffre):
        # ETANT DONNE chiffre compris entre 5 et 7
        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "V" suivi de <chiffre> - 5 fois "I"
        attendu = "V" + "I" * (chiffre - 5)
        self.assertEqual(attendu, nombres_romains)

    @parameterized.expand([[10], [11], [12], [13]])
    def test_ten_plus_unit(self, chiffre):
        # ETANT DONNE un <chiffre> compris entre 10 et 13

        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "X" + "I" répété <chiffre - 10> fois
        attendu = "X" + "I" * (chiffre - 10)
        self.assertEqual(attendu, nombres_romains)


if __name__ == '__main__':
    unittest.main()
