class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        nums.sort()
        ind = []
        cur = 0
        for i, num in enumerate(nums):
            if val == num:
                ind.append(i)
                cur += 1
            else:
                cur += 1
        if not ind:
            return len(nums)
        else:
            nums = nums[:ind[0]] + nums[ind[-1] + 1:]
            print(nums)
            return len(nums)

    def removeElement2(self, nums, val):
        if not nums:
            return 0
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
        return l

    def removeElement3(self, nums: List[int], val: int) -> int:
        l = len(nums)
        i = 0
        while i < l:
            #print(i,nums)
            if nums[i] == val:
                del nums[i]
                l = len(nums)
            else:
                i += 1
        return len(nums)


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    m = Solution()
    print(m.removeElement(nums, 2))