#include <iostream>
namespace Sort {

	template<typename Type, typename Function>
	unsigned long long partition(Type sequence[], unsigned long long start, unsigned long long end, Function compare) {
		unsigned long long wall = start;
		auto& pivot = sequence[end];
		for(unsigned long long i = start; i < end; i++) {
			if(compare(sequence[i], pivot)) {
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

	template<typename Type, typename Function>
	void quick_sort(Type sequence[], unsigned long long start, unsigned long long end, Function compare) {
		if(start < end) {
			auto pivot = partition(sequence, start, end, compare);
			quick_sort(sequence, start, pivot-1, compare);
			quick_sort(sequence,  pivot+1, end, compare);
		}
	}
}
