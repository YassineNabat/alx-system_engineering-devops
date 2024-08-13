#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests

def recurse(subreddit, hot_list=[], after=""):
    """
        Queries the Reddit API and returns
        a list containing the titles of all hot articles for a given subreddit.

        - If not a valid subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    
    params = {"after": after}

    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        children = req.json().get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title", "")
            hot_list.append(title)
                                                                                                    
        after = req.json().get("data", {}).get("after", "")

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

        
    
    if __name__ == "__main__":
        subreddit = "https://www.reddit.com/r/{}/hot.json"  
        result = recurse(subreddit)
        if result is not None:
            print(result)
        else:
            print("No results found.")

