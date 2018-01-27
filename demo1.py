import time

print(time.localtime(time.time()))
f = open('scores.csv', 'r')

list1 = f.readlines()
for i in range(0, len(list1)):
    list1[i] = list1[i].rstrip('\n')
    if i%1000000==0:
        tmp = open('scores'+str(i)+'.cvs','w')
        if i!=0:
            tmp.writelines(list1[0] + '\n')
    tmp.writelines(list1[i]+'\n')
print(time.localtime(time.time()))