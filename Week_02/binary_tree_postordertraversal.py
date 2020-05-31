class Solution2:
    def postOrderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[init]
        """
        res = []

        def innerFunction(node):
            if not node:
                return
            innerFunction(node.left)
            innerFunction(node.right)
            res.append(node.val)

        innerFunction(root)
        return res
