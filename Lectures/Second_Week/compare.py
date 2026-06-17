#Control flow is how we direct the flow of the execution of the code
x = int(input("What's x? "))
y = int(input("What's y? "))

'''if x<y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")'''

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
    height = int(input("What's your height: "))
credits = int(input("How many credits do you have? "))
if height >= 137 and credits >=10:
  print("Enjoy the ride!")
elif height < 137 and credits >=10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  ("You have not met the requirements")