import random

class Pile:
    """ classe Pile
    création d'une instance Pile avec une liste
    """
    def __init__(self):
        self.L = []
    def vide(self):
        return self.L == []
    def depiler(self):
        assert not self.vide(),"Pile vide"
        return self.L.pop()
    def sommet(self):
        assert not self.vide(),"Pile vide"
        return self.L[-1]
    def empiler(self,x):
        self.L.append(x)

def voisins(G,sommet):
    return G[sommet]

def dfs(Gr):
    sommets_visités = []
    sommets_fermés = []
    p = Pile()
    sommets_visités.append(list(Gr.keys())[0])
    p.empiler(list(Gr.keys())[0])
    while not p.vide():
        tmp = p.sommet()
        voisins_list = [y for y in voisins(G, tmp) if y not in sommets_visités]
        # voisins_list = []
        # for voisin in voisins(Gr, tmp):
        #     if voisin not in sommets_visités:
        #         voisins_list.append(voisin)
        if voisins_list != []:
            v = random.choice(voisins_list)
            sommets_visités.append(v)
            p.empiler(v)
        else:
            sommets_fermés.append(tmp)
            p.depiler()
    return sommets_fermés

def dfs_rc(Gr, s):
    sommets_visités = []
    def dfs(Gr, s):
        if s not in sommets_visités:
            sommets_visités.append(s)
        voisins_list = [y for y in voisins(Gr, s) if y not in sommets_visités]
        for voisin in voisins_list:
            dfs(Gr, voisin)
        return sommets_visités
    return dfs(Gr, s)

def Solution(end:str, parents:dict):
    chemin = []
    courant = end
    while courant != None:
        chemin = [courant] + chemin
        courant = parents[courant]
    return chemin

G = dict()
G['a'] = ['b','c']
G['b'] = ['a','d','e']
G['c'] = ['a','d']
G['d'] = ['b','c','e']
G['e'] = ['b','d','f','g']
G['f'] = ['e','g']
G['g'] = ['e','f','h']
G['h'] = ['g']

print(dfs(G))
print(dfs_rc(G, 'g'))
print(dfs_rc(G, 'g')[::-1])
