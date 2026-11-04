# list1 = [10,20,30,40,50,60,70,80,90,100]
# list2= ["Rugta",0.9,False,77]
# print(list1)
# tuple1 = [10,20,30,40,50,60,70,80,90,100]
# # print(tuple)

# print(max(list1))
# print(min(list1))
# print(sum(list1))

# list1.append(110)
# print(list1)

# print(list1.insert(6,55))
# print(list1)
# print(list1.count(1))
# print(list1.index(20))

# li3 = [i for i in range(1,11)]
# print(li3)

# li4 = [i for i in range(50,101) if i%2 ==0]
# print(li4)
# li6 = [78,99,1010,"li4",5.0]
# for i in range(len(li6)):
#     print(li6[i])

# for i in li6:
#     print(i)

# # Unpacking of tuple

# st1 = ("Ravi", 21 ,85)
# name,age,per_st1 = st1
# print(name)
# print(age)
# print(per_st1)


# # Swaping

# a=10
# b=20

# a,b=b,a
# print(a)
# print(b)

# # Tuple to list and list to tuple

# 11 = [1,2,2,3]
# t1 = (5,56,6,7)

# print(tuple(11))



#  create a new list from an        tuple, where each of the
# new element of list should the cube of the elements of tuple if and Only it the elements are odd. t1 = (56,67,99,87,31,32)


t2 = (56,67,99,87,31,32)
li_new = [i**3 for i in t2 if i%2 != 0]
print(li_new)