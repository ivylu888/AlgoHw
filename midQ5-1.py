def findSame(arr, vals):
  j = 0
  index = []
  
  for i in range(len(arr)):
    if arr[i] == vals[j]:
      index.append(i)
      j += 1
    elif arr[i] != vals[j]:
      index.append(-1)'
      j += 1
  retuen index
