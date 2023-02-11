# program that prints out a random number between 1 and 10
# version to take input of range from user
import random

x = int(input("Enter first number in range: "))
y = int(input("Enter second number in range: "))




number = random.randint(x,y)




print("here is a random number {}".format(number))