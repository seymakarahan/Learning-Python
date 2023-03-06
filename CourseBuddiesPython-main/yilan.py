import random
import turtle
import time
#import sys
#from tkinter import Tk, Frame, Canvas, ALL, NW
delay = 0.1
sayac=0

pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('black')
pencere.setup(width=660, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("white")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.shapesize(0.90, 0.90)
yemek.goto(0, 0)

yemek1 = turtle.Turtle()
yemek1.speed(0)
yemek1.shape("circle")
yemek1.color("yellow")
yemek1.penup()
yemek1.shapesize(0.90, 0.90)
yemek1.goto(64, 13)

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("purple")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "bold"))

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"
def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"

def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"
def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"

pencere.listen()
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_right, "Right")
pencere.onkey(go_left, "Left")

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []

        puan = 0
        delay = 0.1

        yaz.clear()
        yaz.write("Puan: {} ".format(puan), align="center", font=("Courier", 24, "bold"))

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("purple")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "bold"))
        sayac+=1
     
    if sayac%3==0:    
        if kafa.distance(yemek1) < 20:    
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            yemek1.goto(x, y)
    
            yeni_kuyruk = turtle.Turtle()
            yeni_kuyruk.speed(0)
            yeni_kuyruk.shape("square")
            yeni_kuyruk.color("purple")
            yeni_kuyruk.penup()
            kuyruklar.append(yeni_kuyruk)
    
            delay -= 0.001
    
            puan = puan + 15
            yaz.clear()
            yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "bold"))
            
          
    
    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))
            hiz = 0.1

    if puan>99:
        yaz.clear()
        yaz.write("Puan: {} OYUN WİNX".format(puan), align="center", font=("Courier", 24, "bold"))
        move.quit()
        quit()
 

    time.sleep(delay)