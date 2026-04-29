class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Lamda is just function tells us start sorrt with start index
        intervals.sort(key=lambda x: x[0])

        merged = []

        for i in intervals:

            if not merged or merged[-1][1] < i[0]:
                merged.append(i)

            else:
                #if we found overlap, merge by updating the end
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged

        