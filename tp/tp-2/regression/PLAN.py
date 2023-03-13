import numpy as np

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

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



# Data for a three-dimensional line
zdata = np.array(I)
xdata = np.array(K)
ydata = np.array(T)

z1data = np.array(I1)
x1data = np.array(K1)
y1data = np.array(T1)

z2data = np.array(I2)
x2data = np.array(K2)
y2data = np.array(T2)

z3data = np.array(I3)
x3data = np.array(K3)
y3data = np.array(T3)

zbdata = np.array(I[i1:])
xbdata = np.array(K[i1:])
ybdata = np.array(T[i1:])
# Afficher le graphique

fig = plt.figure()

ax = fig.gca(projection='3d')

ax.plot_trisurf(xbdata, ybdata, zbdata, cmap = "viridis")


plt.show()
