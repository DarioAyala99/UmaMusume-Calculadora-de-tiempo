class UsuarioEnergia:
    def __init__(self,actual):
        self.actual=actual
        
    def energia_faltante(self):
        ENERGIA_MAXIMA=100
        return (ENERGIA_MAXIMA-self.actual)
    
class Tiempo:
    def __init__(self,datos_usuario):
        self.datos = datos_usuario
    
    def calcular_tiempo(self):
        REGENERACION=10
        HORA_MINUTOS=60
        stamina=self.datos.energia_faltante()
        total_minutos=stamina*REGENERACION
        horas=total_minutos/HORA_MINUTOS
        minutos=total_minutos%HORA_MINUTOS
        return int(horas),int(minutos)
    
    def mostrar_tiempo(self):
        from datetime import datetime,timedelta
        horas,minutos=self.calcular_tiempo()
        ahora = datetime.now()
        tiempo_restante = timedelta(hours=horas, minutes=minutos)
        hora_final = ahora + tiempo_restante
        print(f"Se recupera en {horas} horas y {minutos} minutos.") 
        print(f"La energia se va a llenar a las {hora_final.strftime('%H:%M')} hs.")

if __name__ == "__main__":
    try:
        actual=int(input("Ingrese la energia actual: "))
        entrada=UsuarioEnergia(actual)
        resultado=Tiempo(entrada)
        resultado.mostrar_tiempo()
    except ValueError:
         print("Ingresa un numero.")