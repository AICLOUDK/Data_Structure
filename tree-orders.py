import sys, threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self._in_order(0)
        return self.result

    def _in_order(self, node_index):
        if node_index == -1:
            return
        self._in_order(self.left[node_index])
        self.result.append(self.key[node_index])
        self._in_order(self.right[node_index])

    def preOrder(self):
        self.result = []
        self._pre_order(0)
        return self.result

    def _pre_order(self, node_index):
        if node_index == -1:
            return
        self.result.append(self.key[node_index])
        self._pre_order(self.left[node_index])
        self._pre_order(self.right[node_index])

    def postOrder(self):
        self.result = []
        self._post_order(0)
        return self.result

    def _post_order(self, node_index):
        if node_index == -1:
            return
        self._post_order(self.left[node_index])
        self._post_order(self.right[node_index])
        self.result.append(self.key[node_index])

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()