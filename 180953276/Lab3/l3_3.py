def locvar():
    global b
    b = 112
    a = 20
    st = 'AdvancedProgrammingLab'
print('No of local variables are: ',locvar.__code__ .co_nlocals)  
