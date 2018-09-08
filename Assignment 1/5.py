nol = int(input("Enter the number of lines in which you want to write :"))
z = []
[z.append(input().upper()) for _ in range(nol)] 
[print(x,end="\n") for x in z]
