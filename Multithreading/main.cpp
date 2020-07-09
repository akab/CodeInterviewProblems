#include <vector>
#include <iostream>
#include "Deadlock.cpp"
#include "CriticalSection.cpp"

int count;
std::mutex mtx;
std::mutex mA;
std::mutex mB;
std::condition_variable cv;


int main(int argc, char** argv) {
	//criticalSectionExample();
	//deadlockExample();

	return 0;
}
