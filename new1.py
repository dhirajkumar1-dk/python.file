# Q. write a func^n to print the length and printthe largth word of the given sentance.
s = "First Programe for every coder is Hello World Language"
clean_s = s.strip()

def max_len_str(str1):
    max_len = 0
    slist = str1.split()
    for i in range(len(slist)):
        if len(slist[i]) > max_len:
            max_len = len(slist[i]) 
    return max_len

print(max_len_str(clean_s))

# print disknary

# write a function to calculate the no. of 1- constant 2- special charecters 3- Digits 4- spaces 5- vowels.