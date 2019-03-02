class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return len(nums)

        count = 0
        prev = None
        for num in nums:
            if num != prev:
                prev = num
                nums[count] = num
                count += 1
        return count

    def removeDuplicates2(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)

    def removeDuplicates3(self, nums: List[int]) -> int:
        count = 0
        curt_num = None
        idx = -1
        for num in nums:
            if num != curt_num:
                curt_num = num
                idx += 1
                nums[idx] = num
                count += 1
        nums = nums[0:count]
        return count


if __name__ == "__main__":
    l1 = [1,2,2,3,3,4, 4]
    m = Solution()
    print(m.removeDuplicates(l1))