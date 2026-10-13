class MinStack:

    def __init__(self):
        self.__stack = list()
        self.__min = list()

    def push(self, val: int) -> None:
        
        if not self.__min:
            self.__min.append([val,1])
        else:
            if self.__min[-1][0] == val:
                self.__min[-1][1]+= 1
            elif val < self.__min[-1][0]:
                self.__min.append([val, 1])
        self.__stack.append(val) 
        return None


    def pop(self) -> None:

        if not self.__stack: return None

        rv = self.__stack.pop()

        if self.__min[-1][0] == rv:
            self.__min[-1][1] -= 1
            if self.__min[-1][1] == 0:
                self.__min.pop()

        return None
        

    def top(self) -> int:
        return self.__stack[-1]
        

    def getMin(self) -> int:
        return self.__min[-1][0]
