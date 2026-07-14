class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            k = "".join(sorted(list(word)))
            if k not in hash_map:
                hash_map[k] = [word]
            else:
                hash_map[k].append(word)
        return hash_map.values()