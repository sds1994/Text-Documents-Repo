n = int(input('Enter n : '))

i=j=1

for i in range(1,n+1):
    if(i%3 == 0 and i%5 != 0):
        print('FIZZ')
    elif(i%5 == 0 and i%3 != 0):
        print('BUZZ')
    elif(i%3 == 0 and i%5 == 0):
        print('FIZZBUZZ')
    else:
        print('*'*i)
