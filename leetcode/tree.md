# tree

+ [Validate Binary Search Tree](#validate-binary-search-tree)

+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

+ [Invert Binary Tree](#invert-binary-tree)

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)

+ [Symmetric Tree](#symmetric-tree)

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/


```python

class Solution:
    def go_down(self, root, a, b):
        if root is None:
            return True
        if a is not None and root.val <= a:
            return False
        if b is not None and b <= root.val:
            return False
        x = self.go_down(root.left, a, root.val)
        y = self.go_down(root.right, root.val, b)
        return x and y


    def isValidBST(self, root) -> bool:
        a = None
        b = None
        return self.go_down(root, a, b)

```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/


```python

class Solution:
    def helper(self, root, ans):
        if root is None:
            return ans


        self.helper(root.left, ans)
        ans.append(root.val)
        self.helper(root.right, ans)
        return ans


    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        return self.helper(root, ans)

```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/


```python

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

```

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/


```python

class Solution:
    def go_down(self, root, n):
        if root is None:
            return n
        n += 1
        x = self.go_down(root.left, n)
        y = self.go_down(root.right, n)
        return max(x, y)


    def maxDepth(self, root: TreeNode) -> int:
        n = 0
        return self.go_down(root, n)

```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/


```python

class Solution:
    def helper(self, root, ans):
        if root is None:
            return ans
        self.helper(root.left, ans)
        if root.left is None:
            l = None
        else:
            l = root.left.val
        if root.right is None:
            r = None
        else:
            r = root.right.val
        ans.append(l)
        ans.append(root.val)
        ans.append(r)
        self.helper(root.right, ans)
        return ans


    def isSymmetric(self, root: TreeNode) -> bool:
        ans = []
        ans = self.helper(root, ans)
        print(ans)
        if ans == ans[::-1]:
            return True
        return False

```

## Binary Tree Level Order Traversal

https://docs.google.com/document/d/1YNrFCvlacz6m5w_7CPKQVzR8U-g8tzWUsg3DkjTKaX4/edit


```python

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = deque([(root, 1)])
        level = 0
        if root is None:
            return []


        while len(queue) != 0:
            helper = queue.popleft()
            r = helper[0]
            x = helper[1]
            if x > level:
                level += 1
                res.append([])
            res[level - 1].append(r.val)
            if r.left is not None:
                queue.append((r.left, level + 1))
            if r.right is not None:
                queue.append((r.right, level + 1))
        return res

```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/


```python

class Solution:
    cnt = None


    def helper(self, root):
        if root is None:
            return None
        x = self.helper(root.left)
        self.cnt -= 1
        if self.cnt == 0:
            return root.val
        y = self.helper(root.right)
        if x is not None:
            return x
        if y is not None:
            return y
        return None


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cnt = k
        ans = self.helper(root)
        return ans

```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/


```python

class BSTIterator:
    def _fill_stack(self):
        if self.cur is not None:
            self.nodes.append(self.cur)
            self.cur = self.cur.left
            self._fill_stack()


    def __init__(self, root: TreeNode):
        self.nodes = []
        self.cur = root
        self._fill_stack()


    def next(self) -> int:
        if len(self.nodes) != 0:
            root = self.nodes[-1]
            self.cur = self.nodes[-1].right
            self.nodes.pop(-1)
            self._fill_stack()
            return root.val


    def hasNext(self) -> bool:
        return len(self.nodes) != 0

```

