a = [5,7,9,3,2,1,4,2,6,3,0,9,8]
# (i)
[print(i,end=" ") for i in list(filter(lambda x: x<5,a))] 
# (ii)
new_list = list(filter(lambda x:x<5,a)) 
print("\n",new_list)
# (iv)
[print("It's Present! :)") if int(input("Enter number to be checked: ")) in a else print("Not Present :(")]