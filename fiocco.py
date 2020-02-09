from turtle import *
#impostazioni
pencolor("white")
shape("turtle")
speed(10)
pensize(4)
Screen ().bgcolor("turquoise")

#usiamo le funzioni
def forma():
  right(25)
  forward(50)
  backward(50)
  left(50)
  forward(50)
  backward(50)
  right(25)

def fiocco():
  for i in range(0,4):
    forward(30)
    forma()
  backward(120)
  
i=0
while i<8:
  fiocco()
  right(45)
  i=i+1
