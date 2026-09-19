#Hangman ASCII Art

hangman_stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
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
      |   |
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
          |
          |
          |
          |
    =========
    """
]

wordlist =("Adventure",
    "Bumblebee",
    "Crocodile",
    "Dandelion",
    "Elephant",
    "Fireworks",
    "Grapefruit",
    "Hummingbird",
    "Icicle",
    "Jigsaw",
    "Kangaroo",
    "Lighthouse",
    "Moonlight",
    "Nebula",
    "Oatmeal",
    "Pineapple",
    "Quicksand",
    "Rainforest",
    "Symphony",
    "Tornado")

#Choose a Random Word for Hangman
import random
choosen_word=random.choice(wordlist).lower()
# print(choosen_word)

print(r"""
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

#Placeholder
print("_ "*len(choosen_word))

#Check
lives=6
game_over = False

correct_sequence=[]
while not game_over:
    display=str("")  #Define Display
    guess=str(input("Make a Guess!")).lower()

    for letter in choosen_word:
        if letter==guess:
            display+=letter
            # display+=" "
            correct_sequence.append(guess)
        
        elif letter in correct_sequence:
            display+=letter
        
        else:
            display+="_"
            
    print(display)

    if guess not in choosen_word:
        lives-=1
        print(hangman_stages[lives])
        
        print(f"\nYou Chose '{guess}' which is not in the word\n")
        print(f"*******{lives}/6 Lives Left, Try another Word!*******\n")

    if "_" not in display:
        game_over=True
        print("****************YOU WIN****************")

    elif lives==0:
        game_over=True
        print("****************YOU LOOSE****************")
    
    else:
        continue   
