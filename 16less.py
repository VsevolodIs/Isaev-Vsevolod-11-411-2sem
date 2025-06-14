import time
import numpy as np

def FindMedianSortedArrays(A, B):
    if len(A) > len(B):
        A, B = B, A

    n, m= len(A), len(B)
    low, high = 0, n
    totalLeft = (n + m + 1) // 2

    while low <= high:
        i = (low + high) // 2
        j = totalLeft - i

        A_left = float('-inf') if i == 0 else A[i-1]
        A_right = float('inf') if i == n else A[i]

        B_left = float('-inf') if j == 0 else B[j-1]
        B_right = float('inf') if j == m else B[j]

        if A_left <= B_right and B_left <= A_right:
            if (n+m) % 2 == 1:
                return max(A_left, B_left)
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1

def measure_time(func, *args, repeats=10):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.perf_counter()
        result = func(*args) 
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return result, np.mean(times)      


nums1 = [1, 3]
nums2 = [2]

median, avg_time = measure_time(FindMedianSortedArrays, nums1, nums2, repeats=1000)
print(f"Медиана: {median}") 
print(f"Среднее время выполнения (1000 повторов): {avg_time:.8f} секунд")

nums1 = [1, 2]
nums2 = [3, 4]

median, avg_time = measure_time(FindMedianSortedArrays, nums1, nums2, repeats=1000)
print(f"Медиана: {median}")
print(f"Среднее время выполнения (1000 повторов): {avg_time:.8f} секунд")