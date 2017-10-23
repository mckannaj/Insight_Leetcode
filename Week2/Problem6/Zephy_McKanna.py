"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
"""
import math

# Constructor for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DO NOT CHANGE THIS CLASS
class Solution(object):
    def sortedArrayToBST(self, nums):
        ##
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if (type(nums) is not list):
            print('Unknown input; sortedArrayToBST takes a sorted list. Returning None.')
            return None
        if (len(nums) == 0):
            return None
        if (len(nums) == 1):
            return TreeNode(nums[0])

        mid_index = math.floor(len(nums) / 2)
        head = TreeNode(nums[mid_index])
        head.left = self.sortedArrayToBST(nums[0:mid_index])
        head.right = self.sortedArrayToBST(nums[mid_index+1:])
        return head




#Please come up with your own testcases below:
def main():
    s = Solution()
    head = s.sortedArrayToBST([1,2,3,4,5,6,7,8])
    next = head
    node_num = 0
    while (next.left is not None):
        node_num += 1
        next = next.left
    print("Leftmost value expected 1; received {}. Tree height moving left = {}.".format(next.val, node_num))
    next = head
    node_num = 0
    while (next.right is not None):
        node_num += 1
        next = next.right
    print("Rightmost value expected 8; received {}. Tree height moving right = {}.".format(next.val, node_num))

    head = s.sortedArrayToBST(list(range(1001)))
    next = head
    node_num = 0
    while (next.left is not None):
        node_num += 1
        next = next.left
    print("Leftmost value expected 0; received {}. Tree height moving left = {}.".format(next.val, node_num))
    next = head
    node_num = 0
    while (next.right is not None):
        node_num += 1
        next = next.right
    print("Rightmost value expected 1000; received {}. Tree height moving right = {}.".format(next.val, node_num))


    head = s.sortedArrayToBST(list(range(-9999, 10000, 1111)))
    next = head
    node_num = 0
    while (next.left is not None):
        node_num += 1
        next = next.left
    print("Leftmost value expected -9999; received {}. Tree height moving left = {}.".format(next.val, node_num))
    next = head
    node_num = 0
    while (next.right is not None):
        node_num += 1
        next = next.right
    print("Rightmost value expected 9999; received {}. Tree height moving right = {}.".format(next.val, node_num))

if __name__ == "__main__":
    main()