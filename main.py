import random
from words import word_list


def get_word():
  word = random.choice()
  return word.upper()
  
def play(word):
  word_completion = "_" * len(word)
  guessed=False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("lets play Hangman!")
  print(display_hangman(tries))
  print(word_comletion)
  print("\n")
  
  while not guessed and tries > 0:
    guess = input("please guess a letter or word: ").upper()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
