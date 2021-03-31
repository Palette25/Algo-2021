class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dis, res = 2 * 10 ** 4 + 1, 0  # Set max number, making biggest distance
        size = len(nums)
        nums.sort()

        for index, ele in enumerate(nums):
            # Use double pointers to find triplet making smallest distance
            left, right = index+1, size-1
            while left < right:
                new_sum = ele + nums[left] + nums[right]
                # If equal, directly return
                if new_sum == target:
                    return target
                # Else get pos/neg flag
                flag = True if new_sum > target else False
                new_dis = abs(new_sum - target)
                if new_dis < dis:
                    dis, res = new_dis, new_sum
                # Move pointers twords zero distance
                if flag:
                    right -= 1
                else:
                    left += 1

        return res