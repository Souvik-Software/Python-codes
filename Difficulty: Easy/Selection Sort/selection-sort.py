class Solution: 
    def selectionSort(self, nums):
        for i in range(len(nums)):
            minindex=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minindex]:
                    minindex=j
            nums[minindex],nums[i]=nums[i] , nums[minindex]