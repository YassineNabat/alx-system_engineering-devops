#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
        Function that queries the Reddit API
        - If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        for post_data in req.json().get("data", {}).get("children", []):
            post_title = post_data.get("data", {}).get("title", "")
            print(post_title)
    else:
        print(None)


if __name__ == "__main__":
    subreddit = "Python"  # Replace "Python" with your desired subreddit
    top_ten(subreddit)
