
def pal(str):
    if len(str)<=1:
        return True

    elif str[0] == str[len(str)-1]:
        return pal(str[1:len(str)-1])
    else:
        return False


while True:

    string = input("Please Enter Your String: ")

    if pal(string.lower()):
        if len(string.lower())%2 == 0:
            print("Even Palindrome")
        else:
            print("Odd Palindrome")

    else:
        print("This is not a palindrome")

    answer = input("Do you want to repeat? (y/n): ")
    if answer == "y":
        continue
    else:
        exit()
