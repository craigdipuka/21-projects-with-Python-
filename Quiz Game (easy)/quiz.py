print( "Welcome to the Computer Quiz ")

play = input("Would you like to continue Yes/No ?\n")
play = play.lower()

count =  0 #point count

if play != "yes":
    print ("okay , have a good day :) ")
    quit()
else:
    print("okay lets play :)\n" )
    print(" Current Score: " , count , "\n")


# questions start  

answer = input("what does CPU stand for ?\n")
if answer.lower() == "central processing unit":
    print("you got it !")
    count +=1
else:
    print("you got it wrong :( ")


answer = input("\n what does GPU stand for ?\n")
if answer.lower() == "graphics processing unit":
    print("you got it !")
    count +=1
else:
    print("you got it wrong :( ")


answer = input("\n what does HDD stand for ?\n")
if answer.lower() == "hard drive disk":
    print("you got it !")
    count +=1
else:
    print("you got it wrong :( ")


answer = input("\n what does OS stand for ?\n")
if answer.lower() == "operating system":
    print("you got it !")
    count +=1
else:
    print("you got it wrong :( ")


answer = input("\n  what does PC stand for ?\n")
if answer.lower() == "personal computer":
    print("you got it !\n")
    count +=1
else:
    print("you got it wrong :( ")

points = count/5 *100 
print(f"you got {points}%")