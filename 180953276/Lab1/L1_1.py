lst1 = []
n1 = int(input('Enter the no of elements in list 1'))
for i in range(0,n1):
    ele = int(input('Enter a no'))
    lst1.append(ele)
lst2 = []
n2 = int(input('Enter the no of elements in list 2'))
for i in range(0,n2):
    ele = int(input('Enter a no'))
    lst2.append(ele)
ans = []
for i in lst1:
    if i % 2 != 0:
        ans.append(i)
for i in lst2:
    if i % 2 == 0:
        ans.append(i)
print(ans)        
