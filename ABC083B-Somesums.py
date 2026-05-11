N,A,B=map(int,input().split())
ans=0
for i in range(1,N+1):
  def digin_sum(j):
    return sum(map(int,str(j)))
  x=digin_sum(i)
  if(A<=x<=B):
    ans+=i
print(ans)
