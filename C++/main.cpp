#include "BinaryTree.h"
#include "Sort.h"
#include <iostream>

using namespace std;
using Tree::BinarySearchTree;
using Tree::Node;
using Sort::quick_sort;

void test_tree();
void tset_quick_sort();
void test_linked_list();

int main() {
	test_tree();
	tset_quick_sort();
    return 0;
}

void test_tree() {
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
}

void tset_quick_sort() {
	int a[10] = {21, 4, 1, 3, 9, 20, 25, 6, 21, 14};
	quick_sort(a, 0, 9, [](int x, int y) {
		return x < y;
	});

	for(auto n : a) {
		cout << n << ' ';
	}
	cout << endl;

	int b[10] = {21, 4, 1, 3, 9, 20, 25, 6, 21, 14};
	quick_sort(b, 0, 9, [](int x, int y) {
		return x > y;
	});

	for(auto n : b) {
		cout << n << ' ';
	}
	cout << endl;
}

void test_linked_list() {
	SingeLinkedList list = new SingleLinkedList<int>();
	for(int i = 1; i <= 10; i++) {
		list.add(i);
	}
	list.iterate([](int& value) {
		value += 10;
	});
	list.iterate([](int& value) {
		cout << value << ' ';
	});
	cout << '\n';
	for(int i = 1; i <= 10; i++) {
		list.remove();
	}
	list.iterate([](int& value) {
		cout << value << ' ';
	});
	cout << '\n';
}
