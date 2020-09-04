class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # get first and last ind for each letter that appears
        # then figure out which are overlapping
        letters = {}
        for i in range(0,len(S)):
            if S[i] in letters:
                letters[S[i]]['last'] = i
                letters[S[i]]['count'] += 1
            else:
                letters[S[i]] = {'first':i,'last':i, 'count':1}
        print(letters)
        
        parts = []
        for let in letters.keys():
            i = letters[let]['first']
            j = letters[let]['last']
            if len(parts) < 1:
                parts.append([i,j])
            else:
                for k in range(0,len(parts)):
                    sec = parts[k]
                    if i >= sec[0] and i <= sec[1]:
                        if j > sec[1]:
                            parts[k] = [sec[0],j]
                    elif j >= sec[0] and j <= sec[1]:
                        if i < sec[0]:
                            parts[k] = [i,sec[1]]
                    elif j < sec[0]:
                        shift = parts[k:]
                        parts[k] = [i,j]
                        parts = parts[:k+1] + shift
                    elif k == len(parts) - 1 and i > sec[1]:
                        parts.append([i,j])
        print(parts)
        x = []
        for part in parts:
            x.append(part[1]-part[0] + 1)
        return x