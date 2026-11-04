# n=10

# for i in range(1,n+1):
#     if i == 4:
#         continue
#     print(i)

# print("hello")


# print all the odd numbers from 1 to n using Break/Continue.

# n=10
# for i in range(1,n+1):
#     if i%2 == 0:
#         continue
#     print(i)


# Question

# n = int(input())

# def f (n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2

#     return f(n-1) + (n-2)

# print(f(5))


# Find the sum of all the numbers from 1 to n using Recursion .

# n = int(input())

# def f (n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     if n==3:
#         return 3
#     if n==4:
#         return 4
    
# Calculate (a^b) and using recursion only and do not use ** or pow().

def f(a,b):
    if b ==0 :
        return 1
    return a * f(a,b-1)
print(f(2,5))


# Check weather a number is an Armstrong number using recursion.
