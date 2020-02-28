def last2(str):
  a = list(str)
  count = 0
  for i in range(len(a)):
    if i > 1:
      if a[i] == a[i+1] and a[i-1] != a[i]:
        if a[i] == a[-1] and a[i] == a[-2]:
          if a[i+1] == a[-1] and a[i+1] == a[-2]:
            count = count+1
        else: 
          continue
      else:
        continue
    elif i == 1
  return count
        
print(last2("xxdjhdjhdjhdjhxx"))