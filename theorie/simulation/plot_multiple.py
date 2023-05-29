import numpy as np
import matplotlib.pyplot as plt
from constantes import L, l, lp, celsius

_couleurs = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'black', 'grey', 'cyan']

def plot_puissance(P, Te):
    Nt = len(P)
    t = Te * np.arange(0., Nt)
    plt.plot(t, P)
    plt.xlabel('t (en s)')
    plt.ylabel('P (en W)')
    plt.title('Puissance totale des processeurs')
    # plt.legend()
    plt.show()

def plot_processeurs(T, X, Te, Xe):
    n = len(X)
    Nt = len(T[0, :])
    t = Te * np.arange(0., Nt)
    for i in range(n):
        plt.plot(t, celsius(T[int(X[i] / Xe), :]), color=_couleurs[i],
            label=f'Processeur {i+1} en x = {X[i]}')
    plt.xlabel('t (en s)')
    plt.ylabel('T (en °C)')
    plt.title(f'Températures aux {n} processeurs')
    plt.legend()
    plt.show()

def plot_final(T, X, Nx):
    Tf = T[:, -1]
    Tmin, Tmax = min(Tf), max(Tf)
    x = np.linspace(0, L, Nx+1)
    plt.plot(x, celsius(Tf))
    _plot_zones(Tmin, Tmax, X)
    plt.xlabel('x (en m)')
    plt.ylabel('T (en °C)')
    plt.legend()
    plt.show()

def _plot_zones(Tmin, Tmax, X):
    for i in range(len(X)):
        plt.vlines(x=[X[i]-lp/2, X[i]+lp/2], ymin=celsius(Tmin),
            ymax=celsius(Tmax), colors=_couleurs[i], ls='--', lw=.5) # source
        plt.vlines(x=[X[i]-l/2, X[i]+l/2], ymin=celsius(Tmin),
            ymax=celsius(Tmax), colors=_couleurs[i], ls='-', lw=.2, label=f'Ordinateur {i+1}')
