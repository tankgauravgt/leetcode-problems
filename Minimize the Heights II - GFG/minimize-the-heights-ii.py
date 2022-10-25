#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        
        arr.sort()
        
        min_diff = max(arr) - min(arr)
        for ix in range(n - 1):
            if arr[ix + 1] < k:
                continue
            cmin = min(arr[0] + k, arr[ix + 1] - k)
            cmax = max(arr[n - 1] - k, arr[ix] + k)
            min_diff = min(min_diff, cmax - cmin)
        
        return min_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends