#ifndef BASICALGORITHMS_SEQUENCE_H
#define BASICALGORITHMS_SEQUENCE_H

# include <iostream>

using std::cout;

namespace Sequence {
	template<class T>
	class SingleLinkedList {
	public:
		T* head;
		T* tail;
		unsigned long long size = 0;
		void add(T const * const node) const {
			if(head == nullptr) {
				head = node;
				tail = node;
			}
			else {
				tail->next = node;
				tail = node;
			}
		}

		//remove the node with the exact pointer to this value;
		bool remove(T const * const value);

		bool remove(T& value);

		// 0 the first element, -1 the last element
		// Use Python convention
		bool remove(long long index);

		//find if the exact pointer to this value is in the list
		bool find(T const * const value);

		//find if a node with the same value is in the list
		bool find(T& value);

		template<typename Function>
		void iterate(Function apply) {
			if(size == 0) {
				cout << "This LinkedList is empty. Nothing to iterate!\n"
			}
			else {
				// implement it
			}
		}
	};

	template<class T>
	class DoubleLinkedList {

	};

	template<class T>
	class Stack {

	};

	template<class T>
	class Queue {

	};

	template<class T>
	class PriorityQueue {

	};
}

namespace SequenceNode {

	template<class T>
	class SingleNode {
	public:
		T const * value;
		SingleNode const * next;
		SingleNode(T const * const value) {
			this->value = value;
			this->next = nullptr;
		}
		~SingleNode() {
			cout << "SingleNode is destroyed\n";
		}
	};

	template<class T>
	class DoubleNode {
	public:
		T const * value;
		DoubleNode const * pre;
		DoubleNode const * next;
		DoubleNode(T const * const value) {
			this->value = value;
			this->next = nullptr;
			this->pre = nullptr;
		}
		~DoubleNode() {
			cout << "DoubleNode is destroyed\n";
		}
	};
}

#endif
