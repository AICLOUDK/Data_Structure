import sys
import threading

sys.setrecursionlimit(10 ** 8)
threading.stack_size(2 ** 27)

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left if left != -1 else None
        self.right = right if right != -1 else None

class TreeIsBST:
    def __init__(self):
        self.nodes = []
        self.root = None
        self.keys_inorder = []
        self.result_inorder = []

    def read(self):
        n = int(sys.stdin.readline())
        for i in range(n):
            key, left, right = map(int, sys.stdin.readline().split())
            node = Node(key, left, right)
            self.nodes.append(node)
        if n > 0:
            self.root = self.nodes[0]

    def inorder(self, node):
        if not node:
            return
        if node.left:
            self.inorder(self.nodes[node.left])
        self.keys_inorder.append(node.key)
        if node.left and node.right:
            self.result_inorder.append(self.nodes[node.left].key < node.key <= self.nodes[node.right].key)
        elif node.left:
            self.result_inorder.append(self.nodes[node.left].key < node.key)
        elif node.right:
            self.result_inorder.append(node.key <= self.nodes[node.right].key)
        else:
            self.result_inorder.append(True)
        if node.right:
            self.inorder(self.nodes[node.right])

    def is_bst(self):
        if len(self.nodes) <= 1:
            return True
        self.inorder(self.root)
        return all(self.result_inorder) and self.is_keys_sorted()

    def is_keys_sorted(self):
        return all(self.keys_inorder[i] <= self.keys_inorder[i + 1] for i in range(len(self.keys_inorder) - 1))

def main():
    tree = TreeIsBST()
    tree.read()
    if tree.is_bst():
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == "__main__":
    threading.Thread(target=main).start()