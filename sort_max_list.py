#arrangeindescending
n=int(input())
li=list(map(int,input().split()))
li1=sorted(li)
s=li1[::-1]
k=''
for i in range(len(s)):
    k=k+str(s[i])+''
print(k)
