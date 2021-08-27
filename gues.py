import time
import random

print("I am Abdullahi.\nI use to write it.\nwellcome to use it")
# print it is mining see
variablle = input("Do you wan to play: ")
answer = "yes"

if variablle != "yes":
    print("you are done")
    quit()
#The mining of if it is first   
else:
# And else it is a last
    print("let start game")


score = 0

# t this score is avariable has a integer and this = equel give the variable job

variablle1 =int(input("guse a number? "))
# The variable1 it has integer and question the question isgues a numbe?

variablle2 = random.randint(1,4)
# The random a library randint it is chapter

if variablle2 != variablle1:
    print("you wrong")
elif variablle2 > variablle1:
    print("your number is biger", variablle2)
else:
    print("your number is smaller", variablle2)
    score = score +1
 #this score is avariable has a integer and this = equel give the variable job

variable1 = int(input("guse a number? "))
# The variable1 it has integer and question the question is gues a numbe?

variablle2 = random.randint(1,4)
# The random a library randint it is chapter

if variablle2 != variablle1:
    print("you wrong")
elif variablle2 > variable1:
    print("you number is biger", variablle2)
else:
    print("you number is smaller", variablle2)
    score = score +1
# t this score is avariable has a integer and this = equel give the variable job

variablle1 =int(input("guse a number? "))
# The variable1 it has integer and question the question isgues a numbe?

variablle2 = random.randint(1,4)
# The random a library randint it is chapter

if variablle2 != variablle1:
    print("you wrong")
elif variablle2 < variable1:
    print("you number is smaller", variablle2)
else:
    print("your number is biger", variablle2 )    
    score = score +1
 #this score is avariable has a integer and this = equel give the variable job

# this score is avariable has a integer and this = equel give the variable job

variablle1 =int(input("guse a number? "))
# The variable1 it has integer and question the question isgues a numbe?

variablle2 = random.randint(1,4)
# The random a library randint it is chapter

if variablle2 != variablle1:
    print("you wrong")
elif variablle2 < variable1:
    print("your number is smaller", variablle2)
else:
    print("your number is biger", variablle2)
    score = score +1
# this score is avariable has a integer and this = equel give the variable job

variablle1 =int(input("guse a number? "))
# The variable1 it has integer and question the question isgues a numbe?

variablle2 = random.randint(1,4)
# The random a library randint it is chapter

if variablle2 != variablle1:
    print("you wrong")
elif variablle2 < variable1:
    print("your number is smaller", variablle2)
else:
    print("your number is biger", variablle2)    
    score = score +1


print("you got " + str(score) + "marks")

print("you are done, plese wait for 5.....")

time.sleep(5)
