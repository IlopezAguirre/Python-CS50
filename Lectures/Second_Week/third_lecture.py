#-----CONDITIONALS------

score = int(input("What's the score: "))

if score >= 90 and score <=100:
    print("Your grade is an A")

elif score >=80 and score < 90:
    print("Your grade is a B")

elif score >=70 and score < 80:
    print("Your grade is a C")

elif score >=60 and score < 70:
    print("Your grade is a D")
else:
    print("Your grade is an F")

#bool is a boolean value that can only be tru or false
# this type of expression() return True if n % 2 else False) is called a ternary expression also called a pythonic way of wirting 
#they keyword match allows us to match cases depending on the values of the variables and if they match
#EX:

name = input("What's your name? ")
match name:
    case "Harry" | "Hermione"| "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _ :
        print("Who?")
    
