class Solution:
    def removeElement(self, nums, val):
        """
        """
        k = 0
        for element in nums:
            if element != val:
                nums[k] = element
                k += 1
        return k