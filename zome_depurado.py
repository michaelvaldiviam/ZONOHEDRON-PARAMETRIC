import pandas as pd
from math import pi
import math
import numpy as np

print("Software para cálculo de un zonohedro")
print("Ingrese las variables acontinuación: ")

'''Estas son las entradas por teclado'''
N = 12 # numero de orden corresponde a los números de pétalos del zome
Dk = 8 #diametro del piso hasta nivel K ingresado
K = 8 # nivel hasta el piso
a = 46.2 #angulo de forma regula lo agudo del zome
'''Fin a las entradas por teclado'''

#Calculos esenciales directos
De = Dk / (2 * math.sin((K * pi) / N))  # diámetro esencial para calcular R1
Re = De / 2  # Radio del diámetro esencial
b = 360 / N
k = 1 #comienzo del contador de niveles desde 1
#f = open ('puntoszome.csv','w') #abrimos archivo txt para borrar contenido
#f.close() #cerramos archivo limpio
#datos = pd.read_csv('puntoszome.csv', header=0, sep='\t')



def radio_nivel1(Re,b):
    return Re * math.sqrt(2 * (1 - math.cos(b * (pi / 180)))) #Radio nivel 1

def altura_zome_hastaK(h1,K): #Altura hasta nivel K
    return h1 * K

def altura_zome_polo_a_polo(h1,N): #Altura total polo a polo
    return h1 * N

def altura_un_nivel(R1,a):
    return R1 / math.tan(a * (pi / 180))  #altura de un nivel

def largo_arista(h1,a):
    return h1 / math.cos((pi / 180) * a)  #largo de la arista

def punto_inicial():
    x = 0
    y = 0
    z = 0
    punto = [x,y,z]
    return punto

'''Construcción puntos del primer nivel'''
class puntos():
#PUNTOS NIVEL 1
    def puntos_X1(self,R1,b,N):
        j = 0
        listax = []
        for n in range(N):
            x = R1 * math.cos((pi / 180) * b * j)
            listax.append(x)
            #print(x)
            j = j + 1
        return listax

    def puntos_Y1(self,R1,b,N):
        j = 0
        listay = []
        for n in range(N):
            y = R1 * math.sin((pi / 180) * b * j)
            listay.append(y)
            j = j + 1
        return listay

    def punto_Z1(self,h1,k):
        listaz = []
        for n in range(N):
            z = - h1 * k #k es la representación de solo un nivel
            listaz.append(z)
        return listaz

#PUNTOS NIVEL PAR
    def puntos_Xpar(self, b, N, k):
        j = 1 / 2
        Re_aux = 2 * Re * math.sin(((k) * pi) / N)
        listax = []
        for n in range(N):
            x = Re_aux * math.cos((pi / 180) * b * j)
            listax.append(x)
            j = j + 1
        return listax

    def puntos_Ypar(self, b, N, k):
        j = 1 / 2
        Re_aux = 2 * Re * math.sin(((k) * pi) / N)
        listay = []
        for n in range(N):
            y = Re_aux * math.sin((pi / 180) * b * j)
            listay.append(y)
            j = j + 1
        return listay

    def punto_Zpar(self, h1, k):
        listaz = []
        for n in range(N):
            z = - h1 * k  # k es la representación de solo un nivel
            listaz.append(z)
        return listaz

#PUNTOS NIVEL IMPAR
    def puntos_Ximpar(self,R1,b,N):
        j = 0
        listax = []
        for n in range(N):
            x = R1 * math.cos((pi / 180) * b * j)
            listax.append(x)
            j = j + 1
        return listax

    def puntos_Yimpar(self,R1,b,N):
        j = 0
        listay = []
        for n in range(N):
            y = R1 * math.sin((pi / 180) * b * j)
            listay.append(y)
            j = j + 1
        return listay

    def punto_Zimpar(self,h1,k):
        listaz = []
        for n in range(N):
            z = - h1 * k #k es la representación de solo un nivel
            listaz.append(z)
        return listaz

'''Llamadas a los métodos'''
mispuntos = puntos() #objeto mis puntos
radio1 = radio_nivel1(Re,b) #llamada a la función para retornar radio del nivel 1


if k == 1: #inicio para el nivel 1
    datos_x1 = mispuntos.puntos_X1(radio1, b, N)
    dfx = pd.Series(datos_x1)

    datos_y1 = mispuntos.puntos_Y1(radio1, b, N)
    dfy = pd.Series(datos_y1)

    datos_z1 = mispuntos.punto_Z1(altura_un_nivel(radio1, a), k)
    dfz = pd.Series(datos_z1)

    arreglo = (datos_x1,datos_y1,datos_z1)
    dt = pd.DataFrame(arreglo).T
    f = open("puntoszome.csv", "w+")
    f.write(str(dt))
    f.close()
    print(dt)
    k = k + 1
k2 = 2

while k2 <= K: #inicio para el nivel par

    if k % 2 == 0:
        datos_xp = mispuntos.puntos_X1(radio1, b, N)
        dfxp = pd.Series(datos_xp)

        datos_yp = mispuntos.puntos_Ypar(b,N,k)
        dfyp = pd.Series(datos_yp)

        datos_zp = mispuntos.punto_Zpar(altura_un_nivel(radio1,a),k)
        dfzp = pd.Series(datos_zp)

        k = k +1

    elif k % 2 != 0: #inicio para el nivel impar
        datos_xi = mispuntos.puntos_Ximpar(radio1,b,N)
        dfxi = pd.Series(datos_xi)

        datos_yi = mispuntos.puntos_Yimpar(radio1,b,N)
        dfyi = pd.Series(datos_yi)

        datos_zi = mispuntos.punto_Zimpar(altura_un_nivel(radio1,a),k)
        dfzi = pd.Series(datos_zi)

        k = k + 1
    k2 = k2 + 1
