# -*- coding: utf-8 -*-
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

import scipy.signal as scs


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

# Condição 1
# Cad, Rad, Cvd, Rvd = 3, 50, 0.7, 0.11
# Cae, Rae, Cve, Rve = 2, 50, 0.3, 0.42
# Ccp, Lcp, Rcp = 20, 0.0001, 0.1
# Ccs, Lcs, Rcs = 120, 0.0001, 0.2

# Condição 2
# Cad, Rad, Cvd, Rvd = 3, 0.01, 15, 100
# Cae, Rae, Cve, Rve = 2, 0.02, 10, 100
# Ccp, Lcp, Rcp = 20, 0.0001, 0.1
# Ccs, Lcs, Rcs = 120, 0.0001, 0.2

#Condição 3
Cad, Rad, Cvd, Rvd = 3, 100, 15, 100
Cae, Rae, Cve, Rve = 2, 100, 10, 100
Ccp, Lcp, Rcp = 20, 0.0001, 0.1
Ccs, Lcs, Rcs = 120, 0.0001, 0.2

A=np.array([
	[-1/(Cad*Rad),1/(Rad*Cvd),0,0,0,0,-1],
	[1/(Cad*Rad),-1/(Rvd*Cvd)-1/(Rad*Cvd),0,0,1/(Rvd*Ccp),0,0],
	[0,0,-1/(Cae*Rae),1/(Rae*Cve),0,-1,0],
	[-1/(Ccs*Rve),-1/(Ccs*Rve),-1/(Ccs*Rve)+1/(Cae*Rae),-1/(Ccs*Rve)-1/(Rve*Cve)-1/(Rae*Cve),-1/(Ccs*Rve),0,0],
	[0,1/(Rvd*Cvd),0,0,-1/(Rvd*Ccp),1,0],
	[0,0,1/(Cae*Lcp),0,-1/(Ccp*Lcp),-Rcp/Lcp,0],
	[1/(Cad*Lcs)+1/(Ccs*Lcs),1/(Ccs*Lcs),1/(Ccs*Lcs),1/(Ccs*Lcs),1/(Ccs*Lcs),0,-Rcs/Lcs]])

B=np.array([
    [-1/Rad,0,0,0,0],
    [1/Rad,-1/Rvd,0,0,0],
    [0,0,-1/Rae,0,0],
    [0,0,1/Rae,-1/Rve,-1/(Ccs*Rve)],
    [0,1/Rvd,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,1/(Ccs*Lcs)]
    ])

C=np.array([
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0],
    [-1,-1,-1,-1,-1,0,0]])

D=np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,1]])

sys = clt.ss(A,B,C,D)

##P=(s*eye(7)-A)
##
##E1 = eye(7)
##a1=-Trace(A*E1).simplify()
##E2=A*E1+a1*eye(7)
##a2=-(Trace(A*E2).simplify())/2
##E3=A*E2+a2*eye(7)
##a3=-(Trace(A*E3).simplify())/3
##E4=A*E3+a3*eye(7)
##a4=-(Trace(A*E4).simplify())/4
##E5=A*E4+a4*eye(7)
##a5=-(Trace(A*E5).simplify())/5
##E6=A*E5+a5*eye(7)
##a6=-(Trace(A*E6).simplify())/6
##E7=A*E6+a6*eye(7)
##a7=-(Trace(A*E7).simplify())/7
##      
##Phi_n = E1*s**6+E2*s**5+E3*s**4+E4*s**3+E5*s**2+E6*s+E7
##d = s**7+a1*(s**6)+a2*(s**5)+a3*(s**4)+a4*(s**3)+a5*(s**2)+a6*s+a7
##
##N=C*Phi_n*B+D

G = clt.tf(A, B, C, D)

pp = clt.poles(sys)
