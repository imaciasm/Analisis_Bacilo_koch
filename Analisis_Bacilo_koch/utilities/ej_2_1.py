


def clases_listado(clases, orfs, descriptions, listado):
    """
    Dado un listado de patrones busca las clases las
    clases que contienen ORFs con esa descripcion y
    sus ORFS

    :param clases: lista de todas las clases
    :param orfs: lista de todos los orfs
    :param descriptions: listas de todas las descripciones
    :param listado: listado de patrones
    :return: clases_escogidas: list - clases con ORFS con el patron
             ORFS_escogidos: list - ORFS con el menos un patron de los listados
    """
    clases_escogidas = {}
    orfs_escogidos = {}
    for patron in listado:
        clases_patron = []
        orfs_patron = []
        for clase, orf, description in zip(clases, orfs, descriptions):
            if patron.lower() in description:
                clases_patron.append(clase)
                orfs_patron.append(orf)
        clases_escogidas[patron] = len(set(clases_patron))
        orfs_escogidos[patron] = set(orfs_patron)
    return clases_escogidas, orfs_escogidos
