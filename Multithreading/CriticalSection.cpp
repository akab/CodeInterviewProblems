#include <thread>
#include <mutex>
#include <shared_mutex>
#include <iostream>

/*
	CRITICAL SECTION ACCESS EXAMPLE
	This example demonstrates the use of std::mutex and std::condition_variable
	to regulate the concurrent access of two threads to the same resource (std::cout),
	in order to alternatively write in a for-loop 
*/

extern int count;
extern std::mutex mtx;
extern std::condition_variable cv;

static void alternateWrite() {
	std::unique_lock<std::mutex> lock(mtx);
	for (int i = 0; i < 10; ++i) {
		if (count >= 10) {
			cv.notify_one();
			break;
		}
		count++;
		std::cout << "[" << std::this_thread::get_id() << "]" << " count is " << count << std::endl;
		cv.notify_one();
		if (i != 9)
			cv.wait(lock);
	}
}

static void criticalSectionExample() {
	std::thread t1(alternateWrite);
	std::thread t2(alternateWrite);
	t1.join();
	t2.join();
}