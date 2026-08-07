class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[1]*len(nums)
        rs=[1]*len(nums)
        f=[1]*len(nums)

        for i in range(1,len(nums)):
            ls[i]=nums[i-1]*ls[i-1]
           

        for j in range(len(nums)-2,-1,-1):
            rs[j]= nums[j+1]* rs[j+1]

        for k in range(0,len(nums)):
            f[k]= ls[k] * rs[k]
        return f 

        