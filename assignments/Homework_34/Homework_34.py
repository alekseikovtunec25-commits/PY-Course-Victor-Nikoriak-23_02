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

#Task3

import requests
import threading
import json


SUBREDDIT = "python"

comments = []
lock = threading.Lock()


def load_comments(size):
    url = "https://api.pushshift.io/reddit/comment/search/"

    params = {
        "subreddit": SUBREDDIT,
        "size": size
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()["data"]

            with lock:
                comments.extend(data)

            print(f"Loaded {len(data)} comments")

    except Exception as e:
        print("Error:", e)


threads = []

# создаём несколько потоков
for _ in range(5):
    thread = threading.Thread(
        target=load_comments,
        args=(100,)
    )

    threads.append(thread)
    thread.start()

# ждём завершения всех потоков
for thread in threads:
    thread.join()

# сортировка по времени
comments.sort(key=lambda x: x.get("created_utc", 0))

# сохранение в JSON
with open("reddit_comments.json", "w", encoding="utf-8") as file:
    json.dump(
        comments,
        file,
        ensure_ascii=False,
        indent=4
    )

print(f"Saved {len(comments)} comments")