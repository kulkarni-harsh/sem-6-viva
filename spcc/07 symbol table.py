# Generate Symbol Table
# Enter commands separated by comma

code=[
    ' ,START,200, ',
    ' ,MOVER,AREG,DATA',
    ' ,ADD,AREG,BREG',
    'DATA,DC,5, ',
    'ST,DC,10, ',
    ' ,END, , '
    ]

symbolTable=[['Sym','Add','Len']]

lc = 69     # (˘ ͜ʖ˘) nice
for line in code:
    cmd=line.split(',')

    if cmd[1]=='START':
        lc=int(cmd[2])

    elif cmd[3][0]!='='and cmd[3]!=' 'and "REG"not in cmd[3]:
        if cmd[3] not in [z[0]for z in symbolTable]:
            symbolTable+=[[cmd[3],'-',1]]

    elif cmd[0]!=' ':
        if cmd[0] in [z[0]for z in symbolTable]:
            symbolTable[[z[0]for z in symbolTable].index(cmd[0])][1]=lc
            lc+=1
        
        else:
            symbolTable+=[[cmd[0],lc,1]]

        
        continue


    lc+=1

for i in symbolTable:
    print(*i,sep=' ')






