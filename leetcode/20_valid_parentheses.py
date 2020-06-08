class Solution:
    def isValid(self, s: str) -> bool:
        # go through, add parens to stack, if close paren matches last open paren pop off, if theres a mismatch or things still in the stack 
        paren_stack = []
        if len(s) % 2 == 1:         # odd means there's one without a match; can auto reject
            return False
        
        parens = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for char in s:                      
            if char in ')]}':
                if len(paren_stack) == 0:
                    return False
                elif paren_stack[-1] == parens[char]:
                    paren_stack.pop()
                else:
                    return False
            else:
                paren_stack.append(char)
        
        if len(paren_stack) > 0:
            return False
        else:
            return True
                    