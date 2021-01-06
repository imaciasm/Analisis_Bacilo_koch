from collections import Counter


def count_clases_orfs(ficheros):
    """
    Dado un fichero saca un diccionario con clase: numero_orfs

    Leemos el fichero linea a linea porque no tiene un formato tabla,
    cada linea es diferente y hay que elegir cual queremos y cual no.

    :param ficheros: str - Path al fichero de datos
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
                clase = numb1 + numb2 + numb3 + numb4
                descripcion = line.split(",")[-1].strip("),")
                orfs.append(orf)
                clases.append(clase)
                descriptions.append(descripcion)
    result = Counter(clases)
    return result, orfs, clases, descriptions
