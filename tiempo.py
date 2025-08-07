import usuario

class Tiempo:
    def __init__(self,energia):
        self.usuario = usuario.UsuarioEnergia(energia)
    
    def calcular_tiempo(self):
        REGENERACION=10
        HORA_MINUTOS=60
        stamina=self.usuario.energia_faltante()
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
        texto = (
        f"Se recupera en {horas} horas y {minutos} minutos.\n"
        f"La energia se va a llenar a las {hora_final.strftime('%H:%M')} hs."
        )
        return texto
