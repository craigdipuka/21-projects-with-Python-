print( "Welcome to the Computer Quiz ")

play = input("Would you like to continue Yes/No ?\n")
play = play.lower()

count =  0
if play != "yes":
    quit()
else:
    print("okay lets play :)\n" )
    print("Score: " , count)



answer = input("what does CPU stand for ?\n")
if answer == "central processing unit":
    print("you got it !")
    count +=1
else:
    print("you got it wrong :( ")

