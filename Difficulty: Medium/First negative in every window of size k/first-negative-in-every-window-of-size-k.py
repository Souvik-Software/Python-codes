from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        q = deque()
        result = []
        for i in range(len(arr)):
            if arr[i] < 0:
                q.append(i)
            while q and q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                if q:
                    result.append(arr[q[0]])
                else:
                    result.append(0)
        return result
        
