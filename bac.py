from random import randint
def est_valide(i:int,j:int,n:int,m:int)->bool:
    """
    :param i: La coordonnée en abscisse (N+)
    :param j: La coordonnée en ordonnée (N+)
    :param n: La coordonnée maximale (N+)
    :param m: La coordonnée maximale (N+)
    :return: Vrai ou Faux
    """
    return 0<=i<n and 0<=j<m

def voisines(i:int,j:int,lab:list)->list:
    lv = []
    if est_valide(i+1,j,len(lab),len(lab[j])) and lab[j][i+1] not in {1, 4}:
        lv.append((j, i+1))
    if est_valide(i-1,j,len(lab),len(lab[j])) and lab[j][i-1] not in {1, 4}:
        lv.append((j, i-1))
    if est_valide(i,j-1,len(lab),len(lab[j])) and lab[j-1][i] not in {1, 4}:
        lv.append((j-1, i))
    if est_valide(i,j+1,len(lab),len(lab[j])) and lab[j+1][i] not in {1, 4}:
        lv.append((j+1, i))
    return lv

def resolution(lab:list)->list:
    for j in range(len(lab)):
        for i in range(len(lab[j])):
            if lab[j][i] == 2:
                depart = (j,i)
            if lab[j][i] == 3:
                arrive = (j,i)
    chemin = []
    coordonne = depart
    chemin.append(coordonne)
    while chemin[-1] != arrive:
        voisins = voisines(coordonne, lab)
        if voisins == []:
            chemin.pop()
            coordonne = chemin[-1]
        else:
            coordonne = voisins[randint(a=0, b=(len(voisins)-1))]
            chemin.append(coordonne)
