
import praw
import pandas as pd

def fetch_posts():
    posts = [
        "I feel hopeless and tired of life",
        "Life is going well today",
        "I want everything to end",
        "Feeling great and optimistic"
    ]
    labels = [1,0,1,0]
    df = pd.DataFrame({"text":posts,"label":labels})
    df.to_csv("data/raw/reddit_posts.csv", index=False)

if __name__ == "__main__":
    fetch_posts()
