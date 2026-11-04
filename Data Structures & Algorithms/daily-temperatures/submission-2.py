class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack = []
        # rv = [0 for _ in range(len(temperatures))]

        # for i in range(len(temperatures) -1, -1 , -1):
        #     while stack and stack[-1][0] <= temperatures[i] :
        #         stack.pop()

        #     if stack:
        #         if stack[-1][0] > temperatures[i]:
        #             rv[i] = stack[-1][1] - i
        #         stack.append((temperatures[i],i)) 
        #     else:
        #         stack.append((temperatures[i],i))
        #         rv[i] = stack[-1][1] - i



        rv = [0 for _ in range(len(temperatures))]

        for temp_i in range(len(temperatures) -1,-1,-1):
            temp = temperatures[temp_i]
            while stack and stack[-1][1] <= temp:
                stack.pop()
            if stack:
                if stack[-1][1] > temp:
                    rv[temp_i] = stack[-1][0] - temp_i
                stack.append((temp_i, temp))
            else:
                stack.append((temp_i, temp))
                rv[temp_i] = stack[-1][0] - temp_i
        return rv
