from avl_node import AVLNode


class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None

    def get_tree_root(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root

    def get_tree_height(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        if self.root is not None:
            return self.root.height
        else:
            return -1

    def get_tree_size(self):
        """Yields number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """

        if self.root is not None:
            return len(self.to_array())
        else:
            return 0

    def to_array(self):
        """Yields an array representation of the tree's values (pre-order).
        :return Array representation of the tree values.
        """
        array = []
        if self.root is not None:
            return self._to_array(self.root, array)
        elif self.root is None:
            print(array)

    def _to_array(self, curr_node, list):
        if curr_node is not None:
            list.append(curr_node.value)
            self._to_array(curr_node.left, list)
            self._to_array(curr_node.right, list)
            return list

    def find_by_key(self, key):
        """Returns value of node with given key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        if key is None:
            raise ValueError
        if self.root is not None:
            return self._find_by_key(key, self.root)

    def _find_by_key(self, key, curr_node):
        if curr_node is not None:
            if key == curr_node.key:
                return curr_node.value
            left = self._find_by_key(key, curr_node.left)
            right = self._find_by_key(key, curr_node.right)

            if left is not None:
                return left
            elif right is not None:
                return right

    def insert(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. May be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if key is None or value is None:
            raise ValueError
        if self.root is None:
            self.root = AVLNode(key, value)
            return True
        else:
            if self._insert(key, value, self.root) is None:
                return True
            else:
                return False

    def _insert(self, key, value, curr_node):
        if value < curr_node.value and key != curr_node.key:
            if curr_node.left is None:
                curr_node.left = AVLNode(key, value)
                curr_node.left.parent = curr_node
                self.balance_insertion(curr_node.left)
            else:
                self._insert(key, value, curr_node.left)
        elif value > curr_node.value and key != curr_node.key:
            if curr_node.right is None:
                curr_node.right = AVLNode(key, value)
                curr_node.right.parent = curr_node
                self.balance_insertion(curr_node.right)
                return True
            else:
                self._insert(key, value, curr_node.right)
        elif curr_node.key == key:
            return False

    def node_height(self, curr_node):
        if curr_node is None:
            return -1
        return curr_node.height

    def balance_insertion(self, curr_node, track = []):
        if curr_node.parent is None:
            return
        track = [curr_node] + track

        left_height = self.node_height(curr_node.parent.left)
        right_height = self.node_height(curr_node.parent.right)

        if abs(left_height - right_height) > 1:
            track = [curr_node.parent] + track
            self.rebalance(track[0], track[1], track[2])
            return

        new_height = 1 + curr_node.height
        if new_height > curr_node.parent.height:
            curr_node.parent.height = new_height
        self.balance_insertion(curr_node.parent, track)

    def remove_by_key(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if key is None:
            raise ValueError

        if self.root is not None:
            if self._remove_by_key(key) is None:
                return True
            else:
                return False
        elif self.root is None:
            return False

    def find_node(self, key):
        if self.root is not None:
            return self._find_node(key, self.root)

    def _find_node(self, key, curr_node):
        if curr_node is not None:
            if key == curr_node.key:
                return curr_node
            left = self._find_node(key, curr_node.left)
            right = self._find_node(key, curr_node.right)

            if left is not None:
                return left
            elif right is not None:
                return right

    def _remove_by_key(self, key):
        curr_node = self.find_node(key)
        if curr_node is None:
            return False

        def num_children(n):
            num_children = 0
            if n.left != None: num_children += 1
            if n.right != None: num_children += 1
            return num_children

        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current

        node_parent = curr_node.parent
        node_children = num_children(curr_node)
        if node_children == 0:

            if node_parent != None:
                if node_parent.left == curr_node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # CASE 2
        if node_children == 1:
            if curr_node.left != None:
                child = curr_node.left
            else:
                child = curr_node.right

            if node_parent != None:
                if node_parent.left == curr_node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child
            child.parent = node_parent

        # CASE 3
        if node_children == 2:
            successor = min_value_node(curr_node.right)
            curr_node.value = successor.value
            aux = successor.key
            self._remove_by_key(successor.key)
            curr_node.key = aux
            return

        if node_parent != None:
            node_parent.height = 1 + max(self.node_height(node_parent.left), self.node_height(node_parent.right))
            self.balance_deletion(node_parent)

    def balance_deletion(self, curr_node):
        if curr_node.parent == None:
            curr_node.height = 1 + max(self.node_height(curr_node.left), self.node_height(curr_node.right))
            return

        left_height = self.node_height(curr_node.left)
        right_height = self.node_height(curr_node.right)

        if abs(left_height - right_height) > 1:
            if self.node_height(curr_node.left) > self.node_height(curr_node.right):
                y = curr_node.left
            else:
                y = curr_node.right

            if self.node_height(y.left) > self.node_height(y.right):
                x = y.left
            else:
                x = y.right
            self.rebalance(curr_node, y, x)
        self.balance_deletion(curr_node.parent)

    def rebalance(self, z, y, x):
        array = self._populate_array(z, z, y, x)
        if z.parent is not None:
            subtree_root = z.parent
            if z.parent.left is z:
                z.parent.left = array[3]
                array[3].parent = subtree_root
            elif z.parent.right is z:
                z.parent.right = array[3]
                array[3].parent = subtree_root
        elif z.parent is None:
            self.root = array [3]
            array[3].parent = None

        array[3].left = array[1]
        array[1].parent = array[3]

        array[3].right = array[5]
        array[5].parent = array[3]

        array[1].left = array[0]
        if array[0] is not None:
            array[0].parent = array[1]

        array[1].right = array[2]
        if array[2] is not None:
            array[2].parent = array[1]

        array[5].left = array[4]
        if array[4] is not None:
            array[4].parent = array[5]

        array[5].right = array[6]
        if array[6] is not None:
            array[6].parent = array[5]

        z.height = 1 + max(self.node_height(z.left), self.node_height(z.right))
        y.height = 1 + max(self.node_height(y.left), self.node_height(y.right))
        x.height = 1 + max(self.node_height(x.left), self.node_height(x.right))

    def _populate_array(self, curr_node, z, y, x):
        if curr_node is None:
            return [ None ]
        elif curr_node in [z, y, x]:
            out = self._populate_array(curr_node.left, z, y, x)
            out += [curr_node]
            out += self._populate_array(curr_node.right, z, y, x)
            return out
        return [curr_node]