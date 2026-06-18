import random 
choices = ("r",'p',"s")

emojies = {"r":"🪨","p":"📃","s":"✂️"}
          
def get_user_choice():
  while True:
    user_choice = input("chose one rock, paper , scissor(r/p/s):")
    if user_choice  in choices:
     return user_choice 
  else:
    print("invalid choice")

def display_choices(user_choice , computer_choice):
   print(f"you chose{emojies[user_choice]}")
   print(f"computer chose{emojies[computer_choice]}")

 
def show_the_winner(user_choice,computer_choice):
    if computer_choice == user_choice:
      print("Tie")
    elif \
     (computer_choice == "r" and user_choice == "p") or\
     (computer_choice == "p" and user_choice == "s") or\
     (computer_choice == "s") and user_choice == "r" :
     print("you won")
    else:
     print("you lose")
def play_game():
  while True:
   user_choice=   get_user_choice()
   computer_choice = random.choice(choices)
   display_choices(user_choice , computer_choice)
   show_the_winner(user_choice , computer_choice )

   should_continue = input("do you  want to continue(y/n)")
   if should_continue == "n":
    print("thanks for playing")
    break
play_game()