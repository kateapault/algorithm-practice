class Solution:
    # this is a fucking O(n^2) travesty and I am not at all proud of it
    # but I don't know how to do it more efficiently and I had a lot of 
    # other shit to do today so, you know, here's *a* solution.
    def largestTimeFromDigits(self, A: List[int]) -> str:
        time = ""
        A.sort()
        if A[0] > 2:
            return ""
        elif A[1] > 5:
            return ""
        elif A == [0,0,0,0]:
            return "00:00"
        else:
            h = []
            for i in range(0,len(A)-1):
                for j in range(i+1,len(A)):
                    h.append(A[i]*10+A[j])
                    h.append(A[j]*10+A[i])
            print(h)
            mx = [0,0]        
            for i in range(0,len(h)):
                c = []
                for n in A:
                    c.append(n)
                if h[i] < 24 and h[i] >= mx[0]:
                    x = h[i] // 10
                    y = h[i] % 10
                    c.remove(x)
                    c.remove(y)
                    a = c[0] * 10 + c[1]
                    b = c[1] * 10 + c[0]
                    if h[i] == mx[0]:
                        if max(a,b) < 60 and max(a,b) > mx[1]:
                            mx = [h[i],max(a,b)]
                        elif min(a,b) < 60 and min(a,b) > mx[1]:
                            mx = [h[i],min(a,b)]
                    else:
                        if max(a,b) < 60:
                            mx = [h[i],max(a,b)]
                        elif min(a,b) < 60:
                            mx = [h[i],min(a,b)]
            
            if mx == [0,0]:
                return ""
            else:
                if mx[0] < 10:
                    time += f"0{mx[0]}"
                else:
                    time += f"{mx[0]}"
                if mx[1] < 10:
                    time += f":0{mx[1]}"
                else:
                    time += f":{mx[1]}"
                    
                return time
            