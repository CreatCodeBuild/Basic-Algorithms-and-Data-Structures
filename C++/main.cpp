#include "BinaryTree.h"
#include "Sort.h"
#include <iostream>

using namespace std;
using Tree::BinarySearchTree;
using Tree::Node;
using Sort::quick_sort;

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

	// lambda
	tree.in_order([](Node const * const node) {
		cout << "Value: " << node->value+10 << ' ';
	});

	cout << "Pre Order:\n";
	tree.pre_order();
	cout << "Post Order:\n";
	tree.post_order();

	// int a[10] = {21, 4, 1, 3, 9, 20, 25, 6, 21, 14};
	// quick_sort(a, 0, 9);
	//
	// for(auto n : a) {
	// 	cout << n << ' ';
	// }
	// cout << endl;
    return 0;
}
