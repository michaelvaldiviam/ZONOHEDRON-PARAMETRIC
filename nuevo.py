#import pandas as pd
from math import pi
import math
#import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#%matplotlib notebook

#from matplotlib import cm

print("Software para cálculo de un zonohedro")
print("Ingrese las variables acontinuación: ")

N = 15 # numero de orden
Dk = 8 #diametro del piso hasta nivel K ingresado
K = 8 # nivel hasta el piso
a = 46.2 #angulo de forma

#Calculos esenciales directos
De = Dk / (2 * math.sin((K * pi) / N))  # diámetro esencial para calcular R1
Re = De / 2  # Radio del diámetro esencial
b = 360 / N
k = 1
f = open ('puntosxyz.txt','w') #abrimos archivo txt para borrar contenido
f.close()
def largo_arista(h1):
    L_arista = h1 / math.cos((pi / 180) * a)  #largo de la arista
    return L_arista

def altura_zome_hastaK(h1,K): #Altura hasta nivel K
    altura = h1 * K
    return altura

def radio_nivel1(Re,b):
    Rpol1 = Re * math.sqrt(2 * (1 - math.cos(b * (pi / 180)))) #Radio nivel 1
    return Rpol1

def altura_zome_polo_a_polo(h1,K): #Altura total polo a polo
    altura_total = h1 * K
    return altura_total

def altura_un_nivel(Rpol1,a):
    h1 = Rpol1 / math.tan(a * (pi / 180))  #altura de un nivel
    return h1


def puntoX_pol3D(Rpol1,b,j):
    X = Rpol1 * math.cos((pi / 180) * b * j)
    return X

def puntoY_pol3D(Rpol1,b,j):
    Y = Rpol1 * math.sin((pi / 180) * b * j)
    return Y

def puntoZ_pol3D(h1,k):
    Z = - h1 * k
    return Z

def lista_puntos_nivel1():
    k = 1
    puntos_nivel1 = []
    j = 0
    for i in range(N):
        X = puntoX_pol3D(radio_nivel1(Re,b),b,j)
        Y = puntoY_pol3D(radio_nivel1(Re,b),b,j)
        Z = puntoZ_pol3D(altura_un_nivel(radio_nivel1(Re,b),a),k)
        j = j + 1
        puntos_nivel1.append((X,Y,Z))
    return puntos_nivel1

def radios_por_nivel(): #Calcula una lista de radios hasta nivel K (número de niveles hasta el piso)
    k = 1 #contador
    lista_de_radios = []
    for n in range(K-1):
        Re_aux = 2 * Re * math.sin(((k + 1) * pi) / N)
        lista_de_radios.append(Re_aux) #Acumula los radios desde el nivel K = 2
        k = k + 1
    lista_de_radios.insert(0,radio_nivel1(Re,b)) #Agrega radio nivel 1 a la lista anterior
    return lista_de_radios #Entrega una lista de radios desde el nivel 1

def puntos_nivel_par(k):
    #k = 2 #partimos del nivel 2
    lista_de_puntos_nivel_par = []
    j = 1/2
    Re_aux = 2 * Re * math.sin(((k) * pi) / N)
    for i in range(N):
        Xp = Re_aux * math.cos((pi / 180) * b * j)
        Yp = Re_aux * math.sin((pi / 180) * b * j)
        Zp = puntoZ_pol3D(altura_un_nivel(radio_nivel1(Re,b),a),k)
        j = j + 1
        lista_de_puntos_nivel_par.append((Xp,Yp,Zp))
    return lista_de_puntos_nivel_par

def puntos_nivel_impar(k):
    lista_de_puntos_nivel_impar = []
    Re_aux = 2 * Re * math.sin(((k + 1) * pi) / N)
    j = 0
    for i in range(N):
        Xi = Re_aux * math.cos((pi / 180) * b * j)
        Yi = Re_aux * math.sin((pi / 180) * b * j)
        Zi = puntoZ_pol3D(altura_un_nivel(radio_nivel1(Re,b),a),k)
        j = j + 1
        lista_de_puntos_nivel_impar.append((Xi,Yi,Zi))
    return lista_de_puntos_nivel_impar


