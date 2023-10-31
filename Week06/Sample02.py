'''
1. random --> randint()
2. list
3. random function
4. turtle 
'''

import random as r

t = list()
print(t)
t.append(10)
t.append(1)
t.append(3)
t.append(4)
t.append(6)
t.append(7)
t.append(4)
t.append(-3)
t.append(99)
print(t)



def randomSel(targetList):
    return targetList[r.randint(0, len(targetList)-1)]


print(randomSel(t))