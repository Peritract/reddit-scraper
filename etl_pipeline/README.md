# Reddit ETL pipeline

A pipeline that scrapes the front page of a specific subreddit.

## Installation

1. `pip install -r requirements.txt`
2. Create a `.env` file with the following contents

```sh
DB_HOST=XXXXXXXXXX
DB_USER=XXXXXXXXXX
DB_PASSWORD=XXXXXXXXXX
DB_PORT=5432
DB_NAME=reddit
```

3. Create a `txt` file called `subreddits.txt` with the following contents:

```
subreddit_name_1
subreddit_name_2
...
```
The subreddit names should be without prefixes. For example "soccer" to refer to "r/soccer".

## Development

`python etl.py`

