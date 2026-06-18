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
  
  ###WEIGHT CHALLENGE ## IF & ELSES FLOW CONTROL 
  # Write code below
earth_weight = float(input("What's your weight on earth: "))
planet_number = int(input("What's your planet number: "))
if planet_number == 1:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif planet_number == 2:
  destination_weight = earth_weight * 0.91
  print(destination_weight)
elif planet_number == 3:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif planet_number == 4:
  destination_weight = earth_weight * 2.53
  print(destination_weight)
elif planet_number == 5:
  destination_weight = earth_weight * 1.07
  print(destination_weight)
elif planet_number == 6:
  destination_weight = earth_weight * 0.89
  print(destination_weight)
elif planet_number == 7:
  destination_weight = earth_weight * 1.14
  print(destination_weight)
else:
  print('Invalid number')
  
##New Year Count down
for i in range(10,0,-1):
  print(i)
print("Happy New Year! 🥳")
