str=input("Enter String ")
if "bab" in str:
    print('Yes')
else:
    print('No')
#recognize the lanuage of string with substring bab
state=0
for i in range(0,len(str)):
    if str[i]=='b':
        if str[i-1]=='a':
           if str[i-2]=='b':
                state=1
        
if state==1:
    print('Yes1')
else:
    print('No1')