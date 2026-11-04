# # Recursion 
# # when a func. calls itself until a particular condition is statisfied 
# # - it is also the core mechanism of several.
# # Algo Back-tracking


# def f(n):
#     if(n==4):
#         return
#     print(n)
#     f(n+1)

# f(1)


# {n*factorial(n-1)}
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

print(fact(5))
