# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        if len(a) > len(b):
            diff = len(a) - len(b)
            for i in range(diff):
                b = "0" + b
        if len(a) < len(b):
            diff = len(b) - len(a)
            for i in range(diff):
                a = "0" + a
        carry = 0
        ans = ""
        for i in range(len(a) - 1, -1, -1):
            if a[i] == '0' and b[i] == '0' and carry == 0:
                ans = "0" + ans
            elif a[i] == '0' and b[i] == '0' and carry == 1:
                ans = "1" + ans
                carry = 0
            elif a[i] == '0' and b[i] == '1' and carry == 1:
                ans = "0" + ans
                carry = 1
            elif a[i] == '1' and b[i] == '0' and carry == 1:
                ans = "0" + ans
                carry = 1
            elif a[i] == '1' and b[i] == '0' and carry == 0:
                ans = "1" + ans
                carry = 0
            elif a[i] == '1' and b[i] == '1' and carry == 1:
                ans = "1" + ans
                carry = 1
            elif a[i] == '1' and b[i] == '1' and carry == 0:
                ans = "0" + ans
                carry = 1
            elif a[i] == '0' and b[i] == '1' and carry == 0:
                ans = "1" + ans
                carry = 0
        if carry == 1:
            ans = "1" + ans
        return ans