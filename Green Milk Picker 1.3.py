# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random
import shelve

def writePastWinners(currentWinners):
    winnersFile = shelve.open('pastWinners')
    winnersFile['pastWinners'] = currentWinners
    winnersFile.close()
    
def readPastWinners():
    winnersFile = shelve.open('pastWinners')
    pastWinners = winnersFile['pastWinners']
    return list(pastWinners)

def printPastWinners():
    pastWinners = readPastWinners()
    return (print (list(pastWinners)))        

def milkPick(studentNames, excludeNames, pastWinners):
    firstWinNum = 0
    secondWinNum = 0
    
    print()
    print('-------------------------------------------------')
    print()
    print('Sheep Class Random Milk Picker')
    print()
    print()
    print("Today's class includes:")
    print(studentNames)
    print()
    print(excludeNames, 'do(es) not like milk and so do(es) not play the game')
    print()
    printPastWinners()
    print('won last time')
    print()
    chosenState = 'not'
    while chosenState == 'not':
        
        while firstWinNum == secondWinNum: # This code starts the system but also that the same student can't win twice
            
            firstWinNum = random.randint(0,9)
            secondWinNum = random.randint(0,9)
       
        chosenState = 'yes'
    
    
       
        firstWinner = studentNames[firstWinNum]
        secondWinner = studentNames[secondWinNum]
    
       
        if firstWinner in excludeNames: # This checks that the student is essentially able to drink milk
            
            chosenState = 'not'
            firstWinNum = 0
            secondWinNum = 0 # This is important - set the nums to the same value! If it's different it will loop forever.
            
        if secondWinner in excludeNames: # Since two students are picked, this needs to be done twice
            
            chosenState = 'not'
            firstWinNum = 0
            secondWinNum = 0 # As above. Trust me, this is important this way.
        if firstWinner in pastWinners:
            pastWinners.remove(firstWinner)
    
            chosenState = 'not'
            firstWinNum = 0
            secondWinNum = 0
            
        if secondWinner in pastWinners:
            pastWinners.remove(secondWinner)
    
            chosenState = 'not'
            firstWinNum = 0
            secondWinNum = 0
        currentWinners = [firstWinner, secondWinner]
        
        writePastWinners(currentWinners)
    
    print ('The students who get the green milk today are:' , firstWinner, 'and' , secondWinner) 
    print()
    print()
    print('Enjoy your milk!')
    print()
    print('-------------------------------------------------')
    input('press Enter to close the program')
    
firstWinner = 'nobody'
secondWinner = 'no-one'
studentNames = ['Alex', 'James', 'Victoria', 'Colin', 'Sophia', 'Anna', 'Eileen', 'Joshua', 'Jia', 'Ryan']
excludeNames = ['Alex']
pastWinners = readPastWinners()

milkPick(studentNames, excludeNames, pastWinners)