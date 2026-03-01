import random
words = ["python", "javascript","java", "automation", "pytest", "guvi","selenium"] # creating a list given in the question

def scramble_word(word): # defining the word
    scramble_word = random.sample(word, len(word)) # using the sample function to select the random word
    return scramble_word



while True:
    scramble_word = random.choice(words) #system choice of words
    user_guess = input() # user input 
    if user_guess == scramble_word: # if both are matching it will print matches the original word
        print ("matches the original word")
    else: #if itis not matched with previos condition, it will print try again
        print("tryagain")
        break