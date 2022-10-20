class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        stack = []
        for i in range(1, 10):
            stack.append((str(i), 1))
            
        res = set()
        
        while stack:
            num, length = stack.pop()
            if length == n:
                res.add(num)
            s = int(num[-1])
            if length < n:
                if s + k < 10:
                    stack.append((num + str(s+k), length + 1))
                if s - k >= 0:
                    stack.append(((num + str(s-k), length + 1)))
                
        return [int(x) for x in res]


