class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_w_replacement = float('inf')
        # fixed sliding window problem
        b_count = 0
        l = 0
        for r in range(len(blocks)):
            if blocks[r] == "B":
                b_count += 1
            if (r-l+1) == k:
                curr_w_replacement = k - b_count
                min_w_replacement = min(curr_w_replacement, min_w_replacement)
                if blocks[l] == "B":
                    b_count -= 1
                l += 1


        return min_w_replacement