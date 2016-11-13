#ifndef BASICALGORITHMS_BINARYTREE_H
#define BASICALGORITHMS_BINARYTREE_H

#include <iostream>

using namespace std;

namespace Tree {
	class Node {
	public:
		int value;
		Node* left = nullptr;
		Node* right = nullptr;
		Node(int value) {
			this->value = value;
		}
		void add(int value) {
			if(value > this->value) {
				// right
				if( this->right == nullptr)
					this->right = new Node(value);
				else
					this->right->add(value);
			}
			else {
				// left
				if( this->left == nullptr)
					this->left = new Node(value);
				else
					this->left->add(value);
			}
		}
		bool find(int value) {
			if(this->value == value) {
				return true;
			}
			if(value > this->value) {
				if(this->right != nullptr)
					this->right->find(value);
				else
					return false;
			}
			else {
				if(this->left != nullptr)
					this->left->find(value);
				else
					return false;
			}
		}
		void in_order() {
			if(this->left != nullptr)
				this->left->in_order();
			cout << this->value << ' ';
			if(this->right != nullptr)
				this->right->in_order();
		}
		void pre_order() {
			cout << this->value << ' ';
			if(this->left != nullptr)
				this->left->in_order();
			if(this->right != nullptr)
				this->right->in_order();
		}
		void post_order() {
			if(this->left != nullptr)
				this->left->in_order();
			if(this->right != nullptr)
				this->right->in_order();
			cout << this->value << ' ';
		}
	};

	class BinarySearchTree {
	public:
		Node* root = nullptr;
		BinarySearchTree() {

		};
		void add(int value) {
			if(this->root == nullptr)
				this->root = new Node(value);
			else
				this->root->add(value);
		}
		bool find(int value) {
			return this->root->find(value);
		}
		void in_order() {
			this->root->in_order();
			cout << '\n';
		}
		void pre_order() {
			this->root->pre_order();
			cout << '\n';
		}
		void post_order() {
			this->root->post_order();
			cout << '\n';
		}
	};

};

#endif //BASICALGORITHMS_BINARYTREE_H
