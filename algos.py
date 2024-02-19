class File:
    """ classe File
    création d'une instance File avec une liste
    """
    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)

    def enfiler(self,x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[0]

    def present(self,x):
        return x in self.L

    
G = dict()
G['a'] = ['b','c']
G['b'] = ['a','d','e']
G['c'] = ['a','d']
G['d'] = ['b','c','e']
G['e'] = ['b','d','f','g']
G['f'] = ['e','g']
G['g'] = ['e','f','h']
G['h'] = ['g']
def voisins(G,sommet):
    return G[sommet]

def BFS(Gr):
    f, v = File(), []
    f.enfiler(list(Gr.keys())[0])
    while not f.vide():
        t = f.defiler()
        v.append(t)
        for i in voisins(Gr, t):
            if not f.present(i) and i not in v:
                f.enfiler(i)
    return v

print(BFS(G))


def bfs_recur(G:dict,f:File,sommets_visites:[]):
    if f.vide():
        return None
    tmp=f.defiler()
    print(tmp,end=" ")
    for u in voisins(G,tmp):
        if u not in sommets_visites:
            sommets_visites.append(u)
            f.enfiler(u)
    bfs_recur(G,f,sommets_visites)
f=File()
sommets_visites=[]
sommet = 'b'
f.enfiler(sommet)
sommets_visites.append(sommet)
bfs_recur(G,f,sommets_visites)


