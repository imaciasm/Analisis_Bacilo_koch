import unittest
from Analisis_Bacilo_koch.main import multiple, promedio_orf,clases_listado, count_clases_orfs, ficheros, freq_clase

class TestAnalisisBaciloKoch(unittest.TestCase):

    def test_1_1(self):
        golden_number = 3
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        self.assertEqual(result['2220'], golden_number)

    def test_1_2(self):
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        frq, clase = freq_clase("Pentose phosphate pathway ", result)
        self.assertEqual(frq, 11)
        self.assertEqual(clase, '1250')

    def test_2_1(self):
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        listado = ["electron"]
        clases_escogidas, orfs_escogidos = clases_listado(clases, orfs, descriptions, listado)
        self.assertEqual(clases_escogidas['electron'], 2)
        self.assertEqual(orfs_escogidos['electron'], {'tb3029', 'tb3028', 'tb3053'})

    def test_2_2(self):
        orfs_escogidos = {"electron": ['tb3029']}
        resultado = promedio_orf(orfs_escogidos)
        self.assertEqual(resultado['electron'], 21)

    def test_3(self):
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        aptos = multiple(clases)
        self.assertEqual(aptos[9], 3)

if __name__ == '__main__':
    unittest.main()