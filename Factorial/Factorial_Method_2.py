# THIS IS Second METHOD TO FIND OUT FACTORIAL

while True:
    number = int(input("Please Enter The Number bigger then 0 and less then 10: "))


    def factorial(number):
        initial = 1
        for i in range(1, number+1):
            initial = initial*i
        return initial


    if 0 < number < 10:
        result = factorial(number)
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