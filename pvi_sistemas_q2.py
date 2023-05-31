import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class pvi_sistemas():
    def __init__(self, ponto_inicial, passo, intervalo, equacao1, equacao2):
        self.x0, self.y10, self.y20 = ponto_inicial
        self.h = passo
        self.xn = intervalo[1] # xn é o último ponto do domínio
        self.f1 = equacao1
        self.f2 = equacao2
        self.pontos = []

        if self.x0 != intervalo[0]:
            print("Verifique o ponto inicial e o intervalo de integração.")
    
    def __str__(self):
        string = f"ponto inicial: ({self.x0}, {self.y10}, {self.y20})\n"
        string += f"passo: {self.h}\n"
        string += f"intervalo: ({self.x0}, {self.xn})\n"
        string += f"f1: {self.equacao1}\n"
        string += f"f2: {self.equacao2}"
        return string
    
    def __repr__(self):
        return self.__str__()
    
    # Resolve o PVI com o método de Euler
    # Retorna uma lista de pontos
    # Sobrescreve a lista de pontos do objeto
    def euler(self):
        x = self.x0
        y1 = self.y10
        y2 = self.y20
        h = self.h
        xn = self.xn
        f1 = self.f1
        f2 = self.f2

        pontos = [(x, y1, y2)]
        
        while x < xn:
            y1 = y1 + h*eval(f1)
            y2 = y2 + h*eval(f2)
            x = x + h
            x, y1, y2 = (round(x, 5), round(y1, 5), round(y2, 5))
            pontos.append((x,y1,y2))
        
        self.pontos = pontos
        return pontos
    
    # Resolve o PVI com o método de Runge Kutta de 4ª ordem
    # Retorna uma lista de pontos
    def rg4(self):
        x = self.x0
        y1 = self.y10
        y2 = self.y20
        h = self.h
        xn = self.xn
        f1 = self.f1
        f2 = self.f2

        pontos = [(x, y1, y2)]

        while x < xn:
            x_anterior, y1_anterior, y2_anterior = (x,y1,y2)

            k11 = eval(f1)
            k12 = eval(f2)

            x = x_anterior + h/2
            y1 = y1_anterior + (h/2)*k11
            y2 = y2_anterior + (h/2)*k12

            k21 = eval(f1)
            k22 = eval(f2)

            y1 = y1_anterior + (h/2)*k21
            y2 = y2_anterior + (h/2)*k22

            k31 = eval(f1)
            k32 = eval(f2)

            x = x_anterior + h
            y1 = y1_anterior + h*k31
            y2 = y2_anterior + h*k32

            k41 = eval(f1)
            k42 = eval(f2)

            y1 = y1_anterior + (h/6)*(k11 + 2*(k21 + k31) + k41)
            y2 = y2_anterior + (h/6)*(k12 + 2*(k22 + k32) + k42)

            x = round(x, 5)
            y1 = round(y1, 5)
            y2 = round(y2, 5)

            pontos.append((x,y1,y2))

        self.pontos = pontos
        return pontos
    
    def plottar(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for x, y1, y2 in self.pontos:
            ax.scatter(x, y1, y2, c='b')

        ax.set_xlabel('x')
        ax.set_ylabel('y1')
        ax.set_zlabel('y2')

        plt.show()