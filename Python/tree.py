import random
import time


class Node():
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None
		self.height = None
		self.size = None

	def print(self):
		print(self.value)


# todo: inheritance of tree
class Tree():
	pass

class AVLTree():
	def __init__(self):
		self.root = None

	def left_rotate(self, root):
		'''
		@root: rotation root, not the root of the whole tree
		'''
		newRoot = root.right
		# root.right.left is the next bigger node that can be used as the right of the old root
		root.right = root.right.left
		newRoot.left = root
		root.height = AVLTree.set_height(root)
		newRoot.height = AVLTree.set_height(newRoot)
		return newRoot;

	@classmethod
	def right_rotate(root):
		newRoot = root.left
		root.left = root.left.right
		newRoot.right = root
		root.height = AVLTree.set_height(root)
		newRoot.height = AVLTree.set_height(newRoot)
		return newRoot

	@classmethod
	def set_height(node):
		if node:
			return 1 + max(
				root.left.height if node.left is not None else 0,
				root.right.height if node.right is not None else 0)
		return 0

	@classmethod
	def height(node):
		return node.height if node else 0

	def insert(self, node):
		def insert_on_node(root, new):
			if root is None:
				return new
			if root.value <= new.value:
				root.right = insert_on_node(root.right, new)
			else:
				root.left = insert_on_node(root.left, new)
			balance = self.balance(root.left, root.right)
			if balance > 1:
				if AVLTree.height(root.left.left) >= AVLTree.height(root.left.right):
					root = AVLTree.right_rotate(root)
				else:
					root.left = AVLTree.left_rotate(root.left)
					root = AVLTree.right_rotate(root)
			elif balance < -1:
				if AVLTree.height(root.right.right) >= AVLTree.height(root.right.left):
					root = AVLTree.left_rotate(root);
				else:
					root.right = AVLTree.right_rotate(root.right);
					root = AVLTree.left_rotate(root)
			else:
				root.height = AVLTree.set_height(root)
			return root

		self.root = insert_on_node(self.root, node)

	def delete_one():
		pass

	def delete_all():
		pass

	def search():
		pass

	def balance(self, nodeLeft, nodeRight):
		return AVLTree.height(nodeLeft) - AVLTree.height(nodeRight)

	def in_order(self):
		AVLTree.in_order_on_node(self.root.left)
		self.root.print()
		AVLTree.in_order_on_node(self.root.right)

	@classmethod
	def in_order_on_node(node):
		AVLTree.in_order_on_node(node.left)
		node.print()
		AVLTree.in_order_on_node(node.right)

	def pre_order(self):
		self.root.print()
		AVLTree.in_order_on_node(self.root.left)
		AVLTree.in_order_on_node(self.root.right)

	@classmethod
	def pre_order_on_node(ndoe):
		node.print()
		AVLTree.pre_order_on_node(node.left)
		AVLTree.pre_order_on_node(node.right)

	def post_order(self):
		AVLTree.post_order_on_node(self.root.left)
		AVLTree.post_order_on_node(self.root.right)
		self.root.print()

	@classmethod
	def post_order_on_node(node):
		AVLTree.post_order_on_node(node.left)
		AVLTree.post_order_on_node(node.right)
		node.print()


	def level_order(self):
		pass

start_time = time.time()
if __name__ == '__main__':
	tree = AVLTree()
	node1 = Node(-10)
	node2 = Node(2)
	node3 = Node(13)
	node4 = Node(-13)
	node5 = Node(-15)
	node6 = Node(15)
	node7 = Node(17)
	node8 = Node(20)

	tree.insert(node1)
	tree.insert(node2)
	tree.insert(node3)
	tree.insert(node4)
	tree.insert(node5)
	tree.insert(node6)
	tree.insert(node7)
	tree.insert(node8)

	tree.in_order()
	tree.pre_order()
	tree.post_order()
	tree.level_order()

print("--- %s seconds ---" % (time.time() - start_time))
