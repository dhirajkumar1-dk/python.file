# n = int(input())
# print()
# def dp(n):
#     while (n!=0):
#         id = n%10
#         print(id)
#         n = n//10


# dp(n)

# #scope  (local , globle scope) important topic


# x= 10                # Globle variable

# def fn():
#     global x         #globle key word
#     x = 9
#     print(x)

# print(x)
# fn()                 # function call

# print(x)


x = 10 
y = 20

e = lambda x,y: x+y
e = lambda x,y: x**y
print(e)
print(e(x,y))