import numpy as np

#grandeurs
xo = np.array([0.1]) #point initial
epsi = 0.0001 #epsilon
pas = 0.0001
nbrtourspc = 5
#on suppose avoir que des nombres entre 0 et 1


#définitions fonction de bases
def f(tab):
    return (tab[0] - 1/2)**2

def verif_point(p):
    for i in p:
        if i > 1 :
            return False
    return True

def point_valide(p, grad, pas):
    n = len(p)
    for i in range(n):
        if (p[i] - pas * grad[i]) < 0 or (p[i] - pas * grad[i]) > 1:
            grad[i] = 0
    return grad

def iemederive_part(fonc, point, i, pas):
    pnew = np.copy(point)
    ieme = point[i] + pas
    if ieme < 1:
        pnew[i] = ieme
        return (fonc(pnew) - fonc(point)) / pas
    else:
        pnew[i] = point[i]-pas
        return -(fonc(pnew) - fonc(point)) / pas


def gradient(fonc, pas, point):
    n = len(point)
    grad = np.zeros(n)
    for i in range(n):
        grad[i] = iemederive_part(fonc, point, i, pas)
    return point_valide(point, grad, pas)

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

print(v1grad(f, pas, xo, epsi))
