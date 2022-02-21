class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        for interval in intervals:
            if len(result):
                l, r = result[-1]
                lc, rc = interval
                if r >= lc:
                    result.pop()
                    result.append([l,max(r,rc)])
                else:
                    result.append(interval)
            else:
                result.append(interval) 
        return result

        