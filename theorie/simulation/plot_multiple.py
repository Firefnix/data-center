import numpy as np
import matplotlib.pyplot as plt
from constantes import s_en_h, L, l, lp, celsius

_couleurs = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'black', 'grey', 'cyan']

plt.rcParams.update({'font.size': 18})

def plot_pc_initial(Pc, X):
    Nx = 1+len(Pc)
    x = np.linspace(0., L, Nx)
    plt.plot(x[:-1], Pc)
    _plot_zones_D(min(Pc), max(Pc), X)
    plt.title('$P_c$ à l\'état final')
    plt.xlabel('Position $x$ (en m)')
    plt.ylabel('$P_c$ ($K/s$)')
    plt.show()

def plot_D(D, X):
    Nx = 1+len(D)
    x = np.linspace(0., L, Nx)
    d = 1e6*D
    plt.plot(x[:-1], d)
    _plot_zones_D(min(d), max(d), X)
    plt.xlabel('Position $x$ (en m)')
    plt.ylabel('Diffusivité $D$ ($10^{-6} m^2/s$)')
    plt.show()

def plot_puissance(P, Te):
    Nt, n = P.shape
    t = s_en_h(Te * np.arange(0., Nt))
    # P_tot = np.array([sum(P[i, :]) for i in range(Nt)])
    for i in range(n):
        plt.plot(t, P[:, i], label=f'Ordinateur {i+1}', color=_couleurs[i])
    # plt.plot(t, P_tot, label='Puissance totale')
    plt.xlabel('t (en h)')
    plt.ylabel('P (en W)')
    plt.title('Puissance des ordinateurs')
    plt.legend()
    plt.show()

def plot_processeurs(T, X, Te, Xe):
    n = len(X)
    Nt = len(T[0, :])
    t = s_en_h(Te * np.arange(0., Nt))
    for i in range(n):
        plt.plot(t, celsius(T[int(X[i] / Xe), :]), color=_couleurs[i],
            label=f'Processeur {i+1} en $x$ = {int(100*X[i])} cm')
    plt.xlabel('t (en h)')
    plt.ylabel('T (en °C)')
    plt.title(f'Températures aux {n} processeurs')
    plt.legend()
    plt.show()

def plot_initial(T, X, Nx):
    Ti = T[:, 0]
    Tmin, Tmax = min(Ti), max(Ti)
    x = np.linspace(0, L, Nx+1)
    plt.plot(x, celsius(Ti))
    _plot_zones_T(Tmin-.2, Tmax+1.2, X)
    plt.title('Températures dans l\'état initial')
    plt.xlabel('x (en m)')
    plt.ylabel('T (en °C)')
    plt.legend()
    plt.show()

def plot_final(T, X, Nx):
    Tf = T[:, -1]
    Tmin, Tmax = min(Tf), max(Tf)
    x = np.linspace(0, L, Nx+1)
    plt.plot(x, celsius(Tf))
    _plot_zones_T(Tmin, Tmax, X)
    plt.title('Températures dans l\'état final')
    plt.xlabel('x (en m)')
    plt.ylabel('T (en °C)')
    plt.legend()
    plt.show()

def _plot_zones_D(Dmin, Dmax, X):
    for i in range(len(X)):
        plt.vlines(x=[X[i]-lp/2, X[i]+lp/2], ymin=Dmin,
            ymax=Dmax, colors=_couleurs[i], ls='--', lw=1) # source
        plt.vlines(x=[X[i]-l/2, X[i]+l/2], ymin=Dmin,
            ymax=Dmax, colors=_couleurs[i], ls='-', lw=.6, label=f'Ordinateur {i+1}')

def _plot_zones_T(Tmin, Tmax, X):
    for i in range(len(X)):
        plt.vlines(x=[X[i]-lp/2, X[i]+lp/2], ymin=celsius(Tmin),
            ymax=celsius(Tmax), colors=_couleurs[i], ls='--', lw=1) # source
        plt.vlines(x=[X[i]-l/2, X[i]+l/2], ymin=celsius(Tmin),
            ymax=celsius(Tmax), colors=_couleurs[i], ls='-', lw=2, label=f'Ordinateur {i+1}')
