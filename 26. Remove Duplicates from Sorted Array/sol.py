class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j

"""
nums = [0,0,1,1,1,2,2,3,3,4]
use two pointers
we start both indices at 1. 

if 'i' is not equal to 'i' before it, we assign 'i' to 'j', so as to replace
the element with element after it. then, we increment 'j' by one, becuase 'j' is moved to next element

we do not add any condition for 'i' and its previous 'i' being equal
"""