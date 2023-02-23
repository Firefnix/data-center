import numpy as np


# Carcasse de l'ordinateur
Lx, Ly, Lz = 10e-2 # m : 10 cm
c_ord = 1000 # J.K^-1.kg^-1
V_ord = Lx * Ly * Lz
rho_ord = 1000 # kg.m^-3
S_ord = (2 * Lx * Ly) + (2 * Ly * Lz) + (2 * Lx * Lz)

# Carcasse du processeur
# T désigne la température du processeur
lx, ly, lz = 1e-2 # m : 1 cm
c_proc = 1000 # J.K^-1.kg^-1
V_proc = lx * ly * lz
rho_proc = 1000 # kg.m^-3
S_proc = (2 * lx * ly) + (2 * ly * lz) + (2 * lx * lz)

# Discrétisation du temps et de l'espace
dd = Lx / 100
dt = 1000 # s

# Salle (air)

U = 5 # V
def I(K, T):
    return ...
def P(K, T): return U * I(K, T)
def Pv(K, T): return P(K, T) / V_proc
