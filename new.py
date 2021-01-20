import random
import turtle as t

t.bgcolor('black')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('white')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape((0, 0), (20, 0), (20, 20), (0, 20))
t.register_shape('leaf', square)
leaf.shape('leaf')
leaf.color('yellow')
leaf.penup()
leaf.speed(0)

game_startet = False
text_turtle = t.Turtle()
text_turtle.write('Drpcke Leertaste', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)