class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempN = dict()
        
        for i,num in enumerate(nums):
            if num in tempN:
                # print(num)
                # print(tempN[num])
                tempN[num].append(i)
                # tempN[num] = x
            else:
                tempN[num] = [i]
        print(tempN)
        for i, num in enumerate(nums)    :
            target_num = target-num
            # tempN[num] = tempN[num].remove(i)
            if target_num in tempN:
                # print(tempN)
                for j in tempN[target_num]:
                    if i!=j:
                        return [i,j]
        
                         