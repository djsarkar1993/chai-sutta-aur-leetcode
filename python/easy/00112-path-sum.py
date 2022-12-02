"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.



Example 1:
         5_____
        /      \
    ___4     ___8
   /        /    \
  11       13     4
 /  \        \
7    2        1
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
  1
 / \
2   3
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.



Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""



def hasPathSum(root, targetSum):
        if root is None:
            return False
        
        elif (root.left is None) and (root.right is None) and (root.value == targetSum):
            return True
        
        else:
            remainingSum = targetSum - root.val
            return hasPathSum(root.left, remainingSum) or hasPathSum(root.right, remainingSum)



if __name__ == '__main__':
    from binarytree import build

    for data, targetSum in [    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22),
                                ([1,2,3], 5),
                                ([], 0)                                         ]:
        binary_tree = build(data)
        result = hasPathSum(binary_tree, targetSum)
        print(f'root={data}\ttargetSum={targetSum}\tresult={result}')