list = []
evenlist=[]
n = int(input('Enter  n : '))

for i in range(0,n):
    list.append(int(input('Enter number : ')))

for i in list:
    if (i%2 == 0):
        evenlist.append(i)
print(evenlist)
