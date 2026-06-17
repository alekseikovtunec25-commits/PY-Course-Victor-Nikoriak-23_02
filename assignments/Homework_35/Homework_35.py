#Task1
import math


def is_prime(number):
    """
    Возвращает True, если число простое,
    иначе False.
    """

    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1

    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False

    return True
#Проверка
NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]

for number in NUMBERS:
    print(f"{number}: {is_prime(number)}")

#Task2
import json
import requests
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count

BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT = "python"

# Получаем одну страницу комментариев
def fetch_comments(before):
    params = {
        "subreddit": SUBREDDIT,
        "size": 100,
        "before": before,
        "sort": "desc"
    }

    response = requests.get(BASE_URL, params=params, timeout=20)
    response.raise_for_status()

    data = response.json().get("data", [])
    return data


# Используем concurrent для параллельных запросов
def load_pages():
    timestamps = [
        1750000000,
        1740000000,
        1730000000,
        1720000000,
        1710000000,
    ]

    comments = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_comments, timestamps)

        for page in results:
            comments.extend(page)

    return comments


# multiprocessing для обработки данных
def prepare_comment(comment):
    return {
        "id": comment.get("id"),
        "author": comment.get("author"),
        "body": comment.get("body"),
        "created_utc": comment.get("created_utc")
    }


def main():
    comments = load_pages()

    with Pool(cpu_count()) as pool:
        processed = pool.map(prepare_comment, comments)

    processed.sort(key=lambda x: x["created_utc"])

    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(
            processed,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Сохранено {len(processed)} комментариев")


if __name__ == "__main__":
    main()