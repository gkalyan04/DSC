def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

n = input("Enter numbers seperated by comma(,) :").split(",")
[print(i,end=",") for i in list(map(lambda x:factorial(int(x)),n))]