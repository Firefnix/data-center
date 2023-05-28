import numpy as np
# Grandeurs
xo = np.array([10.]) # point initial
epsi = 0.01 # epsilon
pas = 0.01
nbrtourspc = 5
x = 10 # m
y = 10 # m
K = 1000 # calculs par secondes


#définitions fonction de bases
def f(tab):
    return (tab[0] - 3)**2

def iemederive_part(fonc, point, i, pas):
    pnew = np.copy(point)
    pnew[i] = point[i] + pas
    return (fonc(pnew) - fonc(point)) / pas

def gradient(fonc, pas, point):
    n = len(point)
    grad = np.zeros(n)
    for i in range(n):
        grad[i] = iemederive_part(fonc, point, i, pas)
    return grad

def norme (vect):
    somme = 0
    for i in vect:
        somme += i**2
    return np.sqrt(somme)

#algo
def v1grad(f, pas, xo, epsi):
    point = xo
    while True:
        nablaf = gradient(f, pas, point)
        n = norme(nablaf)
        if n < epsi:
            break
        point = point - pas * nablaf
    return point

print('Minimum atteint en :', v1grad(f, pas, xo, epsi))
