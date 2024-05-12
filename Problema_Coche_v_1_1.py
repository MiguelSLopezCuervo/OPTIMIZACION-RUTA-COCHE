# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:07:09 2023

@author: Miguel Sánchez

PROGRAMA COCHE A OPTIMIZAR

VERSIÓN 1.1:

"""

import numpy as np
import Funciones_Coche as F_C

def Coste_Coche(it_max, Var_Rad, Var_Ang, Meta):
    Pos_Coche = np.array([0, 0])
    Llega = False
    for i in range(0, it_max):
        # 1º Mover el coche
        Pos_Coche = F_C.Avanzar_Coche(Pos_Coche, Var_Rad[i], Var_Ang[i])
        
        # 2º Comprobar que sigue en la carretera
        En_Carretera, Diferencia = F_C.In_Carretera(Pos_Coche)
        
        # 2.1 Si ya no está en la carretera o hemos llegado asignamos el coste y terminamos
        if En_Carretera == False:
            Coste = F_C.Calc_Coste(Pos_Coche, Diferencia, i, it_max, Meta)
            return Coste, En_Carretera, Llega
        
        if Pos_Coche[0]>=Meta:
            Coste = F_C.Calc_Coste(Pos_Coche, Diferencia, i, it_max, Meta)
            Llega = True
            return Coste, En_Carretera, Llega
            # 2.2 Si sigue en la carretera y no ha llegado a la meta continuamos avanzando etc
    
    # 3º Si acaba el bucle y no nos hemos salido de la carretera, calculamos el coste y acabamos
    Coste = F_C.Calc_Coste(Pos_Coche, Diferencia, i, it_max, Meta)
    return Coste, En_Carretera, Llega











