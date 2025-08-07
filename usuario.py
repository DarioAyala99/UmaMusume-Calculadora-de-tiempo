class UsuarioEnergia:
    def __init__(self,actual):
        self.actual=actual
        
    def energia_faltante(self):
        ENERGIA_MAXIMA=100
        return (ENERGIA_MAXIMA-self.actual)