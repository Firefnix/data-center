import numpy as np
from exploitation import T_proc, T_plaque, t
import matplotlib.pyplot as plt

def kelvin(T): # °C -> K
    return T + 273.15

def celsius(T): # K -> °C
    return T - 273.15

def D(x):
    assert 0 <= x <= L
    D_a = 2.25e-05 # m^2/s, à 298 K
    D_n = 8.7e-05
    if x < e:
        return D_n / u
    return D_a

def trouve_T_plaque(t_reel):
    if t_reel < t[0]:
        return T_plaque[0]
    i = 0
    while i < len(t) and t[i] < t_reel:
        i += 1
    if t_reel > t[-1]:
        return T_plaque[-1]
    return T_plaque[i]

u = 50 # trouvé en tâtonnant
alpha = 1 # idem, épaisseur de la couche d'air, 10 cm
e = 50e-3 # épaisseur du socle de l'ordinateur
Nx, L = 400, e + alpha # m
Xe = L / Nx

print(f'Pas spatial de {1000*Xe:.1f} mm')

S = 1 # surface, 85,60 mm × 53,98 mm, en m^2

tau = (10*e)**2 / D(0)
Nt = int((Nx**2) / (0.5))
gamma = (t[-1] - t[0]) / tau
Te = gamma * tau / Nt

print(f'Discrétisation espace×temps, {Nx}×{Nt}')

T = np.zeros((Nx+1, Nt+1))

T[:, 0] = kelvin(T_proc[0]) # condition initiale
for ti in range(Nt): # condition limite (1)
    T[0, ti] = kelvin(trouve_T_plaque(Te * ti))
T[-1, :] = kelvin(T_proc[0]) # condition limite (2)

A = np.array([(D(Xe * xi) * Te) / (Xe**2) for xi in range(Nx-1)])
B = 1 - 2*A

print(f'[debug] Valeurs min/max pour A : {min(A):.2f} / {max(A):.2f}')

for ti in range(Nt):
    T[1:Nx, ti+1] = A * (T[:Nx-1, ti] + T[2:, ti]) + B * T[1:Nx, ti]

x_pos = int(Nx * e / L) - 1

print(f'Durée de simulation : {tau:.2f}')
print(f'Durée d\'expérinence : {t[-1] - t[0]:.2f}')
rho, c = 1.16e3, 4.5 # kg.m^-3, kJ.K^-1.kg^-1
G = rho * c * D(0)
print(f'D = {D(0):.2e} m^2/s')
print(f'λ = {G:.2e} W.m^-1.K^-1')

if __name__ == '__main__':
    plt.rcParams.update({'font.size': 18})
    plt.grid()
    plt.plot(t - t[0], T_plaque, color='g', label='Plaque chauffante (expérience)')
    plt.plot(t - t[0], T_proc, color='b', label='Processeur (expérience)')
    plt.plot(Te*np.array(range(Nt)), celsius(T[x_pos, :-1]), color='red', label='Processeur (simulation)')
    plt.xlabel('Temps (s)')
    plt.ylabel('Température (°C)')
    plt.legend()
    plt.show()
