import time
import tkinter as tk
from Punto import Punto
from Checo import Checo
from Cuadrado import Cuadrado

class Carro2(Punto):
    def __init__(self, canvas, x=0, y=0, size=100, color="black"):
        super().__init__(x, y, color)
        self.setSize(size)
        self.canvas = canvas

    def setSize(self, size):
        if size > 0:
            self.__size = size
        else:
            self.__size = 0

    def getSize(self):
        return self.__size

    def dibuja(self):
        mtz = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 1, 1, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 3, 3, 3, 3, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 5, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 4, 3, 4, 3, 3, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 5, 1, 1, 1,
             0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 5, 5,
             1, 0, 0, 0, 0, 0, 1, 4, 3, 4, 4, 3, 4, 3, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 3, 3, 3, 3, 3, 3, 5,
             1, 5, 0, 0, 0, 1, 3, 3, 3, 4, 3, 3, 4, 3, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 5, 5, 1, 1, 2, 1, 2, 2, 3, 5, 3, 5, 5, 5,
             5, 1, 5, 1, 1, 1, 1, 1, 3, 4, 4, 3, 3, 3, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 6, 6, 1, 1, 5, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 3, 5, 5,
             5, 5, 1, 1, 1, 6, 6, 1, 1, 3, 3, 3, 3, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 6, 1, 1, 1, 1, 1, 6, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
             5, 1, 6, 1, 1, 1, 1, 1, 6, 1, 3, 3, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 5, 5, 1, 1, 1, 1, 6, 1, 1, 7, 7, 7, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
             1, 6, 1, 1, 7, 7, 7, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 5, 5, 5, 5, 1, 3, 3, 1, 6, 1, 7, 8, 8, 8, 7, 1, 6, 1, 5, 5, 5, 3, 3, 5, 3, 3, 3, 5, 3, 3, 5,
             1, 6, 1, 7, 8, 8, 8, 7, 1, 6, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 5, 5, 3, 5, 5, 1, 2, 2, 2, 1, 6, 1, 7, 8, 8, 8, 7, 1, 6, 1, 5, 5, 5, 3, 3, 3, 5, 5, 3, 5, 5, 3, 5,
             1, 6, 1, 7, 8, 8, 8, 7, 1, 6, 1, 0, 0, 0, 0, 0],
            [0, 1, 5, 5, 4, 5, 5, 4, 5, 5, 2, 1, 1, 1, 1, 7, 8, 8, 8, 7, 1, 1, 1, 5, 5, 5, 3, 5, 3, 3, 3, 3, 5, 3, 3, 5,
             1, 1, 1, 7, 8, 8, 8, 7, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 5, 4, 5, 4, 3, 5, 4, 5, 1, 1, 0, 1, 1, 1, 1, 7, 7, 7, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
             1, 1, 1, 1, 7, 7, 7, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 5, 5, 5, 5, 5, 5, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1,
             5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 5, 1, 1, 1, 1, 5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5,
             0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        lado = self.__size // 17

        rb = [0] * 17
        for i in range(17):
            rb[i] = [0] * 52

        for i in range(17):
            for j in range(52):
                if mtz[i][j] == 0:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "")
                elif mtz[i][j] == 1:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "black")
                elif mtz[i][j] == 2:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "yellow")
                elif mtz[i][j] == 3:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "red")
                elif mtz[i][j] == 4:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "white")
                elif mtz[i][j] == 5:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, self.color)
                elif mtz[i][j] == 6:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "gray63")
                elif mtz[i][j] == 7:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "gray26")
                elif mtz[i][j] == 8:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "silver")
                else:
                    rb[i][j] = Cuadrado(self.getX() + (j * lado), self.getY() + (i * lado), lado, "gold")

        for i in range(17):
            for j in range(52):
                rb[i][j].dibuja(self.canvas)


def animacion_desplazamiento(canvas, carro):
    for i in range(100):  # Desplazamiento hacia la izquierda
        canvas.delete("all")  # Borra el lienzo
        carro.setX(carro.getX() - carro.getSize() // 17)  # Actualiza la posición X del carro
        carro.dibuja()  # Dibuja el carro en la nueva posición
        canvas.update()  # Actualiza el lienzo
        time.sleep(0.1)  # Pausa para la animación

# Crear ventana y lienzo
ventana = tk.Tk()
ventana.title("Animación de Carro")

canvas = tk.Canvas(ventana, width=900, height=300)
canvas.pack()

# Crear un objeto carro y dibujarlo
carro = Carro2(canvas, x=800, y=150, size=100, color="blue")
carro.dibuja()


# Ejecutar la animación
animacion_desplazamiento(canvas, carro)

ventana.mainloop()
