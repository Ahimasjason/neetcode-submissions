class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        obj = []
        for i in range(len(position)):
            obj.append((position[i], speed[i], (target - position[i]) / speed[i]))
        
        obj.sort(key=lambda x : x[0], reverse=True)


        stack = []

        for item in obj:
            pos, speed, time = item
            if not stack:
                stack.append((pos, time))
            else:
                if time > stack[-1][1]:
                    stack.append((pos, time))
                
                    
        return len(stack)

        