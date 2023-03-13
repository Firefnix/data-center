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

Supp(3)
i1=19
i2=18+19

T1=T[:i1]
T2=T[i1:i2]
T3=T[i2:]

K1=K[:i1]
K2=K[i1:i2]
K3=K[i2:]

I1=I[:i1]
I2=I[i1:i2]
I3=I[i2:]



U = 5 # V
r = 500 # unité de conversion des calculs
zdata = U*np.array(I)
xdata = r*np.array(K)
ydata = np.array(T)

z1data = U*np.array(I1)
x1data = r*np.array(K1)
y1data = np.array(T1)

z2data = U*np.array(I2)
x2data = r*np.array(K2)
y2data = np.array(T2)

z3data = U*np.array(I3)
x3data = r*np.array(K3)
y3data = np.array(T3)


#Solution


"""grilleX, grilleY = np.meshgrid(K2, T2)
A= np.hstack((transfo(T2), transfo(K2), np.ones_like(transfo(T2))))
res= np.linalg.lstsq(A, transfo(I2))
aopt,bopt,copt=res[0]
ax.plot_surface(grilleX, grilleY, plan(grilleX, grilleY, (aopt, bopt, copt)), alpha=0.8)

print (res)"""
# ax.scatter3D(xdata, ydata, zdata, color='black')

ax.scatter3D(x1data, y1data, z1data, color='black', label='séance 3')

ax.scatter3D(x2data, y2data, z2data, color='red', label='séance 2')

ax.scatter3D(x3data, y3data, z3data, color='green', label='séance 1')

ax.set_xlabel('Calculs (par seconde)', fontweight ='bold')
ax.set_ylabel('Température (°C)', fontweight ='bold')
ax.set_zlabel('Puissance (W)', fontweight ='bold')

ax.legend()

plt.show()
