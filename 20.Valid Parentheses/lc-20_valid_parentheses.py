class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Write your solution here
        stk = []
        for i in s:
            if i == "}":
                if not stk or stk[-1] != "{":
                    return False
                stk.pop()
            elif i == "]":
                if not stk or stk[-1] != "[":
                    return False
                stk.pop()
            elif i == ")":
                if not stk or stk[-1] != "(":
                    return False
                stk.pop()
            else:
                stk.append(i)
        return len(stk) == 0



# ---------- Test Code ----------
if __name__ == "__main__":
    s = "()"

    sol = Solution()
    result = sol.isValid(s)

    print("Input:", s)
    print("Output:", result)
