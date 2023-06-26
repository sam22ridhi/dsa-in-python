#Using Numpy 2D Array
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] # each tuple(u,v) represent edge from u to v
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1 # mark 1 if edge present in graph from i to j , otherwise 0
print(AMat)

#Using Python nested list
V = [0,1,2,3,4]
E = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,3), (3,4)]
size = len(V)
AMat = []
for i in range(size): #iterates over range 0 to size - 1
  row = []
  for j in range(size):
    row.append(0)
  AMat.append(row.copy())
for (i,j) in E:
  AMat[i][j] = 1 # mark 1 if edge present in graph from i to j
print(AMat)

#Using Python dictionary
V = [0,1,2,3,4]
E = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,3), (3,4)]
size = len(V)
AList = {}
# In the dictionary AList, for example, AList[i] = [j,k] represents two edges from i to j and i to k
for i in range(size):
  AList[i] = []

for (i,j) in E:
  # Append the destination vertex j to list associated with source vertex i in AList
  AList[i].append(j)

print(AList)
