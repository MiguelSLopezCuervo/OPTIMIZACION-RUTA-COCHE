# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:05:46 2023

@author: Miguel Sánchez

FUNCIONES DEL PROGRAMA DEL COCHE
"""

import numpy as np
import matplotlib.pyplot as plt

# OJO, ESTA CARRETERA SE VUELVE PERIÓDICA EN 2PI, PROBAR TAMBIÉN CON OTRAS
def Carr_Sup(x):
    y_s = 1.5 * np.sin(3*np.sin(x)) + 0.5
    return y_s   
def Carr_Inf(x):
    y_i = 1.5 * np.sin(3*np.sin(x)) - 0.5
    return y_i
    
def Avanzar_Coche(Pos, Rad, Ang):
    Nueva_Pos_X = Pos[0] + Rad*np.cos(Ang)
    Nueva_Pos_Y = Pos[1] + Rad*np.sin(Ang)
    return Nueva_Pos_X, Nueva_Pos_Y
    
# Veo si sigo dentro, y también si salgo por abajo calculo la diferencia
def In_Carretera(Pos):
    if Pos[1] <= Carr_Sup(Pos[0]):
        if Pos[1] >= Carr_Inf(Pos[0]):
            Dentro = True
            Diferencia = 0
        else:
            Dentro = False
            Diferencia = Carr_Inf(Pos[0]) - Pos[1]
    else:
        Dentro = False
        Diferencia = Pos[1] - Carr_Sup(Pos[0])

    return Dentro, Diferencia

SobreValoracion_Pos = 100
SobreValoracion_Dif = 50
def Calc_Coste(Pos, Diferencia, i, it_max, Meta):
    # Le doy más importancia a avanzar antes que a llegar más rápido
    Coste = -Pos[0]*SobreValoracion_Pos + i 

    #Siempre voy a preferir un coche que llega lento a uno que se queda cerca muy rápido pero no llega
    if Pos[0] > Meta:
        Coste = Coste - it_max*SobreValoracion_Dif
    # Los que no lleguen a meta deben, además tener un coste más adecuado según cuánto se han salido (si la diferencia es 0 pues no se añadirá nada porque sigue dentro)
    else:
        Coste = Coste + SobreValoracion_Dif*Diferencia
        # Interesa el más una diferencia baja a unas iteraciones menores

    return Coste

# Función para representar el movimiento del coche
def Graficar(Avance_rad, Avance_ang, it_max, Meta):

    posiciones_x = np.zeros(it_max+1)
    posiciones_y = np.zeros(it_max+1)
    for i in range(1, it_max+1):
        posiciones_x[i] = posiciones_x[i-1] + Avance_rad[i-1] * np.cos(Avance_ang[i-1])
        posiciones_y[i] = posiciones_y[i-1] + Avance_rad[i-1] * np.sin(Avance_ang[i-1])

    
    x = np.linspace(-0.0, Meta, 1000)
    y_sup = Carr_Sup(x)
    y_inf = Carr_Inf(x)
    
    # Graficar las funciones Carr_Sup y Carr_Inf
    plt.plot(x, y_sup, label='Carr_Sup')
    plt.plot(x, y_inf, label='Carr_Inf')
    
    # Graficar la trayectoria del coche
    plt.plot(posiciones_x, posiciones_y, marker='o', markersize=3, label='Coche', linestyle='-', linewidth=0.7)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trayectoria del coche en la carretera')
    plt.legend()
    plt.grid(True)
    plt.show()



