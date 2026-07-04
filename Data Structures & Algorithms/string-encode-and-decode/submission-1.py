class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""

        for string in strs:
            l = len(string)
            temp += str(l).zfill(3)+string.zfill(200)
        return temp


    def decode(self, s: str) -> List[str]:
        ans = []
        for i in range(0,len(s),203):
            l = int(s[i:i+3])
            print(l)
            ans.append(s[i+203-l:i+203])

        return ans
