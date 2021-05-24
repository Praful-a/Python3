# Returns length of the longest substrring
# with all distinct characters.
def longestUniqueSubsttr(s):
     
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
 
# Driver code
if __name__ == '__main__':
     
    str1 = "abcabcba"
    print(longestUniqueSubsttr(str1))