N=int(input())
pt=0
px=0
py=0

for _ in range(N):
  t,x,y=map(int,input().split())
  dist=abs(x-px)+abs(y-py)
  dt=t-pt
  
  if(dist>dt or (dt-dist)%2!=0):
    print("NO")
    exit()
    
  pt=t
  px=x
  py=y
print("YES")
