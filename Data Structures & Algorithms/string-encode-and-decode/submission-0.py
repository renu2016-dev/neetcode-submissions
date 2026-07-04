class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        # encode their lengths in 3 digits each, pad to 200 chars
        for string in strs:
            l = len(string)
            temp += str(l).zfill(3)+string.zfill(200)
        return temp


    def decode(self, s: str) -> List[str]:
        ans = []
        print(s)
        for i in range(0,len(s),203):
            l = int(s[i:i+3])
            print(l)
            ans.append(s[i+203-l:i+203])
            # l = int(s[200+3:200+3+3])
            # ans.append(s[200+3+3:200+3+3+l])

        return ans
