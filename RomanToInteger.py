#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Hash Table Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                total= total - roman[s[i]]
            else:
                total= total + roman[s[i]]
        return total+roman[s[-1]]
    
#Conditional solution 
class Solution:
    def romanToInt(self, s: str) -> int:
        flag = 0
        t=0
        for i in range(0,len(s)):
            if flag == 1:
                flag=0
                continue
            flag=0
            if s[i] == "I":
                if i != len(s)-1:
                    if s[i+1] == "V":
                        flag=1
                        t = t + 4
                    elif s[i+1] == "X":
                        flag=1
                        t = t + 9
                    else:
                        t = t + 1
                else:
                    t = t + 1
            if s[i] == "V":
                t = t + 5
            if s[i] == "X":
                if i != len(s)-1:
                    if s[i+1] == "L":
                        flag=1
                        t = t + 40
                    elif s[i+1] == "C":
                        flag=1
                        t = t + 90
                    else:
                        t = t + 10
                else:
                    t=t+10
            if s[i] == "L":
                t = t + 50
            if s[i] == "C":
                if i != len(s)-1:
                    if s[i+1] == "D":
                        flag=1
                        t = t + 400
                    elif s[i+1] == "M":
                        flag=1
                        t = t + 900
                    else:
                        t = t + 100
                else:
                    t=t+100
            if s[i] == "D":
                t = t + 500
            if s[i] == "M":
                t = t + 1000
            print(t)
        return t