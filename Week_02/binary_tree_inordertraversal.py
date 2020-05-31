class Solution:
    def inordertraversal(self, root):
        res = []

        def return_root_val(node):
            if not node:
                return
            return_root_val(root.left)
            res.append(root.val)
            return_root_val(root.right)
        return_root_val(root)
        return res
    # 用栈递归

    def inordertravalsal1(self, root):
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
