class Solution1:
    # 递归
    def preordertraversal(self, root):
        """
        :type  root: TreeNode
        :rtype: List[int]
        """
        res = []

        def innerfunction(node):
            if not node:
                return
            res.append(node.val)
            innerfunction(node.left)
            innerfunction(node.right)

        innerfunction(root)

        return res
    # 用栈递归

    def preordertraversal1(self, root):
        if not root:
            return []
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res
