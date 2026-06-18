import random #Random is a module inside python 
#ph = int(input("Input a value bwteen 0 and 14"))
#if ph > 7:
 # print("Basic")
#lif ph < 7:
 # print("Acidic")
#else:
 # print("Neutral")

#MAGIC 8 Ball program
number = random.randint(0,8) #generates a random number between 1 and 9 inclusive of both
string = input("Question:  ")
if number == 0:
  answer = ("Yes - definitely.")
elif number ==1:
  answer =(" It is decidedly so.")
elif number == 2:
  answer = ("Without a doubt")
elif number == 3:
  answer =("Reply hazy, try again.")
elif number == 4:
  answer =("Ask again later. ")
elif number == 5:
  answer =("Better not tell you now.")
elif number == 6:
  answer =("My sources say no.")
elif number == 7: 
  answer =("Outlook not so good.")
elif number == 8:
  answer =("Very doubtful. ")
else:
    print("Error")
print("Magic 8 Ball" + answer)

