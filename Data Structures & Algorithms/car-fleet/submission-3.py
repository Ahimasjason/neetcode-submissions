class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

      
        pair = [ (i, (target - position[i]) / speed[i], position[i]) for i in range(len(position))]

        pair.sort(key = lambda x : x[2] , reverse = 1)
        
        stack = []
        for p in pair:
            
            pos, time, pos = p

            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)

        