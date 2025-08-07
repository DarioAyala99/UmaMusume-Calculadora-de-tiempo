import tkinter as tk
from PIL import Image,ImageTk
import sys
import os
from tiempo import *
     
class VentanaPrincipal():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.resizable(width=False,height=False)
        self.ventana.config(width=350, height=250)
        self.ventana.title("BAKUSHIN CALCULATOR")
        self.crear_fondo()
        self.crear_etiqueta()
        self.crear_caja_texto()
        self.crear_boton()
        self.ventana.mainloop()
    
    def calcular(self):
        try:
            numero_usuario=int(self.caja_energia.get())
            valor_final=numero_usuario
            sta=Tiempo(valor_final)
            resultado=sta.mostrar_tiempo()
            self.resultado.config(text=resultado)
            self.resultado.place(x=75, y=170,)
        except ValueError:
            print("Ingresa un numero.")

    def crear_fondo(self):
        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.abspath(".")
    
        ruta_imagen = os.path.join(ruta_base, "hola.jpeg")
        self.fondo= ImageTk.PhotoImage(Image.open(ruta_imagen))
        self.fondo_label=tk.Label(self.ventana,image=self.fondo)
        self.fondo_label.place(x=0,y=0,relwidth=1,relheight=1)

    def crear_etiqueta(self):
        self.etiqueta_nombre = tk.Label(text="INGRESA LA ENERGIA ACTUAL",justify="center", anchor="center")
        self.etiqueta_nombre.place(x=90, y=15)
        self.resultado = tk.Label(self.ventana,text="",justify="center", anchor="center")

    def crear_caja_texto(self):
        self.caja_energia = tk.Entry(font="Arial",justify="center")
        self.caja_energia.place(x=150, y=60, width=40, height=30)

    def crear_boton(self):
        self.boton_ingreso = tk.Button(text="BAKUSHIN!!!", command=self.calcular)
        self.boton_ingreso.place(x=132, y=110, width=80, height=30)
