class Solution:
    def isPalindrome(self, s):
        # code here
        ans= s[::-1]
        if ans==s:
            return True
        else:
            return False
        
