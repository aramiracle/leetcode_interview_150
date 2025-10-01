class Solution(object):
    def summaryRanges(self, nums):
        """
        Summarize a sorted list of unique integers into ranges.

        Args:
            nums (List[int]): A sorted list of unique integers.

        Returns:
            List[str]: A list of strings representing the ranges of consecutive 
            numbers in `nums`. Each element is either a single number (as a string) 
            or a range in the format "start->end".
        """
        if not nums:
            return []
        
        r = [nums[0], nums[0]]
        ranges = []
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 1:
                r[1] = nums[i]
            else:
                ranges.append(str(r[0])) if r[0] == r[1] else ranges.append(str(r[0]) + "->" + str(r[1]))
                r = [nums[i], nums[i]]

        ranges.append(str(r[0])) if r[0] == r[1] else ranges.append(str(r[0]) + "->" + str(r[1]))

        return ranges
