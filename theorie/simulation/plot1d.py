import numpy as np
import matplotlib.pyplot as plt
from constantes import celsius, kelvin, T0

dil = 100 # facteur de dilatation des longueurs
dilt = 1 # facteur de dilatation temporelle
fig = plt.figure()
ax = fig.add_subplot()

def plot_courbes(T, La, Nx, Nt):
    Ncourbes = 10
    positions = np.linspace(0, La*dil, Nx+1)
    c = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'black', 'grey', 'cyan']
    for n in range(Ncourbes):
        plt.plot(positions, T[:, int(Nt/dilt*(n/Ncourbes)**2)] - kelvin(0), color=c[n],
            label=f't = {(n/Ncourbes)**2:.2f} τ')

def plot_zones(Tmax, Lp, L, La):
    plt.vlines(x=[dil*(La-Lp)/2, dil*(La+Lp)/2], ymin=celsius(T0),
        ymax=celsius(Tmax), colors='blue', ls='--', lw=2, label='Source')
    plt.vlines(x=[dil*(La-L)/2, dil*(La+L)/2], ymin=celsius(T0),
        ymax=celsius(Tmax), colors='grey', ls='--', lw=2, label='Carcasse')

def legende(L):
    ax.annotate('T0', xy=(L, celsius(T0)))
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.xlabel('x (en cm)')
    plt.ylabel('T (en °C)')

def plot(T, Lp, L, La, Nx, Nt):
    Tmax = max(T[:, int(Nt/dilt)])
    plot_courbes(T, La, Nx, Nt)
    plot_zones(Tmax, Lp, L, La)
    legende(L)
    plt.show()
