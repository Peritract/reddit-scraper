"""An ETL pipeline that scrapes Reddit data."""

from os import environ as ENV, _Environ
from datetime import datetime

from dotenv import load_dotenv
import requests as req
from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import execute_values, RealDictCursor


BASE_URL = "https://old.reddit.com/r"


def extract_reddit_data(subreddit_name: str) -> list[dict]:
    """Returns the listing data from a Reddit link."""

    url = f"{BASE_URL}/{subreddit_name}.json"
    res = req.get(url)

    if res.status_code == 200:
        data = res.json()
        return data["data"]["children"]
    else:
        raise ValueError(f"Unable to access the {subreddit_name} subreddit.")


def extract_post_information(post: dict) -> dict:
    """Returns key data about a post."""
    return {
        "title": post["data"]["title"],
        "text": post["data"]["selftext"],
        "author_name": post["data"]["author"],
        "author_id": post["data"]["author_fullname"],
        "at": post["data"]["created_utc"]
    }


def get_all_post_details(posts: list[dict]) -> list[dict]:
    """Returns key details for all posts."""

    return [extract_post_information(p) for p in posts]


def get_connection(config: _Environ) -> connection:
    """Returns a live DB connection."""

    return connect(
        host=config["DB_HOST"],
        user=config["DB_USER"],
        dbname=config["DB_NAME"],
        port=config["DB_PORT"],
        password=config["DB_PASSWORD"],
        cursor_factory=RealDictCursor
    )

def get_subreddit_id(subreddit_name: str, conn: connection) -> int:
    """Gets the subreddit ID from the database."""
    
    with conn.cursor() as cur:
        cur.execute("SELECT subreddit_id FROM subreddit WHERE subreddit_name = %s",
                    [subreddit_name])
        result = cur.fetchone()

    return result["subreddit_id"]

def preprocess_post_details(posts: list[dict], subreddit_id: int) -> tuple[str, str, int, str, int]:
    """Returns a tuple of DB-appropriate values."""
    
    rows = []

    for p in posts:
        rows.append((p["title"], p["text"], datetime.fromtimestamp(p["at"]), p["author_name"], subreddit_id))

    return rows

def upload_post_details(posts: list[dict], conn: connection) -> None:
    """Uploads all posts to the database."""
    
    q = """
    INSERT INTO post
        (post_title, post_text, at, author_name, subreddit_id)
    VALUES %s
    """

    with conn.cursor() as cur:

        execute_values(cur, q, posts)


if __name__ == "__main__":

    load_dotenv()

    conn = get_connection(ENV)

    posts = extract_reddit_data(ENV['SUBREDDIT_NAME'])

    to_insert = preprocess_post_details(get_all_post_details(posts),
                                        subreddit_id=get_subreddit_id(ENV["SUBREDDIT_NAME"], conn))

    upload_post_details(to_insert, conn)

    conn.commit()
    conn.close()