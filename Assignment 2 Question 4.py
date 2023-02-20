#COMPLETED
#TESTED

"""
The goal of this game is for the user (player) to guess the 5 character word in a limited 
number of chances.

Pick up at least 50 5 character words (e.g. from https://7esl.com/5-letter-words/ ) 
and save them in a list or any other structure (you can assign them in a statement, 
i.e. hard code them). Select a word at random from this list - for this, 
generate a random number between 0 and length of the list of words using the random number 
generator randint() provided in python (Pls look it up - it is quite easy) - 
this is the index in the list for the word the user has to guess.

Now prompt the user to input a five character string as his/her guess. 
After the guess, the program should show the user the chars from the guess string which are in 
correct places, and correct chars in wrong places, by outputting:
 --a-d (if a and d were in the input string and are in these two places in the word), 
other characters present: b  (if b is present in the word)

Let the user repeatedly give guesses, till either the guess is correct, or the number of tries is 6.

Bonus: Accept from the user only valid words as guesses. 
For this, use an available online dictionary API to check if the given string is a word or not. 
And if not, prompt the user and do not count this attempt.
"""

import random
words = ["abuse", "adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "blood", "drama", "dream", "dress", "drink", "drive", "earth", "enemy", "entry", "error", "event", "faith", "admit", "adopt", "agree", "allow", "alter", "apply", "argue", "arise", "avoid", "begin", "blame", "alcon", "ought", "there", "three", "where", "which", "above", "acute", "alive", "alone", "angry", "aware", "awful", "basic", "black", "blind", "brave", "aback", "abaft", "about", "afoot", "after", "other", "since", "slash", "until", "where", "while" ]

word = words[random.randint(0,len(words))]

output = ["-", "-", "-", "-", "-"]

flag = False
tries = 0

while (flag==False and tries<6):
    alphabets = []
    print("")
    s = input("Enter your guess: ")

    if len(s)!=5:
        print("I TOLD YOU TO ENTER A 5 DIGIT NUMBER! TRY AGAIN!")
        continue

    else:
        tries += 1
        for i in range(len(s)):
            if s[i]==word[i]:
                output[i] = s[i]

            elif s[i] in word:
                if s[i] not in alphabets:
                    alphabets.append(s[i])

    for i in output:
        print(i,end="")

    print("\n")

    if output==list(word):
        flag = True
        print("Congratulations!")
        break

    elif tries==6:
      print(f"Loser! The word is: {word}")
      flag = True
      break

    else:
      print(f"Alphabets in wrong places are: {alphabets}")
      #print("One alphabet could occur more than once.")

    
        
    
