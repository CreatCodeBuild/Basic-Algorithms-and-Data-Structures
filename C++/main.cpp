#include "BinaryTree.h"
#include <iostream>

using namespace std;
using Tree::BinarySearchTree;

int main() {
    auto tree = BinarySearchTree();
	tree.add(5);
	tree.add(6);
	tree.add(1);
	tree.add(5);
	tree.add(2);
	tree.add(4);
	tree.add(3);

	cout << "In Order:\n";
	tree.in_order();
	cout << "Pre Order:\n";
	tree.pre_order();
	cout << "Post Order:\n";
	tree.post_order();
    return 0;
}
