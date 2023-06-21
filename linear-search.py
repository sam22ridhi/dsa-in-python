def linearsearch(L,v):
  for i in range(len(L)):
    if v==L[i]:
      print('Element at pos' ,i+1)
  return(False)
L = [1,3,4,5,6,8]
v = 6
print(linearsearch(L,v))
