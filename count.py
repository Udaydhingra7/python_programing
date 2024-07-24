n= int(input("Enter the number : "))
count=0
if n<0:
    n = -1*n
if n==0:
    count=1
while n!=0:
    n= n//10
    count+=1
print("The numberof digits are: ", count)