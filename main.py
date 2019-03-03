#Dice Roller
#By Aneesh Poddutur
#Copyrighted 2019

#NOTE: Syntax 2 is BROKEN. The number of dice is set to 2. USE AT YOUR OWN RISK!

#import
import random
import time

#list definition
listofnumbers = [1, 2, 3, 4, 5, 6]

#intro
print ("Welcome to the dice roller!")
time.sleep(1)
noofdice = input("How many dice do you want to roll?")
print("Cool!")
time.sleep(0.5)
trialsofroll = input("How many trials would you like to run?")
print("Got it!")
print("Here are the results:")

#define functions

#Syntax 1
#def roll(noofdice, listofnumbers):
    #numberofdicecount = 1
    #while(numberofdicecount <= noofdice):
            #print ("Dice " + str(numberofdicecount) + ": " + str(random.choice(listofnumbers)))
            #numberofdicecount = numberofdicecount + 1
            
#Syntax 2
numberofdicecount = 1
def roll(noofdice, listofnumbers):
        global numberofdicecount
        print("Trial " + str(numberofdicecount) + ": " + str(random.choice(listofnumbers)) + ", " + str(random.choice(listofnumbers)))
        numberofdicecount += 1
        
#execute
numberofrolls = 1
while(numberofrolls <= trialsofroll):
    roll(noofdice, listofnumbers)
    numberofrolls = numberofrolls + 1

#finale
print("Those are the results!")

