class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        premul = 1
        premulmat = [1]
        for num in nums:
            premul *= num
            premulmat.append(premul)
        postmul = 1
        postmulmat = [1]
        for num in reversed(nums):
            postmul *= num 
            postmulmat.append(postmul)
        # print(premulmat, postmulmat)

        return [premulmat[i]*postmulmat[-i-2] for i in range(len(nums))]