#include <iostream>
namespace Sort {

	template<typename Type>
	unsigned long long partition(Type sequence[], unsigned long long start, unsigned long long end) {
		unsigned long long wall = start;
		Type pivot = sequence[end];
		for(unsigned long long i = start; i < end; i++) {
			if(sequence[i] < pivot) {
				auto temp = sequence[wall];
				sequence[wall] = sequence[i];
				sequence[i] = temp;
				wall++;
			}
		}
		auto temp = sequence[wall];
		sequence[wall] = sequence[end];
		sequence[end] = temp;
		return wall;
	}

	template<typename Type>
	void quick_sort(Type sequence[], unsigned long long start, unsigned long long end) {
		if(start < end) {
			auto pivot = partition(sequence, start, end);
			quick_sort(sequence, start, pivot-1);
			quick_sort(sequence,  pivot+1, end);
		}
	}







}
