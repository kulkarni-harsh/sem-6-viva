st=input('Enter String:')
print(st)
if st[0]=='_' or st[0].isalpha():
    if '_' in st:
        st1= st.replace('_','')
        if st1.isalnum():
            print('YES')
        else:
            print('NO')
    elif st.isalnum():
            print('YES')
    else:
        print('NO')
else:
    print('NO')
