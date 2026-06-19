#programme of creating a number guessing game 
 
import random 
number_to_guess =random.randint(1,100)
 
while True:
  try:  # this try is used for ,when you other than asked it does'nt show error just prints what you codded 

    guess = int(input("guess a number between 1 and 100 :")) #it asks you 

    if guess < number_to_guess:
      print("Too low 😒") # if it is high 

    elif guess > number_to_guess:
      print("Too high 😐")# if it is low
    else:
      print("congrulations!🥳")
      break    
  except ValueError:     # end of the try
      
    
      print("please enter a valid number ☹️")