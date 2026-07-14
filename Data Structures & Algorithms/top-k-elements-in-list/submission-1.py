class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for n in nums:
            if n not in count_dict:
                count_dict[n] = 1
            else:
                count_dict[n] += 1
        # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        output = [k for k, v in sorted(count_dict.items(), key = lambda x : x[1], reverse=True)][0:k]
        return output
        