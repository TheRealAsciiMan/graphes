class File:
    """ classe File
    création d’une instance File avec une liste
    """

    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def defiler(self):
        assert not self.vide(), "file vide"
        return self.L.pop(0)

    def enfiler(self, x):
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[0]

    def present(self, x):
        return x in self.L


def detect_cycle(Gr):
    Cycle_present = False
    drapeaux = [-1] * len(Gr)  # Initialisation des drapeaux à -1
    f = File()
    f.enfiler(list(Gr.keys())[0])  # Commencer par un sommet quelconque
    while not f.vide():
        courant = f.defiler()
        drapeaux[courant] = 1
        for voisin in Gr[courant]:
            if drapeaux[voisin] == 0:
                print("On a déjà rencontré ce sommet ! Il y a un cycle.")
                Cycle_present = True
            elif drapeaux[voisin] == -1:
                f.enfiler(voisin)
    return Cycle_present