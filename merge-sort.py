def merge(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j) = ([], 0, 0)

    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < m:
        C.append(A[i])
        i += 1

    while j < n:
        C.append(B[j])
        j += 1

    return C

def mergesort(L):
    n = len(L)
    if n <= 1:
        return L
    left_half = mergesort(L[:n//2])
    right_half = mergesort(L[n//2:])
    sorted_merged_list = merge(left_half, right_half)
    return sorted_merged_list
  
input = [5, 2, 8, 12, 3, 1]
sorted_list = mergesort(input)
print(sorted_list)

