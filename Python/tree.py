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

	def set_height(self):
		self.height = 1 + max(Node.height(self.left), Node.height(self.right))

	@staticmethod
	def height(node):
		return node.height if node else 0


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

	# todo: should check None at parent level to avoid unnecessary function call
	# todo: implement iterative(heep space stack) DFS
	def in_order(self):
		if self.root:
			Tree.in_order_on_node(self.root)
		else:
			print('This tree is empty')

	@staticmethod
	def in_order_on_node(node):
		if node:
			Tree.in_order_on_node(node.left)
			node.print()
			Tree.in_order_on_node(node.right)

	def pre_order(self):
		if self.root:
			Tree.pre_order_on_node(self.root)
		else:
			print('This tree is empty')

	@staticmethod
	def pre_order_on_node(node):
		if node:
			node.print()
			Tree.pre_order_on_node(node.left)
			Tree.pre_order_on_node(node.right)

	def post_order(self):
		if self.root:
			Tree.post_order_on_node(self.root)
		else:
			print('This tree is empty')

	@staticmethod
	def post_order_on_node(node):
		if node:
			Tree.post_order_on_node(node.left)
			Tree.post_order_on_node(node.right)
			node.print()

	# this BFS is the general way of BFS in a graph
	# not limited to a tree level order
	def level_order(self, apply=None):
		'''
		@apply: a function that is called at each step of traversal, caller scope has to implement it
		'''
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


class BST(Tree):
	pass


class AVLTree(BST):
	def __init__(self, compare):
		self.root = None
		self.compare = compare

	def left_rotate(root):
		'''
		@root: rotation root, not the root of the whole tree
		'''
		newRoot = root.right
		# root.right.left is the next bigger node that can be used as the right of the old root
		root.right = root.right.left
		newRoot.left = root
		root.set_height()
		newRoot.set_height()
		return newRoot;

	@staticmethod
	def right_rotate(root):
		newRoot = root.left
		root.left = root.left.right
		newRoot.right = root
		root.set_height()
		newRoot.set_height()
		return newRoot

	@staticmethod
	def balance_check(node):
		return Node.height(node.left) - Node.height(node.right)

	@staticmethod
	def balancing(node):
		balance = AVLTree.balance_check(node)
		if balance > 1:
			if Node.height(node.left.left) >= Node.height(node.left.right):
				node = AVLTree.right_rotate(node)
			else:
				node.left = AVLTree.left_rotate(node.left)
				node = AVLTree.right_rotate(node)
		elif balance < -1:
			if Node.height(node.right.right) >= Node.height(node.right.left):
				node = AVLTree.left_rotate(node)
			else:
				node.right = AVLTree.right_rotate(node.right);
				node = AVLTree.left_rotate(node)
		else:
			node.set_height()
		return node

	def insert(self, node):
		def insert_on_node(root, new):
			if root is None:
				new.set_height()
				return new
			if new.value > root.value:
				root.right = insert_on_node(root.right, new)
			else:
				root.left = insert_on_node(root.left, new)
			return AVLTree.balancing(root)

		self.root = insert_on_node(self.root, node)

	def delete_one():
		pass

	def delete_all():
		pass

	def search():
		pass




start_time = time.time()
if __name__ == '__main__':
	tree = AVLTree(lambda a, b: a > b)
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

	print('In order:')
	tree.in_order()
	# print('Post order')
	# tree.post_order()
	# print('Level order:')
	# tree.level_order(Node.print)
	# print(Tree.is_bst(tree))

print("--- %s seconds ---" % (time.time() - start_time))
