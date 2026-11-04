# nested loops
# number of rows = n
n = int(input("num: ")) 
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()