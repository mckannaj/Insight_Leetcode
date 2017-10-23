"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Source: https://leetcode.com/problems/permutations/#/description
"""

# DO NOT CHANGE THIS CLASS
class Solution(object):
	#YOUR CODE GOES HERE
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # deal with edge cases first
        if type(nums) is not list:
            print('permute expects a list as input; received {}. Returning None.'.format(type(nums)))
            return None
        if (len(nums) < 2): # no permutations here
            return [nums]
        if (len(nums) == 2):
            return [nums,[nums[1],nums[0]]]

        permutations = []
        for idx, num in enumerate(nums):
            head = [nums[idx]]
            tail = nums[0:idx]+nums[idx+1:]
            neworder = head+tail
            this_head_permutations = self.permute_helper(neworder)
            permutations = permutations + this_head_permutations
        return permutations

    def permute_helper(self, nums):
        if len(nums) < 3:
            print("Error! permute_helper should never be called with less than three items in the list. Returning original list.")
            return nums
        else:
            smaller_permutation = self.permute(nums[1:])
            lists_with_this_head = []
            for idx, sublist in enumerate(smaller_permutation):
                sublist.insert(0, nums[0])
                lists_with_this_head.append(sublist)
            return lists_with_this_head


# Please add your own test cases below:

def main():
    s = Solution()
    error_return = s.permute('not a list')
    print("Expected return None or Error; received {}.".format(error_return))

    list_of_lists = s.permute([])
    print("Expected length of return = 1; received {}.".format(len(list_of_lists)))
    print("Expected return = [[]]; received {}.".format(list_of_lists))

    list_of_lists = s.permute([2])
    print("Expected length of return = 1; received {}.".format(len(list_of_lists)))
    print("Expected return = [[2]]; received {}.".format(list_of_lists))

    list_of_lists = s.permute([1,2])
    print("Expected length of return = 2; received {}.".format(len(list_of_lists)))
    print("Expected return = [[1,2],[2,1]]; received {}.".format(list_of_lists))

    list_of_lists = s.permute([1,2,3])
    print("Expected length of return = 6; received {}.".format(len(list_of_lists)))
    print("Expected return = [[1, 2, 3],[1, 3, 2],[2, 1, 3],[2, 3, 1],[3, 1, 2],[3, 2, 1]]; received {}.".format(list_of_lists))

    list_of_lists = s.permute([1,2,3,4])
    print("Expected length of return = 24; received {}.".format(len(list_of_lists)))

    list_of_lists = s.permute([5,3,19,12, 1, -63, 33])
    print("Expected length of return = 5040; received {}.".format(len(list_of_lists)))


if __name__ == "__main__":
    main()

