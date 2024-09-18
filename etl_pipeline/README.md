# Reddit ETL pipeline

A pipeline that scrapes the front page of a specific subreddit.

## Installation

1. `pip install -r requirements.txt`
2. Create a `.env` file with the following contents

```sh
SUBREDDIT_NAME=XXXXXXXXXX
DB_HOST=XXXXXXXXXX
DB_USER=XXXXXXXXXX
DB_PASSWORD=XXXXXXXXXX
DB_PORT=5432
DB_NAME=reddit
```

`SUBREDDIT_NAME` should be a string value: the name of the subreddit without the `r/` prefix.

## Development

`python etl.py`

