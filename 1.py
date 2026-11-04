# Write a program to find the frequency of every digit present in a number.

n = input("Enter a number: ")

count = [0] * 10

i = 0
while n[i:]:
    count[int(n[i])] += 1
    i += 1

i = 0
while i < 10:
    if count[i] > 0:
        print(i, ":", count[i])
    i += 1