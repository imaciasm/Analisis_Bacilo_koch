import matplotlib.pyplot as plt


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
