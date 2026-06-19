 #building a diece game 
import random   

while True: # i used while loop to rotate the process 
   
   choice = input("roll the dice (y/n):🎲").lower() #it asks the choice

   if choice =="y" :
     die1 = random.randint ( 1 , 6 )  #random will genearte a randim number 

     die2 = random.randint( 1 , 6  )#random will genearte a randim number

     print(f"({die1},{die2})")
   elif  choice == "n":
     print("thanks for playing! 😤")
     break     # while i used it for to stop the repeting loop
   
   else:
     
     print("invalid choice😲")
     


