i,j = map(int,input().split())
strlist = input().split()
list1 = list(map(int,strlist))
strlist = input().split()
list2 = list(map(int,strlist))
list3 = sorted(list1+list2)
for count in range(0,i+j):
    print(int(list3[count]),end=' ')
