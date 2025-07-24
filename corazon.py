import turtle
import math

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
t.color('red')
turtle.bgcolor('black')

# Función para el corazón
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

# Dibujar corazones concéntricos
t.penup()
for i in range(1, 16):
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 628, 2):
        x, y = corazon(n / 100)
        t.goto(x * i, y * i)
    t.penup()

# Ocultar la tortuga del corazón
t.hideturtle()

# Configurar el mensaje debajo del corazón
mensaje = turtle.Turtle()
mensaje.hideturtle()
mensaje.penup()
mensaje.color("white")
mensaje.goto(0, -250)  # Ajusta este valor si el texto queda muy cerca/lejos
mensaje.write("Lo estás haciendo bien, te amo", 
              align="center", 
              font=("times New Roman", 14, "bold"))

# Finalizar
turtle.done()