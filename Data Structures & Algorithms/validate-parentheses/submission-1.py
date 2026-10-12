class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ("}", "]", ")"):
                if not stack:
                    return False
                item = stack.pop()
                if i == "}":
                    if item != "{":
                        return False
                elif i == "]":
                    if item != "[":return False
                elif i == ")":
                    if item != "(":return False
            else:
                stack.append(i)
        return True and not stack