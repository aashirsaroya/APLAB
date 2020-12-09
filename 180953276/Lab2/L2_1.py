str = input('Enter a sentence')
words = []
words = str.split()
dct = {}
ctr = 0
for i in words:
    dct[i] = words.count(i)
    ctr = ctr + 1
print(dct)
print('Total words in the sentence is ',ctr)
