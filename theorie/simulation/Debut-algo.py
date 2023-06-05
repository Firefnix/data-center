import numpy as np
from multiple import fixe_K, energie

#on suppose avoir que des nombres entre 0 et 1
def main():
    fixe_K(1e6)
    n = 3 # nombre d'ordinateurs
    x0 = point_initial(n)
    epsilon = 5. # epsilon
    pas = 0.02
    xf = v1grad(energie, pas, x0, epsilon)
    print(f'Point initial : {x0}')
    print(f'Point final : {xf}')

#définitions fonction de bases
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
def v1grad(f, pas, x0, epsilon):
    point = x0
    while True:
        print(f'Actuellement au point {point}')
        nablaf = gradient(f, pas, point)
        n = norme(nablaf)
        print(f'\tGradient : {nablaf}, de norme {n}')
        if n < epsilon:
            break
        point = point - pas * nablaf
    return point

def point_initial(n):
    l = []
    for i in range(n):
        l.append((i+1) / (n+2))
    for i in range(n):
        l.append(1 / n)
    return np.array(l)

if __name__ == '__main__':
    main()
