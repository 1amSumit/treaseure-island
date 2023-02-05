print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
enterrr = input("press enter to start the game").lower()

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
round1 = input("Hey!! wait... you are on the way which had two direction one is left and other is right and... there is only one direction of the lane is correct and if you choose the right one you will move to next round other wise you will fail in finding the TREASURE so type 'left' for left and 'right' for right direction of lane\n").lower()

if round1 == 'left':
  round2 = input ("Well done you have successfully passed that that was not so difficult i suppose , so you have now reached to the ocean side and you have to move to island , so type 'wait' to wait for the boat to come and drop you there and type 'swim' to swim to that island , so good luck!!\n").lower()
  if round2 == "wait":
    round3 = input("Good job! you have reached to the last level of this game and you are at the bottom of that island and you three doors of different colours red blue and yellow , now you need to choose the color of door very carefully if you fail you won't able to reach back home so be carefull , so type 'red' for red colour door 'blue' for blue colour door 'yellow' for yellow colour door . Good Luck!! \n").lower()
    if round3 == "yellow":
      print("Well done my friend you have completed this game. I hope you have enjoyed this game.")
    elif round3 == "red":
      print("Hey man you have choosed the wrong coloured door inside it there was a burning fire inside . You loose it good luck next Time")
    elif round3 == "blue":
      print("Hey man you have choosen the wrong coloured door inside it there was big big lazerds . so my friend better luck next time")
  elif round2 == "swim":
    print("Bro you cant swim this big ocean because it full of wild aquatic animal which wont allow you to pass the ocean. Game over better luck next time.....")
else:
  print("Hallo Haloo you have fallen into a black hole. Game over better luck next time...")
    


  



