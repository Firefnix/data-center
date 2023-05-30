# Constantes thermodynamiques
def kelvin(T): # °C -> K
    return T + 273.15

def celsius(T): # K -> °C
    return T - 273.15

T0 = kelvin(25) # °C

# Caractéristiques de l'ordinateur
S = 85.60e-3 * 53.98e-3 # surface, 85,60 mm × 53,98 mm, en m^2
L, l, lp = 1, 10e-2, 3e-2 # m
V = S * l
m = 90.9e-3 # kg, masse totale de l'ordinateur
rho = 1.16e3 # kg/m^3, m / V

# Masses volumiques
rho_si = 2_330 # kg.m^-3 | wikipedia:silicium à 25°C
def rho_a(T): # K -> kg.m^-3
    return 346.384 / T
rho_a0 = rho_a(T0)

# Capacités thermiques massiques
c_a = 1_004 # J.kg^-1.K^-1
c_si = 700 # J.kg^-1.K^-1 | wikipedia:silicium
c = 4.5e3 # J.K^-1.kg^-1 | expérimental

# Conductivités thermiques (notées G et pas lambda)
def Ga(T): # K -> W.m^-1.K^-1 | à 1 bar
    vA = celsius(T)
    l = -0.000044075614398888*vA*vA+0.0766069577308689*vA+24.3560822452597
    return l / 1000
Ga0 = Ga(T0)
G_si = 148 # W.m^-1.K^-1 | wikipedia:silicium

# Diffusivités thermiques
def Da(T): # K -> m^2/s
    return Ga(T) / (rho_a(T) * c_a)
Da0 = Da(T0)
D_si = G_si / (rho_si * c_si)
D = 8.25e-8 # expérimental, 8.25e-8 M^2/s
G = D * rho * c

def P_ordinateur(K, T) -> float:
    a = 0.001756489136630004
    b = 0.36499732057780465e-6
    c = 0.9409716753510062
    return a*T + b*K + c

if __name__ == '__main__':
    print(f'T0 = {T0} K = {celsius(T0)} °C')
    print(f'ρ = {rho:.2f} kg.m^-3')
    print(f'ρ_a = {rho_a0:.2f} kg.m^-3 [à T0]')
    print(f'λ = {G:.2e} W.m^-1.K^-1')
    print(f'λ_a = {Ga0:.2e} W.m^-1.K^-1 [à T0]')
    print(f'D = {D:.2e} m^2/s')
    print(f'D_a = {Da0:.2e} m^2/s [à T0]')
