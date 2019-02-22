class Solution:
    def twoSum1(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return i, j
                else:
                    j += 1
        return

    def twoSum2(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        r ={}
        for x in range(len(nums)):
            n = target - nums[x]
            if n in r:
                return [r[n], x]
            r[nums[x]] = x

    def twoSum3(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        r = {}
        for i, num in enumerate(nums):
            if target-num in r:
                return r[target-num], i
            r[num] = i



if __name__ == "__main__":
    ll = [1,6,8,9,5,34]
    sol = Solution()
    print(sol.twoSum2(ll, 10))
