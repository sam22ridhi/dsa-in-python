def binarysearch(L,v):
  low=0
  high=len(L)-1
  while low<=high:
    mid=(low+high)//2
    if L[mid]<v:
      low=mid+1
    elif L[mid]>v:
      high=mid-1
    else:
      return mid
  return False
L = [1,3,4,5,6,8]
v = 6
print(binarysearch(L,v))
