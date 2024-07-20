age=int(input("Enter your age:"))
if age>=18:
    print("you are an Adult :)")
else: 
    print("CHHOTI BACHI HO KYAA!!!")
print("Thnakyou")



number=int(input("Enter any number:"))
if number%2==0:
    print("Given number is Even :)")
else:
    print("Given number is Odd :(")



Number=int(input("Enter the number:"))
if Number%5==0:
    print("Hellow")
else:
    print("bye")



unit=int(input("Enter Electricity Units used:"))
if unit<=100:
    print("No charge")
if 101<=unit>=200:
    bill= unit*5
    print("the total charges are:"+str(bill))
if unit>=201:
    bill=unit*10
    print("the total charges are:"+str(bill))


Digit=int(input("Enter the digit:"))
print("The last digit is:"+str(Digit%10))


digit=int(input("Enter the digit:"))
a= digit%10
if a%3==0:
    print("The last digit is devisible by 3")
print(" not divisible;")
print("thankyou, End of progrm")
