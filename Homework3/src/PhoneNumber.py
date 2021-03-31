class Solution:
    def __init__(self):
        self.res = []
        self.letters = [
            'abc', 'def', 'ghi', 'jkl', 
            'mno', 'pqrs', 'tuv', 'wxyz'
        ]
        self.digits = None

    def getCombination(self, index: int, sstr: str):
        # Recurrence end condition
        if index == len(self.digits):
            self.res.append(sstr)
            return
        
        char = int(self.digits[index])
        string = self.letters[char - 2]

        for ele in string:
            self.getCombination(index+1, sstr + ele)

    def letterCombinations(self, digits: str) -> List[str]:
        # Violent sloving method
        if len(digits) == 0:
            return []
        self.digits = digits
        self.getCombination(0, "")

        return self.res