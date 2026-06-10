#---------WHILE LOOPS------
#A while loop is used when you want to iterate wiht an undefined number of times.
#i = 3 
#while i <= 0:
    #print("Meow")
    #i += 1

#------FOR LOOPS------
#A for loop is used when you need to iterate with a defined number of times.
#for i in range(3):  # range is a built in function in python that's exclusive to the last number but inclusive to the first one.
    #print("meow")   #using _ instead of the variable i tells anyone reading the code "I'm only looping for the count, the value is intentionally ignored."
    
# you can also print miultiple types by multypling the string 3 times and uusing the function end() to remove the extra skipped line by default caused by print
#print("Meow\n" * 3 , end="")

#while True:
    #n = int(input("What's n?: "))
    #if n > 0:
        #break # break is useful in order to break out of for and while loops, in general all types of loops. if/else don't exit out with break

#for i in range(n):
    #print("MEOW")
    
#----WRITING OWN MEOW FUNCTION-----

def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's the number: "))
        if n > 0:
            break
    return n   ## return allows us to specifically return a number from our code.
            
        

def meow(n):
    for _ in range(n):
        print("meow")