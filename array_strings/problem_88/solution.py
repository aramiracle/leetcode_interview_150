class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge two sorted arrays into the first array in-place.

        Args:

            nums1: A list of integers with length m + n. The first m elements are valid numbers in non-decreasing order. The rest of the list (last n elements) can be ignored.
            m: Number of valid elements in nums1.
            nums2: A list of n integers in non-decreasing order.
            n: Number of elements in nums2.

        Returns:
            None. Modifies nums1 in-place to contain the merged sorted array.
        """
        merged = []  # temporary array
        p1, p2 = 0, 0  # pointers for nums1 and nums2

        # Compare and append
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        # Append remaining elements
        while p1 < m:
            merged.append(nums1[p1])
            p1 += 1
        while p2 < n:
            merged.append(nums2[p2])
            p2 += 1

        # Copy merged array back to nums1
        for idx in range(m + n):
            nums1[idx] = merged[idx]