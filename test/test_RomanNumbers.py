import itertools
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

    def cases(self):
        symbols = [["V", 5], ["X", 10]]
        for symbol in symbols:
            for delta in [0, 1, 2, 3]:
                yield symbol[0], symbol[1], delta

    def test_quinte_plus_unit(self):
        for symbole, valeur, delta in self.cases():
            with self.subTest(symbole + str(delta)):
                # ETANT DONNE un symbole romain ayant pour valeur <valeur>
                # ET un <chiffre> le dépassant de 1 à 3
                chiffre = valeur + delta

                # QUAND on le convertit en nombres romains
                nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

                # ALORS on obtient le symbole suivi de "I" répété <chiffre - valeur> fois
                attendu = symbole + "I" * (chiffre - valeur)
                self.assertEqual(attendu, nombres_romains)

    def test_quatorze(self):
        # ETANT DONNE le chiffre 14
        chiffre = 14

        # QUAND on le convertit en nombres romains
        nombres_romains = ConvertisseurNombresRomains.convertir(chiffre)

        # ALORS on obtient "XIV"
        self.assertEqual("XIV", nombres_romains)


if __name__ == '__main__':
    unittest.main()
