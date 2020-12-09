lst = []
ctr = 0
n = int(input('Enter the number of strings'))
for i in range(0,n):
    str = input('Enter a string')
    lst.append(str)
for st in lst:
    if st[0] == st[-1] and len(st) > 1:
        ctr = ctr + 1
print('No of strings with samr 1st & last letters and having len 2 or more: ',ctr)
print('Strings having odd length are as follows')
for st in lst:
    if len(st)%2 !=0:
        print(st)
