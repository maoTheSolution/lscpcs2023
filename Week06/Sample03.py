import random as r

def makeList() -> list:
    saved = list()
    while(True):
        temp = r.randint(0, 101)
        if temp not in saved:
            saved.append(temp)
        if len(saved) == 101:
            break

    return saved




