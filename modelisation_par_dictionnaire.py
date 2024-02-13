import pygraphviz as pgv

def dessine_graphe(nom_fichier="graphe_activite_intro"):
    """Génère un fichier image correspondant au graphe de l' activité
    d' introduction du chapitre
    """
    G = pgv.AGraph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('A', 'D')
    G.add_edge('B', 'D')
    G.add_edge('C', 'D')
    G.add_edge('C', 'E')
    G.add_edge('D', 'E')
    G.add_edge('D', 'F')
    G.add_edge('E', 'F')
    G.graph_attr['label'] = "Graphe de l' activité d' introduction"
    G.layout()
    G.draw(nom_fichier+".png", prog="circo")


def ordre(un_graphe : dict) -> int :
    """Calcul l' ordre d' un graphe modélisé sous forme d' un dictionnaire
    @params :
    - un_graphe : de type dict
    @returns :
    - de type int, l' ordre du graphe
    """
    return len(un_graphe.keys())

def degre(un_graphe:dict, un_noeud:str) -> int :
    """Calcul le degré d' un noeud dans un graphe modélisé sous forme d' un dictionnaire
    @params :
    - un_graphe : de type dict
    - un_noeud : de type str
    @returns :
    - de type int, le degré du noeud
    """
    if un_noeud in un_graphe :
        return len(un_graphe[un_noeud])
    else :
        return None

def sommets_adjacents(un_graphe:dict, un_noeud:str) -> list :
    """Donne la liste des noeuds adjacents à un noeud dans un graphe modélisé sous forme d' un dictionnaire
    @params :
    - un_graphe : de type dict
    - un_noeud : de type str
    @returns :
    - de type list : Liste des noeuds adjacents
    """
    if un_noeud in un_graphe :
        return un_graphe[un_noeud]
    else :
        return None

def lister_aretes(un_graphe:dict, un_noeud:str) -> list :
    """Donne la liste des noeuds adjacents à un noeud dans un graphe modélisé sous forme d' un dictionnaire
    @params :
    - un_graphe : de type dict
    - un_noeud : de type str
    @returns :
    - de type list : Liste des noeuds adjacents
    """
    if un_noeud in un_graphe :
        return un_graphe[un_noeud]
    else :
        return None

def plus_d_amis(un_graphe:dict)->str:
    """Donne le sommet qui a le plus d' arêtes (ou le sommet qui a les plus d' amis)
    dans un graphe modélisé sous forme d' un dictionnaire
    @params :
    - un_graphe : de type dict
    @returns :
    - de type str : Label du sommet
    """
    noeud_max = None
    nb_amis_max = None
    for noeud in un_graphe.keys():
        nb_amis = degre(un_graphe, noeud)
        if nb_amis_max==None or nb_amis_max<nb_amis :
            nb_amis_max = nb_amis
            noeud_max = noeud
    return noeud_max

def dico_to_matrix(un_graphe:dict)->list:
    """Transforme un graphe modélisé sous forme d' un dictionnaire
    en un graphe modélisé sous forme de liste de listes (ou matrice)
    @params :
    - un_graphe : de type dict
    @returns :
    - de type list de list
    """
    ma_matrice = []
    for i in range(len(un_graphe)):
        une_ligne = [0]*len(un_graphe)
        ma_matrice.append(une_ligne)
    #print(ma_matrice)
    tous_les_noeuds = list(un_graphe.keys())
    #print(tous_les_noeuds)
    for un_noeud in tous_les_noeuds:
        sommets_adjacents = un_graphe[un_noeud]
        #print(sommets_adjacents)
        for sommet in sommets_adjacents :
            ma_matrice[tous_les_noeuds.index(un_noeud)][tous_les_noeuds.index(sommet)] = 1
            #print(ma_matrice)
    return ma_matrice

def dico_to_matrix2(un_graphe:dict)->list:
    """Transforme un graphe modélisé sous forme d' un dictionnaire
    en un graphe modélisé sous forme de liste de listes (ou matrice)
    Attention, les labels de sommets sont précisés sur la 1ère ligne
    et la 1ère colonne
    @params :
    - un_graphe : de type dict
    @returns :
    - de type list de list
    """
    tous_les_noeuds = list(un_graphe.keys())
    ma_matrice = [[None] + tous_les_noeuds]
    for i in range(len(un_graphe)):
        une_ligne = [0]*(len(un_graphe))
        ma_matrice.append([tous_les_noeuds[i]]+une_ligne)
    #print(ma_matrice)
    #print(tous_les_noeuds)
    for un_noeud in tous_les_noeuds:
        sommets_adjacents = un_graphe[un_noeud]
        #print(sommets_adjacents)
        for sommet in sommets_adjacents :
            ma_matrice[tous_les_noeuds.index(un_noeud)+1][tous_les_noeuds.index(sommet)+1] = 1
            #print(ma_matrice)
    return ma_matrice

def matrix_to_dico(une_matrice2:list)->dict:
    """Transforme un graphe modélisé sous forme de liste de listes (ou matrice)
    en un graphe modélisé sous forme d' un dictionnaire
    @params :
    - une_matrice2 : de type list de list
    @returns :
    - de type dict
    """
    mon_dico = {}
    for elem in une_matrice2[0][1:]:
        mon_dico[elem] = []
    for ligne in une_matrice2[1:]:
        cle = ligne[0]
        for i in range(1,len(ligne)) :
            if ligne[i]==1 :
                #print(mon_dico)
                mon_dico[cle].append(une_matrice2[0][i])
    #print(mon_dico)
    return mon_dico

