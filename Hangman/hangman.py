import random
from hangman_words import word_list 
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#logo
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display=[]

for _ in range(word_length):
  display.append('_')
print(stages[lives])
print(f"{' '.join(display)}\n")
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
while end_of_game == False :

  guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

  ##TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print(f"{guess} has already been used")
  
# def check_letters(chosen_word,guess):
# for idx, j  in enumerate(chosen_word):
#     if j == guess.lower():
#       display[idx]= guess
    
# check_letters(chosen_word,guess)
  for j in range(word_length):
    letter = chosen_word[j]
    if letter == guess:
      display[j] = guess

  if guess not in display:
    lives -=  1
  #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
  if guess not in chosen_word:
     print(f'\n{guess} is not in this word')

  print(stages[lives])
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}\n")

  
  if "_" not in display:
    end_of_game = True
    print("You win!!!")
  elif lives == 0:
    end_of_game = True
    print("Dead!! You Lose.")
