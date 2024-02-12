G = dict()
G["a"] = ["b","c"]
G["b"] = ["a","d","e"]
G["c"] = ["a","d"]
G["d"] = ["b","c","e"]
G["e"] = ["b","d","f","g"]
G["f"] = ["e","g"]
G["g"] = ["e","f","h"]
G["h"]= ["g"]

def ordre(Gr:dict)->int:
    return len(Gr.keys())

def degre(Gr:dict, S)->int:
    if Gr[S] == []:
        return -1
    else:
        return len(Gr[S])

def sommets_adjacents(Gr:dict, S)->list:
    try:
        return Gr[S]
    except:
        return -1

def lister_aretes(Gr: dict) -> list:
    arretes = []
    for sommet in Gr.keys():
        for voisin in Gr[sommet]:
            if (voisin, sommet) not in arretes and (sommet, voisin) not in arretes:
                arretes.append((sommet, voisin))
    return arretes

def abonne_max_amis(Gr: dict):
    abonne_max = ""
    max_amis = 0
    for abonne in Gr.keys():
        amis = Gr[abonne]
        if len(amis) > max_amis:
            max_amis = len(amis)
            abonne_max = abonne

    return f"L'abonné du réseau social avec le plus grand nombre d'amis à savoir {max_amis} est {abonne_max}.\
    \nSes amis sont : {Gr[abonne_max]}."



print(G)
print(G.keys())
print(G.values())
print(ordre(G))
print(degre(G, "e"))


liste_sommets=['a','b','c','d','e','f','g','h']
n=len(liste_sommets)
matrice=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if liste_sommets [j] in G[liste_sommets [i]]:
            matrice[i][j]=1
print(matrice)


def dico_to_matrix(Gr: dict) -> list:
    nombre_de_noeuds = len(Gr)
    matrix = [[0] * nombre_de_noeuds for _ in range(nombre_de_noeuds)]
