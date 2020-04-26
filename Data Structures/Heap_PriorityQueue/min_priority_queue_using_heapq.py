""""
We will use python predefined data structure heapq to implement Priority Queue
we will use array [task, priority, is_deleted] to represent each item
"""

from heapq import *


class PriorityQueue(object):

    def __init__(self, is_min_heap):
        self.task_dict = {}
        self.priority_queue = []
        if is_min_heap:
            self.mul = 1
        else:
            self.mul = -1

    def is_contains_task(self, task):
        if task in self.task_dict:
            return True
        return False

    def add_task(self, priority, task):
        if self.is_contains_task(task):
            raise KeyError("Task already present")
        entry = [self.mul * priority, task, False]
        self.task_dict[task] = entry
        heappush(self.priority_queue, entry)

    def remove_task(self, task):
        if not self.is_contains_task(task):
            raise KeyError("Task not present to remove")
        entry = self.task_dict.pop(task)
        entry[2] = True

    def pop_task(self):
        while self.priority_queue:
            priority, task, is_removed = heappop(self.priority_queue)
            if not is_removed:
                del self.task_dict[task]
                return task
        raise KeyError("Priority Queue is empty to be pop")

    def peek_task(self):
        while self.priority_queue:
            priority, task, is_removed = heappop(self.priority_queue)
            if not is_removed:
                heappush(self.priority_queue, [priority, task, is_removed])
                return task
        raise KeyError("Priority Queue is empty to be peek")

    def remove_task(self, task):
        entry = self.task_dict.pop(task)
        entry[2] = True

    def change_priority(self, priority, task):
        if not self.is_contains_task(task):
            raise KeyError("Task not present to change the priority")
        self.remove_task(task)
        entry = [self.mul * priority, task, False]
        self.task_dict[task] = entry
        heappush(self.priority_queue, entry)

    def is_empty(self):
        try:
            self.peek_task()
            return False
        except KeyError:
            return True


if __name__ == "__main__":
    min_pq = PriorityQueue(True)
    task1 = "play vlc"
    task2 = "search another planet and identity its speed using ML"
    task3 = "cleanup the room"
    task4 = "bring a cup of coffee"
    task5 = "scan for any spacecraft issue"

    min_pq.add_task(3, task1)
    min_pq.add_task(1, task2)
    min_pq.add_task(2, task4)

    min_pq.change_priority(0, task1)

    while min_pq.is_empty() is False:
        print(min_pq.pop_task())

    # min_pq.change_priority(0, task1)

    # while min_pq.is_empty() is False:
    #     print(min_pq.pop_task())
