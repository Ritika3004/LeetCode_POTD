class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #[3, 2, 1, 4]
        #[3], [2], [1], [4]
        #[3, 2]
        #[2, 1]
        #[3, 2, 1]

        #count=1
        #result=1
        # 0  1  2  3
        #[3, 2, 1, 4]
        #till ind 0 => [3]
        #till ind 1 => [3], [3, 2], [2]
        #till ind 2 => [3], [3, 2], [3, 2, 1], [2], [1]

        n=len(prices)
        count=1
        result=1
        for i in range(1, n):
            if prices[i]==prices[i-1]-1:
                count+=1
            else:
                count=1
            result+=count
        return result
