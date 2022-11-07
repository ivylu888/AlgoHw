class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def preorder(root):
            if root:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return " ".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = [int(x) for x in data.split()]
        
        def build(pre, inorder):
            if not pre:
                return None
            node = TreeNode(pre[0]) #pre[0] root
            temp = inorder.index(node.val)
            node.left = build(pre[1:temp+1], inorder[:temp]) #不包含0因為0是root
            node.right = build(pre[temp+1:], inorder[temp+1:])

            return node
        return build(data, sorted(data))
