a=input('enter the number 1: ')
b=input('enter the number 2: ')
sum=int(a)+float(b)
print(sum) #normal way
# print("the sum is :" +sum) this will throw error cause we cannot concatenate str with float or int
print("the sum is: " + str(sum))