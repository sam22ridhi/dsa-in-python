
def selectionsort(L):
  n=len(L)
  if n<1:
    return(L)
  for i in range(n):
    minpos=i
    for j in range(i+1,n):
      if L[j]<=L[minpos]:
        minpos=j
    (L[i],L[minpos])=(L[minpos],L[i])
  return(L)
L= [4,5,2,1,3]
print(selectionsort(L))
