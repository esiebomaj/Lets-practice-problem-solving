class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        res = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        freqArr = [[] for i in range(len(nums))]

        for n, f in freq.items():
            freqArr[f-1].append(n)

        while k > 0:
            curr = freqArr.pop()
            for i in curr:
                res.append(i)
                k -= 1

        return res


