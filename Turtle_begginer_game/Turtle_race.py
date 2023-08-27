import turtle
import random
#Goto start position
Player_one=turtle.Turtle()
Player_one.shape("turtle")
Player_one.color("red")
Player_one.penup()
Player_one.goto(-300,0)
Player_two=turtle.Turtle()
Pl.shape("turtle")
Player_two.penup()
Player_two.color("green")
Player_two.goto(-300,-200)

#Draw home for turtle1

Player_one.penup()
Player_one.goto(300,0)
Player_one.pendown()
Player_one.circle(60)
Player_one.penup()
Player_one.goto(-300,60)
#tur1.goto(300,60)   #Center


#Draw home for turtle2

Player_two.penup()
Player_two.goto(300,-200)
Player_two.pendown()
Player_two.circle(60)
Player_two.penup()
Player_two.goto(-300,-140)
#tur2.goto(300,-140)   #Center

for i in range(20):
    if Player_one.pos()>= (300,60):
        print("Player_one win!")
        exit()
    if Player_two.pos()>=(300,-140):
        print("Player_two win!")
        exit()
    else:
        player_one_turn = input("Player_one: Hit enter to roll-up the dice >")
        dice_num= random.choice([1,2,3,4,5,6])
        print(f"The result of the dice is: {dice_num}")
        Player_one.fd(20*dice_num)
        
        Player_two_turn = input("Player_two: Hit enter to roll-up the dice")
        dice_num= random.choice([1,2,3,4,5,6])
        print(f"The result of the dice is: {dice_num}")
        Player_two.fd(20*dice_num)
        
        
        
turtle.done()
