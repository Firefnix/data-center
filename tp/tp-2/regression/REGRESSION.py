from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
T=[39.368,39.28,37.411,42.197,40.976,38.808,39.195,42.295,45.17,39.094,38.643,48.01,54.096,60.3,63.255,62.708,62.6,62.703,64.599,27.913,26.368,28.673,28.371,22.748,20.446,20.653,34.264,35.031,34.881,36.139,42.694,43.579,43.579,49.612,47.726,48.471,51.652,38.403,39.631,44.198,47.543,45.532,51.669,48.693,49.705,55.378,56.199,57.304,56.608,55.104,55.677,59.916,63.647,57.344,65.684]
K=[2500,1500,500,2500,1500,500,1000,2000,3000,0,1500,1500,2000,3000,3000,2000,2000,1000,1500,0,0,1000,500,1000,1000,0,1500,1500,1500,2500,1500,1000,2000,3000,0,0,1000,1000,0,2000,3000,2000,3000,0,0,1000,1000,1000,2000,2000,3000,0,0,1000,2000]
I=[0.348,0.311,0.287,0.357,0.309,0.287,0.303,0.341,0.38,0.268,0.261,0.317,0.334,0.38,0.38,0.337,0.339,0.301,0.327,0.14,0.149,1.738,0.177,0.176,1.943,0.146,0.211,0.211,0.201,0.245,0.208,0.186,0.186,0.264,0.151,0.154,0.188,0.193,0.136,0.213,0.248,0.227,0.256,0.143,0.145,0.177,0.178,0.188,0.216,0.216,0.244,0.157,0.173,1.701,0.218]
ax = plt.axes(projection='3d')

def transfo (L):
    l=[]
    for i in L:
        l.append([i])
    return l

def Trouvermax(l):
    return max((l[i],i) for i in range (len(l)))

def Supp(x):
    for _ in range(x):
        _,i = Trouvermax(I)
        I.pop(i)
        T.pop(i)
        K.pop(i)

def plan(x, y, A):
    return A[0]*x + A[1]*y + A[2]

Supp(3) # on supprime 3 valeurs aberrantes
i1 = 19
i2 = 18 + 19

U = 5 # V
r = 500e-6 # unité de conversion des calculs
T1, T2, T3 = np.array(T[:i1]), np.array(T[i1:i2]), np.array(T[i2:])
K1, K2, K3 = r*np.array(K[:i1]), r*np.array(K[i1:i2]), r*np.array(K[i2:])
I1, I2, I3 = np.array(I[:i1]), np.array(I[i1:i2]), np.array(I[i2:])
P1, P2, P3 = U*I1, U*I2, U*I3
If= [0.254,0.274,0.292,0.31,0.324,0.35,0.377,0.385,0.275,0.279,0.3,0.318,0.34,0.355,0.375]
Kf= [0,500,1000,1500,2000,2500,3000,3000,0,500,1000,1500,2000,2500,3000]
Tf= [29.7,31.7,33.2,37.5,37.7,38.8,40.78,68.359,62.35,57,56.787,67.3,73.482,67.988,68.296]
I4 = np.array(If)
K4 = r*np.array(Kf)
T4 = np.array(Tf)
P4 = U*I4
T23 = np.array(T[i1:i2] + T[i2:])
K23 = r*np.array(K[i1:i2] + K[i2:])
I23 = np.array(I[i1:i2] + I[i2:])
P23 = U*I23
#plan final
Td = np.array(T[:i1] + Tf)
Kd = r*np.array(K[:i1] + Kf)
Id = np.array(I[:i1] + If)
Pd = U*Id
# Premier plan
A = np.hstack((transfo(T23), transfo(K23), np.ones_like(transfo(T23))))
res = np.linalg.lstsq(A, transfo(P23))
aopt,bopt,copt=res[0]
#Deuxième plan
Ad = np.hstack((transfo(Td), transfo(Kd), np.ones_like(transfo(Td))))
resd = np.linalg.lstsq(Ad, transfo(Pd))
ad,bd,cd=resd[0]

#Affichage 1er plan
Z = aopt * T23 + bopt * K23 + copt
ax.plot_trisurf(K23, T23, Z, linewidth=0.2, alpha=0.3, antialiased=True)
print(f'a: {aopt}, b: {bopt}, c: {copt}')

#affichage 2em plan
Zd = ad * Td + bd * Kd + cd
ax.plot_trisurf(Kd, Td, Zd, linewidth=0.2, alpha=0.3, antialiased=True)
print(f'a: {ad}, b: {bd}, c: {cd}')


# print(res)
# ax.scatter3D(xdata, ydata, zdata, color='black')
ax.scatter3D(K1, T1, P1, color='black', label='séance 3')

ax.scatter3D(K2, T2, P2, color='red', label='séance 2')

ax.scatter3D(K4, T4, P4, color='blue', label='séance 4')

ax.scatter3D(K3, T3, P3, color='green', label='séance 1')



ax.set_xlabel('Calculs (millions par seconde)', fontweight ='bold')
ax.set_ylabel('Température (°C)', fontweight ='bold')
ax.set_zlabel('Puissance (W)', fontweight ='bold')

ax.legend()

plt.show()
