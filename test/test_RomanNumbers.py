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

    @parameterized.expand([
        ["V", 5, 0], ["V", 5, 1], ["V", 5, 2], ["V", 5, 3],
        ["X", 10, 0], ["X", 10, 1], ["X", 10, 2], ["X", 10, 3],
    ])
    def test_quinte_plus_unit(self, symbole, valeur, delta):
        # ETANT DONNE un symbole romain ayant pour valeur <valeur>
        # ET un <chiffre> le dépassant de 1 à 3
        chiffre = valeur + delta

        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient le symbole suivi de "I" répété <chiffre - valeur> fois
        attendu = symbole + "I" * (chiffre - valeur)
        self.assertEqual(attendu, nombres_romains)


if __name__ == '__main__':
    unittest.main()
