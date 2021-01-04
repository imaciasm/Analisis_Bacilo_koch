import os
import glob
from collections import Counter
import matplotlib.pyplot as plt


ficheros = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/tb_functions.pl")


def count_clases_orfs(fichero):
    """
    Dado un fichero saca un diccionario con clase: numero_orfs

    Primero, será necesario que leáis los archivos facilitados de la forma más óptima teniendo en cuenta las tareas pedidas. Tendréis que justificar vuestra decisión
    Leemos el fichero linea a linea porque no tiene un formato tabla, cada linea es diferente y hay que elegir cual queremos y cual no.


    :param fichero: str - Path al fichero de datos
    :return: result: dict - Relacion entre las clases y el numero de ORF con esa clase
    """
    orfs = []
    clases = []
    descriptions = []
    with open(ficheros, "r") as f:
        for line in f:
            if line.startswith("function"):
                orf = line.split(",")[0][9:]
                numb1 = line.split(",")[1].strip("[")
                numb2 = line.split(",")[2]
                numb3 = line.split(",")[3]
                numb4 = line.split(",")[4].strip("]")
                clase = numb1 + numb2+ numb3 +numb4
                descripcion = line.split(",")[-1].strip("),")
                orfs.append(orf)
                clases.append(clase)
                descriptions.append(descripcion)
    result = Counter(clases)
    return result, orfs, clases, descriptions

def plot(dictionary):
    """
    Plot de los keys y los valores del diccionarios

    :param dictionary: dict - Cualquier diccionario
    :return: None
    """
    valores = [value for key, value in dictionary.items()]
    keys = [key for key, value in dictionary.items()]
    plt.bar(keys, valores)
    plt.xticks(rotation=90)
    plt.show()

def freq_clase(descripcion, frq_clase_orf):
    """
    Busca cuantos clases tienen al menos 1 ORF
    con la descripcion indicada

    :param descripcion: str-descripcion que buscar
    :param frq_clase_orf: dict-diccionario con clase:frequencia
    :return: freq: int-frequencia de la clase
             clase: str-nombre de la clase
    """
    with open(ficheros, "r") as f:
        for line in f:
            if line.startswith("class") and descripcion.lower() in line.lower():
                numb1 = line.split(",")[0].strip("class([")
                numb2 = line.split(",")[1]
                numb3 = line.split(",")[2]
                numb4 = line.split(",")[3].strip("]")
                clase = numb1 + numb2 + numb3 + numb4
                print(clase)
                break
    return frq_clase_orf[clase], clase

def clases_listado(clases, orfs, descriptions, listado):
    """
    Dado un listado de patrones busca las clases las
    clases que contienen ORFs con esa dexcripcion y
    sus ORFS

    :param clases: lista de todas las clases
    :param orfs: lista de todos los orfs
    :param descriptions: listas de todas las descripciones
    :param listado: listado de patrones
    :return: clases_escogidas: list - clases con ORFS con el patron
             ORFS_escogidos: list - ORFS con el menos un patron de los listados
    """
    clases_escogias = []
    orfs_escogidos = []
    for clase, orf, description in zip(clases, orfs, descriptions):
        for patron in listado:
            if patron in description:
                clases_escogias.append(clase)
                orfs_escogidos.append(orf)
    return set(clases_escogias), set(orfs_escogidos)

def promedio_orf(orfs):
    """
    Funcion que busca cuantos ORF están relacionados con otro

    :param orfs: list - lista de orfs
    :return: resultado: dict - relacion entre cada ORF y el numero de ORFS correlacionados
    con este
    """
    ficheros = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/orfs/tb_data*")
    files = glob.glob(ficheros)
    resultado = {}
    for orf in orfs:
        for file in files:
            with open(file, "r") as f:
                lines_original = f.readlines()
                lines = "".join(lines_original)
                if f"begin(model({orf}))" in lines:
                    counter_orf_correl = 0
                    found_begining = False
                    found_ending = False
                    for line in lines_original:
                        if f"begin(model({orf}))" in line:
                            found_begining = True
                        if f"end(model({orf}))" in line:
                            found_ending = True
                        if found_begining and not found_ending:
                            if "tb_to_tb_evalue" in line:
                                counter_orf_correl += 1
                else:
                    continue
        resultado[orf] = counter_orf_correl
    return resultado

def multiple(clases):
    """
    Busca la relacion entre cada numero del 2-9
    y el numero de clases que tienen un dimension multiple de M y != 0

    :param clases: list - lista de todas las lases
    :return:  dict: dict - relacion entre cada numero del 2-9
    y el numero de clases que tienen un dimension multiple de M y != 0
    """
    dict = {}
    for i in range(2,10):
        aptos = []
        for clase in clases:
            for dimension in clase:
                dimension = int(dimension)
                is_multiple = dimension % i == 0
                if is_multiple and dimension != 0:
                    aptos.append(clase)
        dict[i] = aptos
    return dict


def print_bonito(dict):
    """
    Printa el diccionario de la forma M=key len(value) clases

    :param dict: dict- Cualquier diccionario
    :return: None
    """
    for key, values in dict.items():
        print(f"M={key}: {len(values)} clases")


def main():
    """
    Ejecución del programa

    :return: None
    """
    result, orfs, clases, descriptions = count_clases_orfs(ficheros)
    plot(result)

    frq, clase = freq_clase("respiration", result)
    print(format(f"Clase {clase} contiene {frq} ORFS"))

    listado = ["cytochrome"]
    clases_escogias, orfs_escogidos = clases_listado(clases, orfs, descriptions, listado)
    print(f"El numero de clases con al menos un ORF con al menos un patron de los listados es: {len(clases_escogias)}")

    resultado = promedio_orf(orfs_escogidos)
    plot(resultado)

    aptos = multiple(clases)
    print_bonito(aptos)



if __name__ == "__main__":
    main()



