#include <thread>
#include <mutex>
#include <shared_mutex>
#include <vector>
#include <iostream>

int count;
std::mutex mtx;
std::condition_variable cv;

void alternateWrite() {
		std::unique_lock<std::mutex> lock(mtx);
		for (int i = 0; i < 10; ++i) {
			if (count >= 10) {
				cv.notify_one();
				break;
			}
			count++;
			std::cout << "[" << std::this_thread::get_id() << "]" << " count is " << count << std::endl;
			cv.notify_one();
			if(i != 9)
				cv.wait(lock);
		}
}

int main(int argc, char** argv) {
	std::thread t1(alternateWrite);
	std::thread t2(alternateWrite);
	t1.join();
	t2.join();

	return 0;
}
