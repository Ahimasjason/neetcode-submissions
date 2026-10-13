class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        rv = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures) -1, -1 , -1):
            while stack and stack[-1][0] <= temperatures[i] :
                stack.pop()

            if stack:
                if stack[-1][0] > temperatures[i]:
                    rv[i] = stack[-1][1] - i
                stack.append((temperatures[i],i)) 
            else:
                stack.append((temperatures[i],i))
                rv[i] = stack[-1][1] - i

        return rv
