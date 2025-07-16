class Solution:
    def canJump(self, nums: List[int]) -> bool:
        list_of_used_list = []
        def recursion(nums, list_of_used_list):
            if nums == []:
                return False

            if len(nums) == 1:
                return True
            elif nums in list_of_used_list:
                return False
            else:
                list_of_used_list.append(nums)
                value = nums[0]
                for i in range(value, 0, -1):
                    half_result = recursion(nums[i:], list_of_used_list)
                    if half_result:
                        return True
                return False
        result = recursion(nums, list_of_used_list)
        return result