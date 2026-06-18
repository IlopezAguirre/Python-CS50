###-----THIS IS A CHECKPOINT PROJECT-------###

#==================
#Area Calculator 📐
#==================

import math
area = 0
answer = 0
while answer != 5:
    
    print('''      1) Triangle
      2) Rectangle
      3) Square
      4) Circle
      5) Quit''')
    answer = int(input("Which shape: "))
    if answer == 3:
        side = int(input("Side: "))
        area = side ** 2
        print(f' The area is: {area} ')
    elif answer == 2:
        length= int(input("Length: "))
        width = int(input("Width: "))
        area = length * width
        print(f' The area is: {area} ') 
    elif answer == 1:
        base = int(input('Base: '))
        height = int(input("Height:"))
        area = (height * base) / 2
        print(f' The area is: {area} ')
    elif answer == 4:
        radius = int(input("Radius: "))
        area = math.pi * (radius ** 2)
        print(f'The area is: {area}')
    elif answer == 5:
        break
