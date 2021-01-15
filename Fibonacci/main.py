while True:

    nterms = int(input("How many terms?: "))

    n1,n2 = 0,1

    if nterms<=0:
        print("please enter positive integer")
    elif nterms==1:
        print("Fibonacci Sequence upto", nterms)
        print(n1)
    elif nterms==2:
        print("Fibonacci Sequence upto", nterms)
        print(n1)
        print(n2)
    elif 2 < nterms < 20:
        print("Fibonacci Sequence upto", nterms)
        print(n1)
        print(n2)
        for i in range(1,nterms-1):
            n3= n1+n2
            n1=n2
            n2=n3
            print(n3)
    elif nterms >= 20:
        print("Please Enter Number less then 20")
    answer = input("Do you want to repeat? (y/n): ")
    if answer == "y":
        continue
    else:
        exit()