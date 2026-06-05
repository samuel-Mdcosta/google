class Solution:
    def topK(self, nums:List[int], k:int) -> List[int]:
        count - Counter(nums)
        res = [[] for i in range(len(nums)+ 1)]

        for num, freq in count.items():
            res[fre].append(num)

        answer = []
        
        for freq in range(len(res) -1, 0 ,-1):
            for num in res[freq]:
                answer.append(num)
                if len(answer) == k:
                    return answer