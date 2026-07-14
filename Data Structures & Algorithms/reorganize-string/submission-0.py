from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # create a hash map of count and character for s 
        count = Counter(s)
        # Create a list of char and frequency that we can heapify
        # use negative sign as python implement minHeap so largest
        # frequency char will come at top with negative sign
        maxHeap = [[-cnt, char] for char, cnt in count.items() ]
        #heapify
        heapq.heapify(maxHeap)

        # Store previous character when they are still 
        # remaining but can't be kept at top of heap
        prev = None
        # Store the reorganized string in res variable
        res = ''

        # Looping until prev or maxHeap is not empty
        while maxHeap or prev:
            if prev and not maxHeap: # case when we don't have any other character to place except repeating the prev one
                return ''
            # Get the most frequent character from string
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                # if we have previous variable non-empty, that mean
                # there is a frequent character that needed to be pushed back to heap
                # to get processed in next iteration
                heapq.heappush(maxHeap, prev)
                prev = None # Reset 
            
            if cnt != 0:
                # frequent character not done yet but had to wait for another character
                # to not repeat in next iteration
                prev = [cnt, char]
        return res
        