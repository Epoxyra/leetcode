class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i in range(len(intervals)):
            # Check if the new interval is before the interval i
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Check if the new interval is after the interval i
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Else, the new interval is overlapping with the interval i
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

    
intervals = [[1,3],[6,9]]
newInterval = [2,5]
sol = Solution()
print(sol.insert(intervals, newInterval))