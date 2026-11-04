# remove dublicate from string.

s = input()
clean_s = s.strip()

def remove_dublicates(s):
    # empty string
    temp_empty = ""
    for i in s:
        if i not in temp_empty:
            temp_empty +=i
    return temp_empty

print(remove_dublicates(clean_s))

#  SWAPCASE
# s= "Recursion function 24"
# 1. write function
# 2. write a recursion function

