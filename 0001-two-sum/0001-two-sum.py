class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict={}
        for i in range(0,len(nums)):
            remaining=target-nums[i]
            if remaining in my_dict:
                return [i,my_dict[remaining]]
            else:
                my_dict[nums[i]]=i