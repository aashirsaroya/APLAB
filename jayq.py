n=int(input("enter the order of 2 square matrices: "))
dict1={}
l1=[]
dict2={}
l2=[]
dict3={}
l=[]
for i in range(n*n):
    ele=int(input("enter val: "))
    l1.append(ele)
    if(ele):
        dict1[i]=ele
print(dict1)
for i in range(n*n):
    ele=int(input("enter val: "))
    l2.append(ele)
    if(ele):
        dict2[i]=ele
print(dict2)
for i in dict1.keys():
    dict3[i]=dict1[i]
for i in dict2.keys():
    if(i in dict1.keys()):
        dict3[i]+=dict2[i]
    else:
        dict3[i]=dict2[i]
print(dict3)
for i in range(n*n):
    if(i in dict3.keys()):
        l.append(dict3[i])
    else:
        l.append(0)
c=0
for i in range(n):
    for j in range(n):
        print(l[c], end=" ")
        c+=1
    print("")
