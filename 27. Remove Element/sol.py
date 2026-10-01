class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


"""
nums = [3,2,2,3], val = 3
Trick

We use two pointers and partition algorithm.
'k' is set to 0 and 'i' is set to 0 and 'i' is incremented.

if 'i' is NOT EQUAL to given val, we replace 'k' by 'i', and incrememtn k, otherwise 
we do nothing

We return k normally

"""