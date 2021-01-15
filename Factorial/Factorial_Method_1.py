# THIS IS FIRST METHOD TO FIND OUT FACTORIAL


import math

while True:
    # number input
    number = int(input("Please Enter The Number bigger then 0 and less then 10: "))

    if 0 < number < 10:
        result = math.factorial(number)
        print("The Factorial of", number, "is", result)

    elif number < 0:
        print("Number is less then 0")
    else:
        print("number is bigger or equal to 10")

    answer = input("Do You Want To Repeat? (y/n): ")
    if answer == "y":
        continue
    else:
        exit()
