OrgN = int(input())
N=OrgN
count=0
true=1
while true:
    Fst = int(N/10)
    Sec = int(N%10)
    if Fst==0:
        N = N*11
    else :
        Sum_result = Fst + Sec
        N = Sec*10+Sum_result%10

    count +=1
    if OrgN==N:
        true=0

print(count)
