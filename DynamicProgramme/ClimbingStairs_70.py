"""
https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:

    @staticmethod
    def climb_stairs_v1(n: int) -> int:
        """
        采用回溯法，穷举所有的可能性
        时间复杂度:O(2**n)
        空间复杂度:O(n)
        :param n:
        :return:
        """

        def climb(n: int):
            if n == 0:
                return 1
            if n == -1:
                return 0
            return climb(n - 1) + climb(n - 2)

        return climb(n)

    @staticmethod
    def climb_stairs_v2(n: int) -> int:
        """
        采用回溯法，进行剪枝:
        通过一个字典存储n对应的可能性，如果n在字典中，则直接返回，如果n不在，计算结果后，再记录在字典中
        时间复杂度:O(n)
        空间复杂度:O(n)
        :param n:
        :return:
        """
        history = {}

        def climb(n: int):
            if n == 0:
                return 1
            if n == -1:
                return 0

            if n not in history:
                history[n] = climb(n - 1) + climb(n - 2)
            return history[n]

        climb(n)
        return climb(n)

    @staticmethod
    def climb_stairs_v3(n: int) -> int:
        """
        dp[i]=dp[i-1]+dp[i-2]
        时间复杂度:O(n)
        空间复杂度:O(n)
        :param n:
        :return:
        """
        history = {
            0: 0,
            1: 1,
            2: 2
        }
        for i in range(3, n + 1):
            history[i] = history[i - 1] + history[i - 2]

        return history[n]

    @staticmethod
    def climb_stairs_v4(n: int) -> int:
        """
        dp[i]=dp[i-1]+dp[i-2]计算和斐波拉契数列相同，因此可以利用数学公式进行计算
        时间复杂度:O(n)
        空间复杂度:O(1)
        :param n:
        :return:
        """
        if n in [0, 1, 2]:
            return n
        first = 1
        second = 2
        for i in range(3, n + 1):
            second, first = first + second, second
        return second


def test():
    assert Solution.climb_stairs_v1(3) == 3
    assert Solution.climb_stairs_v2(5) == 8
    assert Solution.climb_stairs_v3(5) == 8
    assert Solution.climb_stairs_v4(5) == 8


if __name__ == '__main__':
    test()
