class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort all the intervals with key as left-bounding (ascending order)
        intervals.sort(key=lambda x : x[0])

        result = []
        # Push first interval into result
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            # Judge whether current interval's left-bounding is larger
            # than result's last interval's right-bounding
            # If yes, no overlap
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            # If no, merge them
            else:
                result[-1][1] = max(intervals[i][1], result[-1][1])

        return result