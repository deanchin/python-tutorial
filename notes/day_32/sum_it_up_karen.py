class Solution:
    def runningSum(self, nums: []):
        out_list = []

        for i in nums:
            if out_list == []:
                out_list.append(i)
            else:
                out_list.append(i + out_list[len(out_list) - 1])
        return out_list

print(Solution().runningSum(nums=[1,1,1,1]))