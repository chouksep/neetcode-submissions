class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Brute force: 
        
        checking every substring of s against t and returning minimum length valid substring (O(n2.m)) which is too slow for n, m <= 1000.

        Sliding window problem:
        2 pointers --> right pointer until the current window contains all characters of t --> Shrink the left pointer as much as possible while still having 
        a valid window (containing all of t)

        valid window: 
        2 freq dictionaries: countT - frequency of characters in t, window - freq of characters in the current window

        Track "have" (numbers of characters in window that meet or exceed the required count), "need" (total distinct characters in t), when have == need,
        the window is valid.
        """
        if t == "":
            return ""

        ## Use two pointers (l and r) to define a window in s
        ## Expand r to include characters until the window contains all characters of t (including duplicates)
        ## Then shrink l from the left as much as possible while still keeping the window valid, tracking the smallest such window.
    
        l,r = 0,0
        countT = {} # countT stores the required frequency of each character in t
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            
        have, need = 0, len(countT) #need is the number of distinct characters in t
        # have counts how many distinct characters have reached their required frequency (We only increment have when character's count in the window eactly matches its required count)
        window = {} # will store the current frequency of characters inside the window
        
        window_length = float("infinity")
        result = [0,0]
        
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] == countT[char]: # if the window completes required count for that character
                have += 1 #  increment have

            while have == need: #window is valid (all distinct char in t is in s and count of each distinct char in t is same as window)
                if (r-l+1) < window_length: # update window_length to find the min possible
                    result = [l, r] 
                    window_length = r - l + 1
                # Shrink left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1

     
        return s[result[0]: result[1]+1] if window_length != float("infinity") else ""