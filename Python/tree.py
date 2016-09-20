'''
This module is just a proof of concept. Should not use it in production, unless you want to
'''

import random
import time
from collections import deque

class Node():
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None
		self.height = None

	def print(self):
		print(self.value)


# todo: inheritance of tree
class Tree():
	@staticmethod
	def is_bst(tree):
		def is_bst(root):
			ret = True
			if root.left:
				if root.left.value <= root.value:
					ret = ret and is_bst(root.left)
				else:
					print(root.left.value, root.value)
					return False
			if root.right:
				if root.right.value > root.value:
					ret = ret and is_bst(root.right)
				else:
					return False
			return ret
		if tree.root:
			return is_bst(tree.root)
		else:
			return True

class AVLTree():
	def __init__(self):
		self.root = None

	def left_rotate(root):
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

	@staticmethod
	def right_rotate(root):
		newRoot = root.left
		root.left = root.left.right
		newRoot.right = root
		root.height = AVLTree.set_height(root)
		newRoot.height = AVLTree.set_height(newRoot)
		return newRoot

	@staticmethod
	def set_height(node):
		if node:
			return 1 + max(
				node.left.height if node.left is not None else 0,
				node.right.height if node.right is not None else 0)
		print('return 0?')
		return 0

	@staticmethod
	def height(node):
		return node.height if node else 0

	def insert(self, node):
		def insert_on_node(root, new):
			if root is None:
				new.height = AVLTree.set_height(new)
				print(new.height)
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
		AVLTree.in_order_on_node(self.root)

	@staticmethod
	def in_order_on_node(node):
		if node:
			AVLTree.in_order_on_node(node.left)
			node.print()
			AVLTree.in_order_on_node(node.right)

	def pre_order(self):
		AVLTree.pre_order_on_node(self.root)

	@staticmethod
	def pre_order_on_node(node):
		if node:
			node.print()
			AVLTree.pre_order_on_node(node.left)
			AVLTree.pre_order_on_node(node.right)

	def post_order(self):
		AVLTree.post_order_on_node(self.root)

	@staticmethod
	def post_order_on_node(node):
		if node:
			if node.value == 17:
				print('17', node.left)
				print('17', node.right)
			AVLTree.post_order_on_node(node.left)
			AVLTree.post_order_on_node(node.right)
			node.print()

	# todo: add an apply function that apply an operation on node at each step of traversal
	# todo: level_order(self, apply)
	# this BFS is the general way of BFS in a graph
	# not limited to a tree level order
	def level_order(self, apply=None):
		if self.root:
			q = deque()
			q.append(self.root)
			while q:
				node = q.popleft()
				# if no apply function is specified, print the node
				apply(node) if apply else node.print()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
		else:
			print('This tree is empty')


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

	# print('In order:')
	# tree.in_order()
	print('Post order')
	tree.post_order()
	print('Level order:')
	tree.level_order(Node.print)
	print(Tree.is_bst(tree))

print("--- %s seconds ---" % (time.time() - start_time))
