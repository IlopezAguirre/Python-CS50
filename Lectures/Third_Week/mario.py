#def main():
    #print_column(3)
    #print_row(4):
     #print_square(3)   
#def print_column(height):
    #for _ in range(height):
        #print("#")
        
#def print_row(width):
    #print("?"* width)

#def print_square(size):
 #  for i in range(size):
        
        #For each brick in row
  #      for j in range(size):
            #Print brick
    #        print("#", end="")
   #     print("#") 
#main()
##FINISHED LOOPS 

#----CHALLENGES------
##----FIZZZ BUZZZ CHALLENGE----
#or number in range(1,101):
   # if number % 3 == 0:
       # print("Fizz")
    #elif number % 3 == 0 and number % 5 == 0:
       # print("FizzBuzz")
    #elif number % 5 == 0:
       # print("Buzz")
    #else:
       # print(number)
contacts = {}     
while True:
    print("1) Add a contact ")
    print("2) Look up the contact")
    print("3) Quit")
    n = int(input("Pick one of the options: "))
    if n == 1:
        contacts["name"] = input(("What's your name? "))
        contacts["number"] = input("What's your phone number?")
    elif n == 2:
        name = input("What's the name: ")
        if name in contacts:
            print(f'number: {contacts["number"]}')
        elif name != contacts["name"]:
            print("The name is not registered")
    elif n == 3:
        break




       

