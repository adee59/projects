
#_____________printing all posiitive no. in the range_______________

m=int(input('enter no.of terms: '))
print('Enter ',m ,' terms below:')

l1=[]
l2=[]

print("Enter one term then press 'ENTER' to input another term.")
for i in range(0,m):
    no=float(input('Enter the terms here: '))
    l1.append(no)

print('The entered range is: ',l1)

for i in range(0,m):
    
    a=l1[i]
    if a>0:
        l2.append(a)
    
print('Positive no.s in the gven range are: ',l2)    
    
