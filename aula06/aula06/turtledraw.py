# Exercise 5 on "How to think like a computer scientist", ch. 11.
import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
arquivo = open('drawing.txt' ,'r')
for linha in arquivo:
    if linha == "UP\n":
        t.up()
    elif linha == "DOWN\n":
        t.down()
    else:
        t.goto(int(linha.split()[0]), int(linha.split()[1]))
arquivo.close()



# wait
turtle.Screen().exitonclick()

