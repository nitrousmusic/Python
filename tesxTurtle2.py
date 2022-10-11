import turtle


#this is only for the 'Screen'
background = turtle.Screen()
# this is my 'Class' of the 'Method' with the turtlr
t1000 = turtle.Turtle()
#this is the 'circle' alone = '100' radius
t10002 = turtle.Turtle()



#this is the backGround and lets me put 'bgpic' but not for the 't1000 = turtle.Turtle

#for background.'bgcolor'
background.bgcolor("lightgreen")
#in 'addshape' I loaded the 'NitrousTurtle' to pass to 't1000 = turtle.Turtle()'. You can also use 'bgpic' put cant 'passit' to 't1000'
background.addshape("turtle?.gif")
#change the 'POSTION' for the 'Screen' to 'startx=0, starty=0
background.setup(width=800, height=800, startx=100, starty=100)

#this pick ups the 'pen' = 'penup'
t1000.penup()


def main():
    t1000.goto(285, -230)
    t1000.shape("turtle?.gif")

    #make an 'if statement' to have them run together
    t10002.circle(100)
    t1000.circle(100)
    return
main()


#this exits the program once the 'Screen' is clicked
turtle.exitonclick()








#def myTurtleNitrousMusic():



    #t1000.penup()
    #t1000.pendown()


#myTurtleNitrousMusic()






#'turtle.done()' will stop the window once it shows what your done. keeps it turtle in the screen'turtle.done'
#turtle.done()


