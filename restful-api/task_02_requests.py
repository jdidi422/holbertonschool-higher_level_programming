import requests
import csv
"""Fetch posts from JSONPlaceholder API and print their titles."""


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder API and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save them to posts.csv, excluding 'userId'."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        filename = "posts.csv"
        headers = ["id", "title", "body"]

        filtered_posts = [{k: post[k] for k in headers} for post in posts]

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(filtered_posts)

        print(f"Data saved to {filename}")
