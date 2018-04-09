import turtle
bob = turtle.Turtle()
def polygon(t, n, length):    
    angle = 360 / n     
    for i in range(n):         
        t.fd(length)         
        t.lt(angle)
def circle(t, r):     
    circumference = 2 * math.pi * r     
    n = int(circumference / 3) + 1     
    length = circumference / n     
    polygon(bob, 10, 70)
turtle.mainloop()