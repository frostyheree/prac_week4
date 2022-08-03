"""
CP 1404 - Prac week 4
list warmups
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
#What values do the following expressions have?
#The values above is a list of random numbers
numbers[0]
#This shows the first value in the list
numbers[-1]
#This shows the last value in the list
numbers[3]
#This shows the fourth value in the list
numbers[:-1]
#This shows all the value except for the last
numbers[3:4]
#This shows all the value between the fourth and fifth (but excluding the fifth)
5 in numbers
#This will show if the number "5" is inside the list
#output: True
7 in numbers
#This will show if the number "7" is inside the list
#output: False
"3" in numbers
#This will check if there is the string "3" in the list
#It will be false because there are no strings in the list
numbers + [6, 5, 3]
#This will add the numbers 6, 5, 3 into the list

#Write Python expressions to achieve the following:
#1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
#2. Change the last element of numbers to 1
numbers[-1] = 1
#3. Get all the elements from numbers except the first two
numbers[2:]
#4. Check if 9 is an element of numbers
9 in numbers
