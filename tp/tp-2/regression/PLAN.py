import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

T=[39.368,39.28,37.411,42.197,40.976,38.808,39.195,42.295,45.17,39.094,38.643,48.01,54.096,60.3,63.255,62.708,62.6,62.703,64.599,27.913,26.368,28.673,28.371,22.748,20.446,20.653,34.264,35.031,34.881,36.139,42.694,43.579,43.579,49.612,47.726,48.471,51.652,38.403,39.631,44.198,47.543,45.532,51.669,48.693,49.705,55.378,56.199,57.304,56.608,55.104,55.677,59.916,63.647,57.344,65.684]
K=[2500,1500,500,2500,1500,500,1000,2000,3000,0,1500,1500,2000,3000,3000,2000,2000,1000,1500,0,0,1000,500,1000,1000,0,1500,1500,1500,2500,1500,1000,2000,3000,0,0,1000,1000,0,2000,3000,2000,3000,0,0,1000,1000,1000,2000,2000,3000,0,0,1000,2000]
I=[0.348,0.311,0.287,0.357,0.309,0.287,0.303,0.341,0.38,0.268,0.261,0.317,0.334,0.38,0.38,0.337,0.339,0.301,0.327,0.14,0.149,1.738,0.177,0.176,1.943,0.146,0.211,0.211,0.201,0.245,0.208,0.186,0.186,0.264,0.151,0.154,0.188,0.193,0.136,0.213,0.248,0.227,0.256,0.143,0.145,0.177,0.178,0.188,0.216,0.216,0.244,0.157,0.173,1.701,0.218]

def Trouvermax(l):
    return max((l[i],i) for i in range (len(l)))

def Supp(x):
    for _ in range(x):
        _,i = Trouvermax(I)
        I.pop(i)
        T.pop(i)
        K.pop(i)

def plot_plan(x, y, coefficients):
    print('Affichage du plan a*x + b*y + c')
    a, b, c = coefficients[0], coefficients[1], coefficients[2]
    print(f'Avec a = {a}, b = {b} et c = {b}')
    grilleX, grilleY = np.meshgrid(x, y)
    ax.plot_surface(grilleX, grilleY, a*grilleX + b*grilleY + c)

Supp(3) # on supprime 3 valeurs aberrantes
i1 = 19
i2 = 18 + 19

U = 5 # V
r = 500 # unité de conversion des calculs
T1, T2, T3 = np.array(T[:i1]), np.array(T[i1:i2]), np.array(T[i2:])
K1, K2, K3 = r*np.array(K[:i1]), r*np.array(K[i1:i2]), r*np.array(K[i2:])
I1, I2, I3 = np.array(I[:i1]), np.array(I[i1:i2]), np.array(I[i2:])
P1, P2, P3 = U*I1, U*I2, U*I3

# x = K, y = T et z = I
ax = plt.axes(projection='3d')

X_data = np.array([K2, T2]).reshape((-1, 2))
reg = linear_model.LinearRegression().fit(X_data, P2)
a, b, c = reg.coef_[0], reg.coef_[1], reg.intercept_
plot_plan(K2, T2, (a, b, c))

ax.scatter3D(K1, T1, P2, color='red', label='séance 2')

ax.set_xlabel('Calculs (par seconde)', fontweight ='bold')
ax.set_ylabel('Température (°C)', fontweight ='bold')
ax.set_zlabel('Puissance (W)', fontweight ='bold')
ax.legend()

plt.show()
