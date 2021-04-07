class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = 0
        N = len(citations)
        # Sort the citations list
        citations.sort()
        # After sorting, 
        # Find max h number
        while i < N and citations[N - 1 - i] > i:
            i += 1

        return i