class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return

        curr = self.root
        while True:
            if key > curr.key:
                if curr.right is None:
                    curr.right = newNode
                    return
                curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = newNode
                    return
                curr = curr.left
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1
        

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeRecursion(self.root, key)

    def removeRecursion(self, curr, key):
        if curr is None:
            return None
        if key > curr.key:
            curr.right = self.removeRecursion(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeRecursion(curr.left, key)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeRecursion(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        keys_lst = []
        self.inorderTraversal(self.root, keys_lst)
        return keys_lst

    def inorderTraversal(self, root, res):
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.key)
            self.inorderTraversal(root.right, res)

