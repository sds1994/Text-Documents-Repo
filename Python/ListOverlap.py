import random
list1=[]
list2=[]
comman=[]

n1 = int(input('Enter size of list 1 : '))
lb1 = int(input('Enter Lower Boundary : '))
ub1 = int(input('Enter Upper Boundary : '))

n2 = int(input('Enter size of list 2 : '))
lb2 = int(input('Enter Lower Boundary : '))
ub2 = int(input('Enter Upper Boundary : '))

for i in range(0,n1):
    list1.append(random.randrange(lb1,ub1))
for i in range(0,n2):
    list2.append(random.randrange(lb2,ub2))

##if(n1>=n2):
##    for i in range(0,n1):
##        for j in range(0,n2):
##            if(list1[i]==list2[j] and list1[i] not in comman):
##                comman.append(list1[i])
##else:
##    for i in range(0,n2):
##        for j in range(0,n1):
##            if(list2[i]==list1[j] and list2[i] not in comman):
##                comman.append(list2[i])
for i in list1:
    if i in list2 and i not in comman:
        comman.append(i)


print('List 1 : '+str(list1))
print('List 2 : '+str(list2))
print('List of Comman Numbers : '+str(comman))








