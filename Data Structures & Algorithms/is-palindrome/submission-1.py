class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        text = re.sub(r'[^a-zA-Z0-9]','',s)

        for i in range(int(len(text)/2)):
            if text[i].lower() != text[-i-1].lower():
                return False
        return True
        