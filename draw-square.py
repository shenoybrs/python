import turtle

    
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    santosh = turtle.Turtle()
    santosh.shape("classic")
    count = 0
    turn = 0
    while turn != 10:
        
        #draw_square(santosh)
        draw_triangle(santosh)
        turn = turn +10
        santosh.right(10)       
        
        
    window.exitonclick()

def draw_square(santosh):
    count=0
    while count < 4:
        santosh.forward(100)
        santosh.right(90)
        count = count +1

def draw_triangle(santosh):
    for i in range(1,4):
        santosh.forward(100)
        santosh.left(120)
        
    santosh.forward(100)
    santosh.left(120)
    santosh.forward(50)
    santosh.left(60)

    for i in range(1,4):
        santosh.forward(50)
        santosh.left(120)

    santosh.right(60)    
    santosh.forward(50)
    santosh.left(120)
    santosh.forward(100)
    santosh.left(120)
    santosh.forward(12.5)
    santosh.left(60)
    
    for i in range(1,4):
        santosh.forward(12.5)
        santosh.left(120)

    santosh.right(60)    
    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        if i == 2:
            santosh.forward(12.5)
            santosh.right(120)
            for i in range(1,4):
                santosh.forward(12.5)
                santosh.left(120)
            santosh.left(120)
            santosh.forward(12.5)
            santosh.left(120)
        else:
        
            santosh.forward(25)
            santosh.left(120)

    santosh.right(60)    
    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        santosh.forward(12.5)
        santosh.left(120)

    santosh.right(60)    
    santosh.forward(25)
    santosh.left(60)

    for i in range(1,4):
        santosh.forward(12.5)
        santosh.left(120)

    santosh.right(60)    
    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        if i == 2:
            santosh.forward(12.5)
            santosh.right(120)
            for i in range(1,4):
                santosh.forward(12.5)
                santosh.left(120)
            santosh.left(120)
            santosh.forward(12.5)
            santosh.left(120)
        else:
        
            santosh.forward(25)
            santosh.left(120)

    santosh.right(60)    
    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        santosh.forward(12.5)
        santosh.left(120)

    santosh.right(60)
    santosh.forward(12.5)
    santosh.left(120)
    santosh.forward(50)
    santosh.left(60)
    santosh.forward(50)

    santosh.right(180)

    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        santosh.forward(12.5)
        santosh.left(120)

    santosh.right(60)    
    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        if i == 2:
            santosh.forward(12.5)
            santosh.right(120)
            for i in range(1,4):
                santosh.forward(12.5)
                santosh.left(120)
            santosh.left(120)
            santosh.forward(12.5)
            santosh.left(120)
        else:
        
            santosh.forward(25)
            santosh.left(120)

    santosh.right(60)    
    santosh.forward(12.5)
    santosh.left(60)

    for i in range(1,4):
        santosh.forward(12.5)
        santosh.left(120)

    
draw_art()

