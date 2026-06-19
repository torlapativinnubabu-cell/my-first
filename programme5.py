
import random
words = [
    "apple", "river", "mountain", "python", "sunshine", "book", "cloud", "music", "forest", "dream",
    "guitar", "ocean", "flower", "castle", "planet", "star", "light", "shadow", "mirror", "stone",
    "bridge", "garden", "storm", "desert", "island", "tree", "fire", "water", "earth", "wind",
    "sky", "rain", "snow", "ice", "sand", "gold", "silver", "bronze", "iron", "steel",
    "lion", "tiger", "bear", "wolf", "eagle", "hawk", "fish", "whale", "shark", "dolphin",
    "horse", "camel", "zebra", "monkey", "dog", "cat", "rabbit", "mouse", "rat", "snake",
    "king", "queen", "prince", "princess", "knight", "wizard", "witch", "dragon", "giant", "elf",
    "fairy", "ghost", "spirit", "angel", "demon", "monster", "robot", "alien", "hero", "villain",
    "city", "village", "town", "road", "street", "house", "home", "school", "temple", "church",
    "bookstore", "library", "market", "shop", "tower", "palace", "fort", "wall", "gate", "door"
]
#computer random word
computer = random.choice(words)
#instalize dash for the list 
dash_blank = ['_']*len(computer)
attempts = 6
game_over = False
stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

print(" ".join(dash_blank))

def play_game():
    while not game_over:

        user_guess = input('guess a letter to find the word :').lower()

        #checking and updating the user guess
        for position in range(len(computer)):
            letter = computer[position]
            if letter == user_guess:
                dash_blank[position] = user_guess
                
                #print the update blank for progress
                print(" ".join(dash_blank))

                # checking   lose 
        if user_guess not in computer:
            attempts -= 1
            print(f'wrong guess remaining attempts:{attempts}')
            print(stages[6 - attempts])
            if attempts == 0:
                print(f"0 attempts you lose the game the correct word is { computer}")
                game_over = True
                print('game over')

                # win case check
        if '_' not in dash_blank:
            game_over = True
            print('you win')
play_game()



