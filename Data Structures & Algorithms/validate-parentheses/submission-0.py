class Solution:
    def isValid(self, s: str) -> bool:
        # Solve this by stack data structure
        # stack ds will store open bracket
        stacked = []
        closeToOpen = {']':'[', ')':'(', '}':'{'} # mapping to open when
        # close bracket comes in

        for char in s:
            if char in closeToOpen:
                # if stack is non-empty and last element is
                # the same type of opening bracket
                if stacked and stacked[-1] == closeToOpen[char]: 
                    stacked.pop()
                else: # Means char is open bracket
                    return False # not same type of bracket
            else:
                stacked.append(char)
        return True if not stacked else False ## If stack contains open bracket
        # that are not closed then not a valid string