def dico_to_graph(un_graphe:dict, nom_fichier="dico_to_graph"):
    """Transforme un graphe modélisé sous forme d' un dictionnaire
    en un fichier image (par défaut : 'dico_to_graph')
    @params :
    - un_graphe : de type dict
    - nom_fichier : de type str, nom du fichier .png
    @returns :
    - None
    """
    G = pgv.AGraph()
    for sommet1 in un_graphe:
        for sommet2 in un_graphe[sommet1] :
            G.add_edge(sommet1, sommet2)
    G.graph_attr['label'] = "Graphe de l' activité d' introduction"
    G.layout()
    G.draw(nom_fichier+".png", prog="circo")

def matrix_to_graph(un_graphe:list, labels_sommets:list, nom_fichier="matrix_to_graph"):
    """Transforme un graphe modélisé sous forme d' une matrice
    en un fichier image (par défaut : 'matrix_to_graph')
    @params :
    - un_graphe : de type list de list
    - labels_sommets : de type list, tous les labels des sommets
    - nom_fichier : de type str, nom du fichier .png
    @returns :
    - None
    """
    G = pgv.AGraph()
    for num_ligne in range(len(un_graphe)):
        for num_colonne in range(len(un_graphe[num_ligne])) :
            if un_graphe[num_ligne][num_colonne] != 0:
                G.add_edge(labels_sommets[num_ligne], labels_sommets[num_colonne])
    G.graph_attr['label'] = "Graphe de l' activité d' introduction"
    G.layout()
    G.draw(nom_fichier+".png", prog="circo")

def matrix_to_dico2(une_matrice2:list, labels_sommets)->dict:
    """Transforme un graphe modélisé sous forme de matrice pondérée
    en un graphe modélisé sous forme d' un dictionnaire'
    @params :
    - une_matrice2 : de type list de list
    - labels_sommets : de type list, labels de tous les sommets
    @returns :
    - de type dict
    """
    mon_dico = {}
    for label in labels_sommets :
        mon_dico[label] = []
    for num_ligne in range(len(une_matrice2)):
        for num_colonne in range(len(une_matrice2[0])):
            coef = une_matrice2[num_ligne][num_colonne]
            if coef!=0:
                mon_dico[labels_sommets[num_ligne]].append((labels_sommets[num_colonne], coef))
    return mon_dico

def dessine_graphe(nom_fichier="graphe_oriente_activite_intro"):
    """Génère un fichier image correspondant au graphe orienté
    """
    G = pgv.AGraph(directed=True)
    G.add_edge('A', 'B')
    G.add_edge('A', 'E')
    G.add_edge('B', 'F')
    G.add_edge('C', 'A')
    G.add_edge('C', 'B')
    G.add_edge('D', 'A')
    G.add_edge('D', 'C')
    G.add_edge('E', 'D')
    G.add_edge('F', 'C')
    G.add_edge('F', 'E')
    G.graph_attr['label'] = "Graphe orienté"
    G.layout()
    G.draw(nom_fichier+".png", prog="circo")

mon_graphe = {}

mon_graphe['A'] = ['B', 'C', 'D']
mon_graphe['B'] = ['A', 'D']
mon_graphe['C'] = ['A', 'D', 'E']
mon_graphe['D'] = ['A', 'B', 'C', 'E']
mon_graphe['E'] = ['C', 'D', 'F']
mon_graphe['F'] = ['D', 'E']

ma_matrice = [[0,1,1,1,0,0],
              [1,0,0,1,0,0], 
              [1,0,0,1,1,0], 
              [1,1,1,0,1,1], 
              [0,0,1,1,0,1], 
              [0,0,0,1,1,0]]

ma_matrice2 = [[None,'A','B','C','D','E','F'],
              ['A',0,1,1,1,0,0],
              ['B',1,0,0,1,0,0], 
              ['C',1,0,0,1,1,0], 
              ['D',1,1,1,0,1,1], 
              ['E',0,0,1,1,0,1], 
              ['F',0,0,0,1,1,0]]

ma_matrice_ponderee = [[ 0,12,20, 9, 0, 0, 0],
                       [12, 0, 0, 0, 0, 0,13], 
                       [20, 0, 0, 8, 0,11, 7], 
                       [ 9, 0, 8, 0, 0,21, 0], 
                       [ 0, 0, 0, 0, 0, 3, 9], 
                       [ 0, 0,11,21, 3, 0, 5],
                       [ 0,13, 7, 0, 9, 5, 0]]

dessine_graphe()
print("clés du graphe : ", mon_graphe.keys())
print("valeurs du graphe : ", mon_graphe.values())
print("ordre du graphe : ", len(mon_graphe))
print("sommets en lien avec D : ", mon_graphe['D'])
print("ordre du graphe : ", ordre(mon_graphe))
print("degré du noeud D : ", degre(mon_graphe, 'D'))
print("degré du noeud K : ", degre(mon_graphe, 'K'))
print("liste des noeuds adjacents du noeud D : ", sommets_adjacents(mon_graphe, 'D'))
print("liste des noeuds adjacents du noeud K : ", sommets_adjacents(mon_graphe, 'K'))
print("le noeud qui a le plus d' amis est : ", plus_d_amis(mon_graphe))
print("la matrice d' adjacence est : ", dico_to_matrix(mon_graphe))
print("la matrice d' adjacence est : ", dico_to_matrix2(mon_graphe))
print("le dictionnaire d' adjacence est : ", matrix_to_dico(ma_matrice2))
print("fonction dico_to_graph ", dico_to_graph(mon_graphe))
print("fonction matrix_to_graph ", matrix_to_graph(ma_matrice, ['A','B','C','D','E','F']))
print("le dictionnaire d' adjacence pondéré est : ", matrix_to_dico2(ma_matrice_ponderee, ['A','B','C','D','E','F','G']))