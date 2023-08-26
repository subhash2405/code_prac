str1=input("enter first word:")
str2=input("enter second word:")
a=0
if(len(str1)!=len(str2)):
    print('False')
else:
    str1=''.join(sorted(str1))
    str2=''.join(sorted(str2))
    for i in range(len(str1)):
        if(str1[i]==str2[i]):
            a+=1
    if(a==len(str1)):
        print('True')
    else:
        print('False')
#there is a better method to do this
