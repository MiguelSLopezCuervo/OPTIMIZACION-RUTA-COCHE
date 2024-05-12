# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 18:35:56 2023

@author: Miguel Sánchez

Algoritmo RCS (Reduce Coste Siempre):
    
    1º Calculamos el coste del coche
    
    2º El coche realiza un mov aleatorio
    
    3º Compara su coste con el coste de la iteración anterior
    
    4º Si es menor el coste, se lo queda, si es mayor, lo desecha
    
"""

import numpy as np
import Problema_Coche_v_1_1 as Coche
import Funciones_Coche as F_C

# DAR VALOR FINAL
Meta = 10

Movimientos_Rad = []
Movimientos_Ang = []

# Empieza con coste 0 ya que empieza en el (0,0)
Coste = 0
Llega = False
while Llega == False:
    
    Avance_Rad = np.random.uniform(0.05, 0.3)
    Avance_Ang = np.random.uniform(-np.pi/2, np.pi/2)
    Movimientos_Rad.append(Avance_Rad)
    Movimientos_Ang.append(Avance_Ang)
    
    it_max = len(Movimientos_Rad)
    Coste_Nuevo, En_Carretera, Llega = Coche.Coste_Coche(it_max, Movimientos_Rad, Movimientos_Ang, Meta)
    
    if Coste_Nuevo > Coste or (En_Carretera is False):
        Movimientos_Rad.pop()
        Movimientos_Ang.pop()
    
    if Llega == True:
        break
    
    Coste = Coste_Nuevo
    
F_C.Graficar(Movimientos_Rad, Movimientos_Ang, it_max, Meta)

    
    
    
    
    
    
    
    
