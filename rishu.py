def count(s):
    s=s.lower()
    v=0
    c=0
    sc=0
    d=0
    space=0
    for i in s:
        t="aeiou"
        if i.isalpha():
            if i in t:
                v=v+1
            else:
                c=c+1
        elif i.isdigit():
            d=d+1
        elif i.isspace():
            space=space+1
        else:
            sc=sc+1
    return v,c,d,space,sc
s=input("Enter a String")
print(count(s))