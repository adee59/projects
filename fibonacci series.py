
#______________project : 2 {fibonacci series}________________

print('___________Generating Fibonacci Series With Desired No. Of Terms__________')

a=int(input('Enter the required no. of terms: '))

t1=0
t2=1

tn=0
bello=0

if a<=0:
    print('Please enter a positive no.')
elif a==1:
    print('The fibonacci series with 1 term is: 0')
else:
    print('Fibonacci series with ',a ,'terms is as follows:')
    while bello<a:
        print(t1)
        tn= t1+t2
        t1=t2
        t2=tn
        bello=bello+1

    print('Series has been generated.')
