import random
dct = {}
n = int(input('Enter no of values you are entering in the dictionary'))
for i in range(0,n):
    dct[random.randrange(0,100)] = input('Enter whatever you wish to')
print(dct)
avgn = 0
s = 0
st = ''
for key,value in dct.items():
    if(dct[key].isdigit()):
        dct[key] = int(value)
        s = s + dct[key]
        avgn = avgn + 1;
    else:
        st = st+dct[key]
     
avg = (float)(s/avgn)        
print('Average of all the numbers are ',avg)
print('All concatenated strings are: ',st)
v = input('Enter the value to be searced')
val = None
if v.isdigit():
    val = int(v)
else:
    val = v
f = 0    
for key, _ in dct.items():
    if dct[key] == val:
        print('Entered value is present and corresponding key is: ',key)
        f = 1
        break
if f == 0:
    print('Entered value not present') 
li = []
print('The strings with only special characters are as follows')
for key,value in dct.items():
           
       li = str(value)
       y = 1
       for i in range(0,len(li)):
           if(li[i].isalpha() or li[i].isdigit()):
               y = 0
               break
       if y == 1:
           print(value)
           


