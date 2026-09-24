class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Write your solution here
        hashmap = {")":"(", "}":"{","]":"["}
        stk = []
        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    poped = stk.pop()
                    if poped != hashmap[c]:
                        return False
        return not stk
# ---------- Test Code ----------
if __name__ == "__main__":
    s = "([{}])"

    sol = Solution()
    result = sol.isValid(s)

    print("Input:", s)
    print("Output:", result)
