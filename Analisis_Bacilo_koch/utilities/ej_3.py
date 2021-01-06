

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
        dict[i] = len(set(aptos))
    return dict


def print_bonito(dict):
    """
    Printa el diccionario de la forma M=key len(value) clases

    :param dict: dict- Cualquier diccionario
    :return: None
    """
    for key, values in dict.items():
        print(f"M={key}: {values} clases")
