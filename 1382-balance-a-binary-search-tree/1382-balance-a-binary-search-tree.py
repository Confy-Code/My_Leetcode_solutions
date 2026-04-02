# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.in_order = []

        def order_in_list(node):
            if not node:
                return

            order_in_list(node.left)
            self.in_order.append(node.val)  #append before you go to the right(greater nodes)
            order_in_list(node.right)
        
        order_in_list(root)

        def balancedTree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(self.in_order[mid])

            node.left = balancedTree(left, mid - 1)
            node.right = balancedTree(mid + 1, right)

            return node
        
        return balancedTree(0, len(self.in_order) - 1)

            


        