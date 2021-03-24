import random


file1 = open("words.txt", "r")

words = file1.readlines()
for i, w in enumerate(words):
    words[i] = w[0:-1]

randomWrd = random.choice(words)




wrd  = randomWrd












displayList = []
wrongAns = []








def didWin(displayList):
    return "-" not in displayList


for character in wrd:
    displayList.append("-")

print("Hello welcome to hangman guess a letter")
print(displayList)



while (True):
    if len(wrongAns) == 6:
        print("you lost")
        break


    if didWin(displayList):
        print("you won")
        break


    guess = input("choose a lowercase letter: ")
    for i, character in enumerate(wrd):    
        if character == guess:
            displayList[i] = character
        
    
    if guess not in wrd:
        print("wrong")
        wrongAns.append(guess)
        print(wrongAns)
    else:
        print(displayList)
            
        
        


    


















