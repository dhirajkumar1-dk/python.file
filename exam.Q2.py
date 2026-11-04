n = int(input("Enter number of values: "))

numbers = []
for i in range(n):
    value = float(input(f"Enter number {i + 1}: "))
    numbers.append(value)

largest = max(numbers)
small = min(numbers)
average = sum(numbers)/len(numbers)
total = sum(numbers)

positive = 0
negative = 0
zero = 0 

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero  += 1
even = 0 
odd = 0
for num in numbers:
    if num%2 == 0:
        even += 1
    else:
        odd += 1

print(numbers)
print(largest)
print(small)
print(average)
print(total)
print(positive)
print(negative)

 
