import numpy as np

# Classe pvi_sistemas, recebe:
    # ponto inicial: tupla de floats, representa (x0, y0). ex: (0,0)
    # ponto final: tupla de floats, representa (xf, yf). ex: (1,1)
    # N: número de subintervalos, inteiro
    # p: string, representa a função p(x) que acompanha y''. ex: 'x**2'
    # q: string, representa a função q(x) que acompanha y'. ex: '-x'
    # r: string, representa a função r(x) que acompanha y. ex: '1'
class pvi_2ordem:
    def __init__(self, ponto_inicial, ponto_final, N, p, q, r):
        self.x0, self.y0 = ponto_inicial
        self.xf, self.yf = ponto_final
        self.N = N
        self.p_x = p
        self.q_x = q
        self.r_x = r
        self.delta_x = (self.xf-self.x0)/N
        self.x = np.linspace(self.x0 + self.delta_x, self.xf - self.delta_x, N-1)
        self.A = np.zeros((N-1, N-1))
        self.b = np.zeros(N-1)
        self.y = np.zeros(N-1)
    
    def p(self, a):
        x = a
        return eval(self.p_x)
    
    def q(self, a):
        x = a
        return eval(self.q_x)
    
    def r(self, a):
        x = a
        return eval(self.r_x)
    
    def diferencas_finitas(self):
        # Preenchendo a matriz A
        for i in range(self.N-1):
            x = self.x[i]
            for j in range(self.N-1):

                if i == j: # diagonal principal
                    self.A[i][j] = 2 + self.q(x)*(self.delta_x**2)

                elif i == j+1: # diagonal inferior
                    self.A[i][j] = -1 - self.p(x)*self.delta_x/2
                
                elif i == j-1: # diagonal superior
                    self.A[i][j] = -1 + self.p(x)*self.delta_x/2

                # os elementos fora dessas diagonais permanecem nulos
        
        # Preenchendo o vetor b
        for i in range(self.N-1):
            x = self.x[i]
            if i == 0: # primeira linha
                self.b[i] = (1 + self.p(x)*self.delta_x/2)*self.y0 - self.r(x)*self.delta_x**2
            
            elif i == self.N-2: # ultima linha
                self.b[i] = (1 - self.p(x)*self.delta_x/2)*self.yf - self.r(x)*self.delta_x**2
            
            else: # demais elementos
                self.b[i] = -self.r(x)*self.delta_x**2

        # TROCAR ISSO AQUI PELO THOMAS
        self.y = np.linalg.solve(self.A, self.b)

        return self.y