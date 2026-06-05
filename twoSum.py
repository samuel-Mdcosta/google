class Solution:
    def twoSum(self, nums:List[int], target) -> lint[int]:
        seen = {}

        for i, num in enumerate(nums):
            summ = target - num
            if summ in seen:
                return [seen[summ], i]
            seen[num] = i
        return []