S=str(input())
while True:
  if(S.endswith("dream")):
    S=S[:-5]
  elif(S.endswith("dreamer")):
    S=S[:-7]
  elif(S.endswith("erase")):
    S=S[:-5]
  elif(S.endswith("eraser")):
    S=S[:-6]
  else:
      break
if(S==""):
  print("YES")
else:
  print("NO")
