import matplotlib.pyplot as plt
import numpy as np

# Classe pvi, recebe:
    # ponto inicial: tupla de floats, representa (x0, y0). ex: (0,0)
    # passo: float
    # intervalo: tupla de floats, representa (x0, xn). ex: (0)
        # x0 no intervalo deve corresponder a x0 do ponto inicial
        # se não corresponderem, será considerado x0 passado no ponto inicial
    # equacao: string, representa a equacao. ex: 'x**2 + y**2', 'np.sin(x)'
        # deve ser usadas as variáveis x e y na notação
class pvi:
    def __init__(self, ponto_inicial, passo, intervalo, equacao):
        self.x0, self.y0 = ponto_inicial
        self.h = passo
        self.xn = intervalo[1] # xn é o último ponto do domínio
        self.equacao = equacao
        self.pontos = []

        if self.x0 != intervalo[0]:
            print("Verifique o ponto inicial e o intervalo de integração.")

    def __str__(self):
        string = f"ponto inicial: ({self.x0}, {self.y0})\n"
        string += f"passo: {self.h}\n"
        string += f"intervalo: ({self.x0}, {self.xn})\n"
        string += f"equacao: {self.equacao}"
        return string
    
    def __repr__(self):
        return self.__str__()
    
    # Resolve o PVI com o método de Euler
    # Retorna uma lista de pontos
    # Sobrescreve a lista de pontos do objeto
    def euler(self):
        x = self.x0
        y = self.y0
        h = self.h
        xn = self.xn
        equacao = self.equacao
        pontos = [(self.x0, self.y0)]

        while x < xn:
            y = y + h*eval(equacao)
            x = x + h
            x, y = (round(x, 5), round(y, 5))
            pontos.append((x,y))
        
        self.pontos = pontos
        return pontos
    
    # Resolve o PVI com o método de Runge Kutta de 4ª ordem
    # Retorna uma lista de pontos
    # Sobrescreve a lista de pontos do objeto
    def rg4(self):
        x = self.x0
        y = self.y0
        h = self.h
        xn = self.xn
        
        equacao = self.equacao
        pontos = [(self.x0, self.y0)]
        
        while x < xn:
            x_anterior, y_anterior = (x,y)
            
            k1 = eval(equacao)
            
            x = x_anterior + h/2
            y = y_anterior + (h/2)*k1
            
            k2 = eval(equacao)
            
            y = y_anterior + (h/2)*k2
            
            k3 = eval(equacao)
            
            x = x_anterior + h
            y = y_anterior + h*k3
            
            k4 = eval(equacao)
            
            x = x_anterior + h
            y = y_anterior + (h/6)*(k1 + 2*(k2+k3) + k4)
            
            x = round(x, 5)
            y = round(y, 5)

            pontos.append((x, y))
        
        self.pontos = pontos
        return pontos
    
    # gera o gráfico com os pontos encontrados
    def plottar(self):
        x_ex = [ponto[0] for ponto in self.pontos]
        y_ex = [ponto[1] for ponto in self.pontos]

        plt.plot(x_ex, y_ex, 'o-')
        plt.show()