import os
from Analisis_Bacilo_koch.utilities.graphics import plot
from Analisis_Bacilo_koch.utilities.ej_1_1 import count_clases_orfs
from Analisis_Bacilo_koch.utilities.ej_1_2 import freq_clase
from Analisis_Bacilo_koch.utilities.ej_2_1 import  clases_listado
from Analisis_Bacilo_koch.utilities.ej_2_2 import promedio_orf
from Analisis_Bacilo_koch.utilities.ej_3 import multiple, print_bonito

FICHEROS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/tb_functions.pl")


def main():
    """
    Ejecución del programa

    :return: None
    """
    ficheros = FICHEROS

    #1.1
    result, orfs, clases, descriptions = count_clases_orfs(ficheros)
    plot(result)

    #1.2
    frq, clase = freq_clase("Pentose phosphate pathway ", result, ficheros)
    print(format(f"Clase {clase} contiene {frq} ORFS"))

    #2.1
    listado = ["electron", "subunit"]
    clases_escogidas, orfs_escogidos = clases_listado(clases, orfs, descriptions, listado)
    plot(clases_escogidas)

    #2.2
    resultado = promedio_orf(orfs_escogidos)
    plot(resultado)

    #3
    aptos = multiple(clases)
    plot(aptos)
    print_bonito(aptos)




if __name__ == "__main__":
    main()



