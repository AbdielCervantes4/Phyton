#PruebaPoly.py
from tkinter import *
import tkinter as tk
from Checo import Checo
from Nube import Nube
from Per import Per
from Fondo2 import Fondo2
from Carretera2 import Carretera2
from Carro import Carro

ventana = tk.Tk()
ventana.title(" ***  Figuras  *** ")
ventana.geometry("640x850")
lienzo = Canvas(ventana, width=640, height=850, bg="cyan")
lienzo.pack()

x = 360
figuras = [
           Fondo2(0,330,700,300,"DodgerBlue2"), Nube(160,80,150,"sky blue"), Nube(460,55,70,"sky blue"), Nube(540,80,100,"sky blue"),
           Carretera2(0,600,700,200,"gray42"), Checo(260, 350, 150, "navy"),Per(180,140,20, "black"),
           Carro(100, 530, 100, "navy")]

for f in figuras:
    f.dibuja(lienzo)


ventana.mainloop()
