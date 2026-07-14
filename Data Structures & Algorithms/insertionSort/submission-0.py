# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        right = 0
        
        output = []
        while right < len(pairs):
            
            left = right - 1
            while (left >= 0) and (pairs[left].key > pairs[left + 1].key):
                pairs[left], pairs[left+1] = pairs[left+1], pairs[left]
                left -= 1
            
            output.append(pairs[:])
            right += 1
        return output
        