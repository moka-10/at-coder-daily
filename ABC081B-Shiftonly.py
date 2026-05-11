N=int(input())
A=list(map(int,input().split()))
ans=10**9
for i in A:
  count=0
  while(i%2==0):
    i//=2
    count+=1
  ans=min(ans,count)
print(ans)
  
