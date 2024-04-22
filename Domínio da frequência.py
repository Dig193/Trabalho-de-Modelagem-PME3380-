"""
Spyder Editor
This is a temporary script file.
"""

import control as clt
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import *
init_printing()


# Cad=symbols('Cad')
# Rad=symbols('Rad')
# Cvd=symbols('Cvd')
# Rvd=symbols('Rvd')
# Ccp=symbols('Ccp')
# Rcp=symbols('Rcp')
# Lcp=symbols('Lcp')
# Cae=symbols('Cae')
# Rae=symbols('Rae')
# Cve=symbols('Cve')
# Rve=symbols('Rve')
# Ccs=symbols('Ccs')
# Rcs=symbols('Rcs')
# Lcs=symbols('Lcs')
s=symbols('s')

Ccp, Lcp, Rcp = 20, 0.0001, 0.1
Ccs, Lcs, Rcs = 120, 0.0001, 0.2
Cad, Cae = 3, 2

def Condição (R_ad, C_vd, R_vd, R_ae, C_ve, R_ve):
    Rad, Cvd, Rvd = R_ad, C_vd, R_vd
    Rae, Cve, Rve = R_ae, C_ve, R_ve
    
    return Rad, Cvd, Rvd, Rae, Cve, Rve
    
# Condição 1
# Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(100, 0.7, 0.11, 100, 0.3, 0.42)

# Condição 2
# Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(0.01, 15, 100, 0.02, 10, 100)


# Condição 3
# Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(100, 15, 100, 100, 10, 100)

def A_cond (Rad, Cvd, Rvd, Rae, Cve, Rve):
    A=np.array([
	[-1/(Cad*Rad),1/(Rad*Cvd),0,0,0,0,-1],
	[1/(Cad*Rad),-1/(Rvd*Cvd)-1/(Rad*Cvd),0,0,1/(Rvd*Ccp),0,0],
	[0,0,-1/(Cae*Rae),1/(Rae*Cve),0,-1,0],
	[-1/(Ccs*Rve),-1/(Ccs*Rve),-1/(Ccs*Rve)+1/(Cae*Rae),-1/(Ccs*Rve)-1/(Rve*Cve)-1/(Rae*Cve),-1/(Ccs*Rve),0,0],
	[0,1/(Rvd*Cvd),0,0,-1/(Rvd*Ccp),1,0],
	[0,0,1/(Cae*Lcp),0,-1/(Ccp*Lcp),-Rcp/Lcp,0],
	[1/(Cad*Lcs)+1/(Ccs*Lcs),1/(Ccs*Lcs),1/(Ccs*Lcs),1/(Ccs*Lcs),1/(Ccs*Lcs),0,-Rcs/Lcs]])
    return A

# def B_cond (Rad, Cvd, Rvd, Rae, Cve, Rve):
#     B=np.array([
#     [-1/Rad,0,0,0,0],
#     [1/Rad,-1/Rvd,0,0,0],
#     [0,0,-1/Rae,0,0],
#     [0,0,1/Rae,-1/Rve,-1/(Ccs*Rve)],
#     [0,1/Rvd,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,1/(Ccs*Lcs)]
#     ])
#     return B

def B_cond (Rad, Cvd, Rvd, Rae, Cve, Rve):
    B=np.array([
    [-1/Rad,0,0,0],
    [1/Rad,-1/Rvd,0,0],
    [0,0,-1/Rae,0],
    [0,0,1/Rae,-1/Rve],
    [0,1/Rvd,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ])
    return B


C=np.array([
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0],
    [-1,-1,-1,-1,-1,0,0]])

D=np.array([
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]])

# Condição 1
Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(100, 0.7, 0.11, 100, 0.3, 0.42)
A1 = A_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)
B1 = B_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)    
sys = clt.ss(A1,B1,C,D)
G1 = clt.tf(sys)
pp1 = clt.poles(sys)

# Condição 2
Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(0.01, 15, 100, 0.02, 10, 100)
A2 = A_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)
B2 = B_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)    
sys = clt.ss(A2,B2,C,D)
G2 = clt.tf(sys)
pp2 = clt.poles(sys)

# Condição 3
Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(100, 15, 100, 100, 10, 100)
A3 = A_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)
B3 = B_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)    
sys = clt.ss(A3,B3,C,D)
G3 = clt.tf(sys)
pp3 = clt.poles(sys)

# Condição 4
Rad, Cvd, Rvd, Rae, Cve, Rve = Condição(100, 15, 0.11, 100, 10, 0.42)
A4 = A_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)
B4 = B_cond (Rad, Cvd, Rvd, Rae, Cve, Rve)    
sys = clt.ss(A4,B4,C,D)
G4 = clt.tf(sys)
pp1 = clt.poles(sys)

# plt.figure(dpi=800)

# #Volume de cada um dos átrios afetados pela diferença de pressão em cada uma de suas saídas
# mag,phase,omega = clt.bode_plot(G2[0,0],Hz=True,dB=True,color='lime',label ='Átrio direito')
# mag,phase,omega = clt.bode_plot(G2[2,2],Hz=True,dB=True,color='deepskyblue',label ='Átrio esquerdo')

# plt.legend()
# plt.show()

# plt.figure(dpi=800)

# #Volume de cada um dos ventrículos afetados pela diferença de pressão em cada uma de suas saídas
# mag,phase,omega = clt.bode_plot(G1[1,1],Hz=True,dB=True,color='green',label ='Ventrículo direito (s)')
# mag,phase,omega = clt.bode_plot(G1[3,3],Hz=True,dB=True,color='blue',label ='Ventrículo esquerdo (s)')
# mag,phase,omega = clt.bode_plot(G4[1,1],Hz=True,dB=True,color='greenyellow',label ='Ventrículo direito (d)')
# mag,phase,omega = clt.bode_plot(G4[3,3],Hz=True,dB=True,color='cyan',label ='Ventrículo esquerdo (d)')

# plt.legend()
# plt.show()

# plt.figure(dpi=800)

# #Volume de cada uma das ciruclações afetadas pela diferença de pressão em cada uma de suas entradas (imposta pelos ventrículos)
# mag,phase,omega = clt.bode_plot(G1[4,1],Hz=True,dB=True,color='lightcoral', label ='Circulação pulmonar')
# mag,phase,omega = clt.bode_plot(G1[5,3],Hz=True,dB=True,color='crimson',label ='Circulação sistêmica')

# plt.legend()
# plt.show()

# plt.figure(dpi=800)

# #Volume de cada um dos ventrículos afetados pela diferença de pressão em cada uma de suas entradas (imposta pelos átrios)
# mag,phase,omega = clt.bode_plot(G2[1,0],Hz=True,dB=True,color='green',label ='Ventrículo direito')
# mag,phase,omega = clt.bode_plot(G2[3,2],Hz=True,dB=True,color='blue',label ='Ventrículo esquerdo')

# plt.legend()
# plt.show()

Q1 = clt.ctrb(A1,B1)
Q2 = clt.ctrb(A2,B2)
Q3 = clt.ctrb(A3,B3)
Q4 = clt.ctrb(A4,B4)
