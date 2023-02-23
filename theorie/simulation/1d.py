from enum import Enum, auto
import numpy as np
from plot1d import plot
from constantes import T0, Da0, D, c

hyp = 'B' # hypothèse

La, L, Lp = 1, 1e-1, 1e-2 # m
if hyp == 'A': La = L
S = 1e-4 # m^2
tau = La**2 / D # s
print(f'τ = {tau:.2f} s')
Nx = 300

A = 0.5
B = 1 - 2*A

Xe = La / Nx
Nt = int((Nx**2) / A)
Te = tau / Nt
print(f'Discrétisation espace×temps, {Nx}×{Nt}')

P = 0.05 # W
Cp = c * S * Lp # J.K^-1

class Zone(Enum):
    source = auto()
    carc = auto()
    air = auto()

def zone(xi) -> Zone:
    X = (xi+1) * Xe
    if (La-Lp)/2 <= X <= (La+Lp)/2:
        return Zone.source
    if (La-L)/2 <= X <= (La+L)/2:
        return Zone.carc
    return Zone.air

def Dx(xi):
    if zone(xi) == Zone.air:
        return Da0
    return D
Ax = np.array([(Dx(xi) * Te) / (Xe**2) for xi in range(Nx-1)])
print(f'Constante A : {(Da0 * Te) / (Xe**2):.2f} (air)')
print(f'Constante A : {(D * Te) / (Xe**2):.2f} (ordinateur)')
Bx = 1 - 2*Ax

P_c = np.zeros(Nx-1)
for xi in range(Nx-1):
    if zone(xi) == Zone.source:
        P_c[xi] = P / Cp

T = np.zeros((Nx+1, Nt+1))
def hypA(T): # air thermostat
    T[0, :] = T0
    T[-1, :] = T0
def hypB(T, ti): # continuité aux bords
    T[0, ti+1] = T[1, ti+1]
    T[-1, ti+1] = T[-2, ti+1]

T[:, 0] = T0
if hyp == 'A': hypA(T)

for ti in range(Nt):
    T[1:Nx, ti+1] = Ax * (T[:Nx-1, ti] + T[2:, ti]) + Bx * T[1:Nx, ti] + Te * P_c
    if hyp == 'B': hypB(T, ti)

plot(T, Lp, L, La, Nx, Nt)
