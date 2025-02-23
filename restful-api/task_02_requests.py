import requests
import csv
"""
This module provides functions to fetch and print
posts from JSONPlaceholder and save them to a CSV file.
"""


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()
        posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
        print("Posts have been saved to 'posts.csv'.")
    else:
        print("Failed to fetch posts.")
