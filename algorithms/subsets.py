import copy


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
