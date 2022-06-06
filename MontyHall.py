import random
playAgain = True
while playAgain:
    numberOfDoors = input("how many doors do you want?: ")
    numberOfIterations = input("how many times would you like to run the program: ")
    doesUserSwitch = input("would you like to switch the doors or not? (Y/N ONLY): ")
    counter = int(numberOfIterations)
    initcounter = counter
    score = 0
    playAgain = True
    while(counter >= 0):
        CorrectDoor = False
        doors = list(range(1,int(numberOfDoors) + 1))
        prizeDoor = random.choice(doors)
        userDoor = random.choice(doors)
    
        if(prizeDoor == int(userDoor)):
            CorrectDoor = True
            switch = doesUserSwitch
        else:
            CorrectDoor = False
            switch = doesUserSwitch
    
    
        if (CorrectDoor and switch == "N") or ( (not CorrectDoor) and switch == "Y"):
            score = score + 1
        
        counter = counter - 1
    
    print("You are correct " + str(score*100/initcounter) + " percent of the time")
    
    doesUserGoAgain = input("Would you like to go again? (Y/N): ")
    
    if doesUserGoAgain != "Y":
        playAgain = False