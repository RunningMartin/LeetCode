from typing import List, Tuple

"""
https://leetcode-cn.com/problems/maximum-subarray/
"""


class Solution:
    @staticmethod
    def max_sub_array_v1(nums: List[int]) -> Tuple[int, List]:
        """
        依次遍历，统计所有子序列的和，然后找出最大值
        时间复杂度:O(n^2)
        空间复杂度:O(n^2)
        :param nums:
        :return: 最大子序列和，最大子序列
        """
        if not nums:
            return 0, []
        sub_arrays = list()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_arrays.append(nums[i:j + 1])

        max_sum = sum(sub_arrays[0])
        sub_array = sub_arrays[0]
        for array in sub_arrays:
            if sum(array) > sum(sub_array):
                max_sum = sum(array)
                sub_array = array

        return max_sum, sub_array

    @staticmethod
    def max_sub_array_v2(nums: List[int]) -> Tuple[int, List]:
        """
        V1版本中，计算子序列和时，可以采用如下策略剪枝：
        1、如果当前的子序列和<0，则不需要以当前子序列为基础往里添加新的元素
        2、只有当前子序列和大于0时，才可能让以它为基础的子序列和更大
        时间复杂度:O(n)
        空间复杂度:O(n)
        :param nums:
        :return: 最大子序列和，最大子序列
        """
        if not nums:
            return 0, []
        sub_arrays = list()
        array = []
        for num in nums:
            array.append(num)
            sub_arrays.append(array[:])

            if sum(array) < 0:
                array = []

        max_sum = sum(sub_arrays[0])
        sub_array = sub_arrays[0]
        for array in sub_arrays:
            if sum(array) > sum(sub_array):
                max_sum = sum(array)
                sub_array = array
        return max_sum, sub_array

    @staticmethod
    def max_sub_array_v3(nums: List[int]) -> int:
        """
        V2版本的空间复杂度为O(n),如果只需要最大序列和，则我们可以利用原序列，统计sum，将空间复杂度控制为O(1)
        时间复杂度:O(n)
        空间复杂度:O(1)
        :param nums:
        :return: 最大子序列和
        """
        if not nums:
            return 0

        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] >= 0:
                nums[i] = nums[i] + nums[i - 1]
            max_sum = max(max_sum, nums[i])
        return max_sum


def test():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert Solution.max_sub_array_v1(nums) == (6, [4, -1, 2, 1])
    assert Solution.max_sub_array_v2(nums) == (6, [4, -1, 2, 1])
    assert Solution.max_sub_array_v3(nums) == 6


if __name__ == '__main__':
    test()
