N=int(input())
d=[]
for x in range(N):
  d.append(int(input()))
d.sort(reverse=True)
count=0
s=10000
for i in d:
  if(i<s):
    s=i
    count+=1
print(count)
