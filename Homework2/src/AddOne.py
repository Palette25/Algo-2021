class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        l = len(digits)

        for i in range(l):
            tmp = (digits[l-1-i] + carry) // 10
            digits[l-1-i] = (digits[l-1-i] + carry) % 10
            carry = tmp

            if carry == 0:
                break
        
        # Judge if need to create new element
        if carry >= 1:
            digits.insert(0, carry)

        return digits