import random

def tri_selection(list):
    for i in range(len(list)):
        mini = i
        for j in range(i, len(list)):
            if list[j] < list[mini]:
                mini = j
            list[i], list[mini] =list[mini], list[i]
    return list


def tri_rapide(list):
    inferieur = []; pivot = []; superieur = []
    if len(list) < 2:
        return list
    pivotNombre = random.choice(list)
    for i in list:
        if i < pivotNombre:
            inferieur.append(i)
        elif i > pivotNombre:
            superieur.append(i)
        else:
            pivot.append(i)
    return tri_rapide(inferieur) + pivot + tri_rapide(superieur)
