from auto_check import Queue

def rotate_queue(queue, n):
	if queue.size() > 0:
		for i in range(n):
			queue.enqueue(queue.dequeue())
	return queue