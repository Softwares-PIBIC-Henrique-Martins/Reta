# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:39:44 2020

@author: Samaung
"""
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

dados=pd.read_excel('C:/Users/Samaung/OneDrive - unb.br/Documentos/Henrique/DadosExcel/dadosgráfico.xlsx')

x=dados['x']
y=dados['y']

def reta(x,a,b):
    return a*x+b

parâmetros, erro = curve_fit(reta, x, y)
print("a =", parâmetros[0])
print("b =", parâmetros[1])
print("Matriz de covariância=", erro)
xFit=np.arange(0.1,5.21,0.01)
yFit = reta(xFit, *parâmetros)
plt.plot(x, y, 'o')
plt.plot(xFit, yFit, '-')
plt.show()
