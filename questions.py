# """password validation"""
# # write a function to validate the given password.
# password = input("Enter your password:")



# write a fun. to print each element 

# Write a fun^n to swap 1st and last element of a given tuple.   t=(10,20,30,40,50)


# t = (10, 20, 30, 40, 50)
# t = (10,)
# def swap(t):
#     if len(t) < 2:
#         return t
#     result = (t[-1],) + (t[1:-1]) + (t[0],)
#     return result
# print(swap(t))


# write a fun to Rotate a given tuple by K position.
#  t =(10,20,30,40,50,60) K=2   (50,60,10,20,30,40)


# t = (10,20,30,40,50)
# def swap(t):''''''
# def rotate(t,k):
#     k = k%len(t)
#     print(k)
#     return t[k:] + t[:k]

# print(rotate(t,2))



# t = (1, 2, 3, 1, 4, 5, 8)
# target = 9
# found = False
# for i in t:
#     found = True


# # Write a fun. to print a dictionary which contains the frequancy of each characters of a given string. 

# word = input()

# def f(word):
#     empt_dict ={}

#     for i in word:
#         if i in empt_dict:
#             empt_dict[i] +=1
#         else:
#             empt_dict[i] = 1
#     return empt_dict

# print(f(word))

# # write a function to print the key with the maximm value.

# d1 = {"a":-9,"b":-10,"c":-1}

# def max_key(dict):
#     max_val = (-1)*(2**32)
#     for i in dict:
#         if dict[i]>max_val:
#             max_val = dict[i]
#             max_key = i
#     return max_key

# print(max_key(d1))


# write a function to marge_add(d1,d2) and a

# d1 = {"a":1,"b":9}
# d2 = {"b":10,"c":7}

# for i in d2:
#     if i in d1:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]


# print(d1)
        

d1 = {"a":1,"b":9}
d2 = {"b":10,"c":7}

def f(d1,d2):
    for i in d1:
        for j in d2:
            if (i==j):
                d1[i]=d1[i]+d2[j]
            else:
                