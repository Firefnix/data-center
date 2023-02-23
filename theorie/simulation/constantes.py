# Constantes thermodynamiques

def kelvin(T): # °C -> K
    return T + 273.15

def celsius(T): # K -> °C
    return T - 273.15

T0 = kelvin(25) # °C

# Masses volumiques
rho = 2_330 # kg.m^-3 | wikipedia:silicium à 25°C
print(f'ρ = {rho} kg.m^-3')
def rho_a(T): # K -> kg.m^-3
    return 346.384 / T
rho_a0 = rho_a(T0)

# Capacités thermiques massiques
c_a = 1_004 # J.kg^-1.K^-1
c = 700 # J.kg^-1.K^-1 | wikipedia:silicium
# print(f'c = {c} J.kg^-1.K^-1')

# Conductivités thermiques (notées G et pas lambda)
def Ga(T): # K -> W.m^-1.K^-1 | à 1 bar
    vA = celsius(T)
    l = -0.000044075614398888*vA*vA+0.0766069577308689*vA+24.3560822452597
    return l / 1000
Ga0 = Ga(T0)
G = 148 # W.m^-1.K^-1 | wikipedia:silicium

# Diffusivités thermiques
def Da(T): # K -> m^2/s
    return Ga(T) / (rho_a(T) * c_a)
Da0 = Da(T0)
D = G / (rho * c)
print(f'D = {D:.2e} m^2/s')

"""
for ti in range(Nt):
    for xi in range(1, Nx):
        T[xi, ti+1] = (T[xi, ti] + (Te / (Xe**2)) * Dx(xi) *
            (T[xi+1, ti] - T[xi, ti] + T[xi-1, ti])
            + P_c(xi) * Te)
"""
