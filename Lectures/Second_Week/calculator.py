#-----INTEGERS-------#
#Concatenates string
'''x =input("What's x? ")
y = input("What's y? ")
z = x+y
print(z)'''

'''x =input("What's x? ")
y = input("What's y? ")
z = int(x)+int(y) #int() is a function that takes a parameter like a string makes it an int
print(z)'''

#you can nest functions -- function inside another function
'''x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)'''

#float: is a floating point value- decimal in value
#round is a function that takes two parameters (one number, (optional)the number of digits)
#x = float(input("What's x? "))
#y = float(input("What's y? "))
#z = (x + y)
#print(f"{z:,}")

def main():
     x = int(input("What's x?"))
     print("x squared is", square(x))

def square(n):
     return n * n 

def power(n):
    x = int(input("What's x?"))
    return (n,2)

main()

