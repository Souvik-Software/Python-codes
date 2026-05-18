class Solution:
    def findMin(self, nums: List[int]) -> int:
        m=0
        n=len(nums)-1
        while m<n:
            mid=(m+n)//2
            if nums[mid]>nums[n]:
                m=mid+1
            else:
                n=mid
        return nums[m]
        