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





print(G)
print(G.keys())
print(G.values())
print(ordre(G))
print(degre(G, "e"))