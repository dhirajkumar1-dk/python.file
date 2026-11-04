# ARM strong number

n =int(input("Enter the number :-"))
temp = n
sum = 0

while(temp>0):
    num = temp%10
    sum = sum+num**3
    temp = temp//10

if(sum==n):
    print("Yes this is Arm Strong number")

else:
    print("No this is not Arm Strong number")




