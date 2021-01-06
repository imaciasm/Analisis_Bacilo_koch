

def freq_clase(descripcion, frq_clase_orf, ficheros):
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
                break
    return frq_clase_orf[clase], clase