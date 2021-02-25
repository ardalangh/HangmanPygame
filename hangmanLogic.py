wrd  = "apple"
displayList = []


def didWin(displayList):
    return "-" not in displayList


for character in wrd:
    displayList.append("-")

print("Hello welcome to hangman guess a letter")
print(displayList)



while (not didWin(displayList)):
    guess = input("choose a lowercase letter: ")

    for i, character in enumerate(wrd):    
        if character == guess:
            displayList[i] = character
        
        


    print(displayList)


















