from typing import List

"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    @staticmethod
    def max_profit_v1(prices: List[int]) -> int:
        """
        穷举法，将所有的买卖可能性都计算
        时间复杂度:O(n^2)
        空间复杂度:O(1)
        :param prices:
        :return:
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

    @staticmethod
    def max_profit_v2(prices: List[int]) -> int:
        """
        购买股票盈利的前提是在低谷买入，然后在高峰卖出，因此可以通过维护两个变量`max_profit`和`min_price`，
        记录当前的最大利润和股价低谷，如果当前的股价比min_price大，则判断是否比max_profit大，
        如果比`min_price`小，则更新`min_price`
        时间复杂度:O(n)
        空间复杂度:O(1)
        :param prices:
        :return:
        """
        max_profit = 0
        min_price = 9999999999999999999999999999999999999999999999
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(price - min_price, max_profit)
        return max_profit


def test():
    stock_1 = [7, 1, 5, 3, 6, 4]
    stock_2 = [7, 6, 4, 3, 1]
    assert Solution.max_profit_v1(stock_1) == 5
    assert Solution.max_profit_v1(stock_2) == 0
    assert Solution.max_profit_v2(stock_1) == 5
    assert Solution.max_profit_v2(stock_2) == 0


if __name__ == '__main__':
    test()
