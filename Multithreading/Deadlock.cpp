#include <mutex>
#include <iostream>

/*
	DEADLOCK EXAMPLE
	Possible solutions may be:
	1. Restructure the code such that mutexes are acquired in the same order
	2. Use std::scoped_lock to acquire both mutexes at the same time
	3. Use std::timed_mutex so that mutex lock will be released after a timeout
*/

extern std::mutex mA;
extern std::mutex mB;

static void locksAB(std::string message) {
	mA.lock();
	std::this_thread::sleep_for(std::chrono::milliseconds(100));
	mB.lock();
	std::cout << std::this_thread::get_id() << " " << message.c_str() << std::endl;
	mB.unlock();
	mA.unlock();
}

static void lokcsBA(std::string message) {
	mB.lock();
	std::this_thread::sleep_for(std::chrono::milliseconds(100));
	mA.lock();
	std::cout << std::this_thread::get_id() << " " << message.c_str() << std::endl;
	mA.unlock();
	mB.unlock();
}

static void deadlockExample() {
	std::thread t1(locksAB, "Hello from t1!");
	std::thread t2(lokcsBA, "Hello from t2!");

	t2.join();
	t1.join();
}