import unittest
from Analisis_Bacilo_koch.main import FICHEROS
from Analisis_Bacilo_koch.utilities.ej_1_1 import count_clases_orfs
from Analisis_Bacilo_koch.utilities.ej_1_2 import freq_clase
from Analisis_Bacilo_koch.utilities.ej_2_1 import  clases_listado
from Analisis_Bacilo_koch.utilities.ej_2_2 import promedio_orf
from Analisis_Bacilo_koch.utilities.ej_3 import multiple

ficheros = FICHEROS

class TestAnalisisBaciloKoch(unittest.TestCase):

    def test_1_1(self):
        """
        Funcion para testear ejercicio 1.1 funcion count_clases_orfs
        :return: None
        """
        golden_number = 3
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        self.assertEqual(result['2220'], golden_number)

    def test_1_2(self):
        """
        Funcion para testear ejercicio 1.2 funcion count_clases_orfs
        :return: None
        """
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        frq, clase = freq_clase("Pentose phosphate pathway ", result, ficheros)
        self.assertEqual(frq, 11)
        self.assertEqual(clase, '1250')

    def test_2_1(self):
        """
        Funcion para testear ejercicio 2.1 funcion clases_listado
        :return: None
        """
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        listado = ["electron"]
        clases_escogidas, orfs_escogidos = clases_listado(clases, orfs, descriptions, listado)
        self.assertEqual(clases_escogidas['electron'], 2)
        self.assertEqual(orfs_escogidos['electron'], {'tb3029', 'tb3028', 'tb3053'})

    def test_2_2(self):
        """
        Funcion para testear ejercicio 2.2 funcion promedio_orf
        :return: None
        """
        orfs_escogidos = {"electron": ['tb3029']}
        resultado = promedio_orf(orfs_escogidos)
        self.assertEqual(resultado['electron'], 21)

    def test_3(self):
        """
        Funcion para testear ejercicio 3 funcion count_clases_orfs
        :return: None
        """
        result, orfs, clases, descriptions = count_clases_orfs(ficheros)
        aptos = multiple(clases)
        self.assertEqual(aptos[9], 3)

if __name__ == '__main__':
    unittest.main()