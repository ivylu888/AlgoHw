class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = []
        node = head
        while node:
            array.append(node.val)
            node = node.next

        def helper(array, l, r):
            if l <= r: 
                mid = (l + r) // 2
                root = TreeNode(array[mid])
                root.left = helper(array, l, mid-1)
                root.right = helper(array, mid+1, r)
                return root
        return helper(array, 0, len(array)-1)
