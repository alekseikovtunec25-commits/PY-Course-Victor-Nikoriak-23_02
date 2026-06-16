# Task1

import requests

sites = [
    "https://www.wikipedia.org/robots.txt",
    "https://twitter.com/robots.txt",
    "https://www.google.com/robots.txt"
]

for url in sites:
    response = requests.get(url)

    filename = url.split("//")[1].split("/")[0] + "_robots.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"Saved: {filename}")
