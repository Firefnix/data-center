import numpy as np
from constantes import h_en_s, s_en_h, T0, P_ordinateur, L, l, lp, D, S, c, rho, Da0
from plot_multiple import plot_puissance, plot_processeurs, plot_final

DEBUG = False
tau = h_en_s(4)
t_sim = h_en_s(12)
Nx = 200
Xe = L / Nx
Nt = int((Nx**2) / (0.5)) # 0.5 est une constante magique
N_sim = int(Nt * t_sim / tau)
Te = tau / Nt

def fixe_K(val):
    global _K
    _K = val

def donne_K():
    return _K

def pstat(args: np.ndarray) -> float:
    P, T, X, K, _ = f(args)
    return sum(P[-1, :])

def f(args: np.ndarray) -> float:
    X, n = _positions(L, args)
    K = _calculs(args)
    T = _condition_initiale(Nx, N_sim, T0)
    _condition_limite_A(T)
    _initialise_zones(X)
    P = np.zeros((N_sim, n))
    A = (Dx() * Te) / (Xe**2)
    B = 1 - 2*A
    if DEBUG: print(f'[debug] Valeurs min/max pour A : {min(A):.2f} / {max(A):.2f}')
    Pc0 = None
    for ti in range(N_sim):
        P_ti, Pc = _puissances(T[:, ti], K, X)
        if ti == N_sim-1: Pc0 = Pc
        P[ti] = P_ti
        T[1:Nx, ti+1] = A * (T[:Nx-1, ti] + T[2:, ti]) + B * T[1:Nx, ti] + Te * Pc
        # _condition_limite_B(T, ti)
    return P, T, X, K, Pc0

def _condition_initiale(Nx, Nt, T0) -> np.ndarray:
    T = np.zeros((Nx+1, Nt+1))
    T[:, 0] = T0
    return T

def _condition_limite_A(T):
    T[0, :] = T0
    T[-1, :] = T0

def _condition_limite_B(T, ti): # continuité de la température aux bords
    T[0, ti+1] = T[1, ti+1]
    T[-1, ti+1] = T[-2, ti+1]

def _positions(L, args):
    assert len(args) % 2 == 0
    return L * args[:len(args) // 2], len(args) // 2

def _calculs(args):
    assert len(args) % 2 == 0
    k = args[len(args) // 2:]
    return donne_K() / sum(k) * k

def _puissances(T, K, X):
    Cp = lp * S * rho * c
    n = len(X)
    pc = np.zeros(Nx-1)
    n = len(X)
    p_tab = [P_ordinateur(K[i], T[int(X[i] // Xe)]) for i in range(n)]
    for z in range(n):
        for xi in POSITIONS[z]:
            pc[xi] = p_tab[z] / Cp
    return p_tab, pc

CARCASSE = -1
AIR = -2

def _initialise_zones(X):
    assert _pas_de_conflit(X)
    global ZONES
    global POSITIONS
    ZONES = np.zeros(Nx-1, dtype=int)
    POSITIONS = {i: [] for i in range(len(X))}
    POSITIONS[AIR] = []
    POSITIONS[CARCASSE] = []
    for xi in range(Nx-1):
        z = _zone(xi, X)
        ZONES[xi] = z
        POSITIONS[z].append(xi)

def _pas_de_conflit(X):
    return True

def _zone(xi, X) -> int:
    """Un entier positif si on est dans la i-ème source,
    -1 si on est dans une carcasse, et -2 si on est dans l'air"""
    x = (xi+1) * Xe
    n = len(X)
    for i in range(n):
        if X[i] - lp/2 <= x <= X[i] + lp/2:
            return i
    for i in range(n):
        if X[i] - l/2 <= x <= X[i] + l/2:
            return CARCASSE
    return AIR

def Dx() -> np.ndarray: # K -> m^2/s
    d_tab = np.zeros(Nx-1)
    for xi in range(Nx-1):
        if ZONES[xi] == AIR:
            d_tab[xi] = Da0
        else:
            d_tab[xi] = D
    return d_tab

def Ax(T: np.ndarray): # K -> 1
    return np.array([(Dx(xi, T0) * Te) / (Xe**2) for xi in range(Nx-1)])

def Bx(T: np.ndarray): # K -> 1
    return 1 - 2 * Ax(T)

def hypB(T, ti): # continuité aux bords
    T[0, ti+1] = T[1, ti+1]
    T[-1, ti+1] = T[-2, ti+1]

if __name__ == '__main__':
    print(f'Discrétisation espace×temps, {Nx}×{N_sim}')
    fixe_K(1e6)
    print(f'Unité spatiale : {Xe:.2f} m')
    print(f'Unité temporelle : {Te:.2f} s, durée totale : {s_en_h(t_sim):.1f} h')
    P, T, X, K, Pc0 = f(np.array((.01, .03, .965, .99, .5, .1, .1, .6)))
    # P, T, X, K, Pc0 = f(np.array((.47, .49, .51, .53, .6, .4, .3, .65)))
    # P, T, X, K, Pc0 = f(np.array((.1, .25, .4, .9, .3, .3, .3, .3)))
    # P, T, X, K = f(x_min)
    E = Te * P.sum()
    print(f'Énergie totale consommée : {int(E)} J soit {E / 3.6e6:.2f} kWh')
    print(f'Puissance en régime stationnaire : {sum(P[-1, :]):.2f} W')
    # plot_D(Dx(), X)
    # plot_pc_initial(Pc0, X)
    # plot_initial(T, X, Nx)
    plot_final(T, X, Nx)
    plot_puissance(P, Te)
    plot_processeurs(T, X, Te, Xe)
