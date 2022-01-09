
#_______________counting alphabets using functions in a string_______________

print('__________count the alphabets on your string________')

a=input('Please enter a string: ').lower()

def most_frequent(a):
    d1=dict()
    for i in a:

        if i not in d1:
            d1[i]=1
        else:

            d1[i]=d1[i]+1
    return d1
    
print(most_frequent(a))
