#Task1
from threading import Thread

counter = 0
rounds = 100000


class Counter(Thread):

    def run(self):
        global counter

        for _ in range(rounds):
            counter += 1


t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter =", counter)