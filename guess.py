#importing random module to select random word from the word back
import random
#create a word bank with some words we can add many

word_bank = ["apple","banana","foot","heaven","orchestra","shiver","drink","frame","prosecution","rhetoric","flag","agenda","color","book"]
#choose a random word from the word bank 
word=random.choice(word_bank)
#placeholder
guessedletter = ["_"] * len(word)
# no of attempts the player will get to type correct word
chances = 10

# looping 
while chances > 0:
    print("\nCurrent word is: " + ' '.join(guessedletter))
    #take input and convert in lower case
    user_guess = input("Guess a letter : ").lower()
    #check if input is in our word bank 
    if user_guess in word: 
        for i in range(len(word)):
            if word[i]==user_guess:
                guessedletter[i]=user_guess
        print("Great guess!")
    else: 
        chances-=1
        print(f"Oops! Wrong Guess!      Attempts Left: {chances}")
    print()    
    if '_' not in guessedletter:
        print("Yay! Youve guessed the word correctly!")   
        break
if chances==0 and '_' in guessedletter:

    print(f"You ran out of guesses! The correct word is: {word}")
