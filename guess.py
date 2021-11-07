import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time")
        quit()
else:
    print("please type a number lrger than 0 next time")
    quit()

random_number = random.randint(0,top_of_range)
gauss =0
while True:
    gauss += 1
    user_gues = input("make a gues: ")
    if user_gues.isdigit():
        user_gues = int(user_gues)   
    else:
        print("please type a number lrger than 0 next time")
        continue
    
    if user_gues == random_number:
        print("You got it!")
        break
    else:
        if user_gues >random_number:
            print("you were  above the number!")
        else:
            print("you were below the number!")
print("You got in ",gauss , "guesses")        

