class Solution:
    def product(self, nums:List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        sufix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= sufix
            sufix *= nums[i]
        return answer