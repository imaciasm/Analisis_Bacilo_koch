import os
import glob

def promedio_orf(patron_orfs):
    """
    Funcion que busca cuantos ORF están relacionados con otro

    :param orfs: list - lista de orfs
    :return: resultado: dict - relacion entre cada ORF y el numero de ORFS correlacionados
    con este
    """
    ficheros = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data/orfs/tb_data*")
    files = glob.glob(ficheros)
    resultado = {}
    for patron, orfs in patron_orfs.items():
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
            resultado[patron] = counter_orf_correl
    return resultado
