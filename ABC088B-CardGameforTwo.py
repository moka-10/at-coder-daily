N=int(input())
a=list(map(int,input().split()))
s=0
ans=0
score_A=0
score_B=0
for i in range(N):
  if (i%2==0):
    score_A+=a.pop(a.index(max(a)))
  else:
    score_B+=a.pop(a.index(max(a)))
print(score_A-score_B)
    