class puntos():

    def nive1(self,k):
        for i in lista_puntos_nivel1():
            f = open("puntosxyz.txt", "a+")
            puntoXYZ = i
            X = puntoXYZ[0]
            Y = puntoXYZ[1]
            Z = puntoXYZ[2]

            f.write(str(X))
            f.write(' '+str(Y))
            f.write(' '+str(Z))
            f.write('\n')
            f.close()
            #np.savetxt('puntosxyz.txt', np.column_stack([X, Y, Z]))
            #ax.scatter3D(X, Y, Z)
            plt.plot(X, Y, Z, 'bo')
            self.p = (X,Y,Z)
        return self.p

    def nivelPAR(self,k,k2):
        for t in puntos_nivel_par(k):
            f = open("puntosxyz.txt", "a+")
            puntoXYZpar = t
            Xpar = puntoXYZpar[0]
            Ypar = puntoXYZpar[1]
            Zpar = puntoXYZpar[2]

            f.write(str(Xpar))
            f.write(' '+str(Ypar))
            f.write(' '+str(Zpar))
            f.write('\n')
            f.close()
            plt.plot(Xpar, Ypar, Zpar, 'ro')
            # ax1.scatter3D(Xpar, Ypar, Zpar)
            self.p2 = (Xpar, Ypar, Zpar)
            '''
            f = open("puntosxyz.txt", "a+")
            for i in self.p2:
                f.write(str(i))
            f.close()
            '''
            k = k + 1
        return self.p2

    def nivelIMPAR(self,k):
        for s in puntos_nivel_impar(k):
            f = open("puntosxyz.txt", "a+")
            puntoXYZimpar = s
            Ximpar = puntoXYZimpar[0]
            Yimpar = puntoXYZimpar[1]
            Zimpar = puntoXYZimpar[2]

            f.write(str(Ximpar))
            f.write(' '+str(Yimpar))
            f.write(' '+str(Zimpar))
            f.write('\n')
            f.close()
            # plt.plot(Ximpar, Yimpar, Zimpar, color="red", markersize=1)
            plt.plot(Ximpar, Yimpar, Zimpar, 'bo')
            # ax1.scatter3D(Ximpar, Yimpar, Zimpar)
            self.p3 = (Ximpar, Yimpar, Zimpar)

            '''
            f = open("puntosxyz.txt", "a+")
            for i in self.p3:
                f.write(str(i))
            f.close()
            '''
            k = k + 1
        return self.p3

#CUERPO DEL PROGRAMA


print("Los radios por nivel son: "+str(radios_por_nivel()))
print('La altura Zome hasta nivel K es : '+str(altura_zome_hastaK(altura_un_nivel(radio_nivel1(Re,b),a),K)))
print('La altura de un nivel es: '+str(altura_un_nivel(radio_nivel1(Re,b),a)))
print(' ')

# Creamos la figura
fig = plt.figure()
# Agregamos un plano 3D
ax = fig.gca(projection='3d')
#ax = fig.add_subplot(111, projection='3d')
#ax1 = fig.add_subplot(111,projection='3d')

plt.title('Gráfico de puntos 3D de los vértices de un Zome de orden '+str(N))



mispuntos = puntos()
punto_inicial = [0,0,0]
#plt.plot(0,0,- altura_zome_hastaK(altura_un_nivel(radio_nivel1(Re,b),a),K),'go')

print(punto_inicial)
if k == 1:
    print(mispuntos.nive1(k=1))
    k = k + 1
k2 = 2
while k2 <= K:

    if k % 2 == 0:
        print(mispuntos.nivelPAR(k,k2))
        k = k +1

    elif k % 2 != 0:
        print(mispuntos.nivelIMPAR(k))
        k = k + 1
    k2 = k2 + 1

punto_final = [0,0,altura_zome_hastaK(altura_un_nivel(radio_nivel1(Re,b),a),K)]
print(punto_final)

print(largo_arista(altura_un_nivel(radio_nivel1(Re,b),a)))


'''
for i in lista_puntos_nivel1():
    puntoXYZ = i
    X = puntoXYZ[0]
    Y = puntoXYZ[1]
    Z = puntoXYZ[2]
    np.savetxt('puntosxyz.txt', np.column_stack([X,Y,Z]))
    plt.plot(X, Y, Z, 'bo')
k2 = 2
k = 2
while k2 <= K+1:
    #k = k + 1
    if k % 2 == 0:
        for t in puntos_nivel_par(k):
            puntoXYZpar = t
            Xpar = puntoXYZpar[0]
            Ypar = puntoXYZpar[1]
            Zpar = puntoXYZpar[2]
            plt.plot(Xpar, Ypar, Zpar, 'ro')
            #ax1.scatter3D(Xpar, Ypar, Zpar)
        k = k + 1

    elif k % 2 != 0:
        for s in puntos_nivel_impar(k):
            puntoXYZimpar = s
            Ximpar = puntoXYZimpar[0]
            Yimpar = puntoXYZimpar[1]
            Zimpar = puntoXYZimpar[2]
            #plt.plot(Ximpar, Yimpar, Zimpar, color="red", markersize=1)
            plt.plot(Ximpar, Yimpar, Zimpar, 'bo')
            #ax1.scatter3D(Ximpar, Yimpar, Zimpar)
        k = k + 1
    k2 = k2 + 1
'''

#print(puntos_nivel_par(k))


#plt.ylabel('Eje Y')
#plt.xlabel('Eje X')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.plot(0, 0, 0, 'ro')
f.close()
#plt.interactive(True)
plt.show()




