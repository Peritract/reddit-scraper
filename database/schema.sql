DROP TABLE post;
DROP TABLE subreddit;

CREATE TABLE subreddit (
    subreddit_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    subreddit_name TEXT UNIQUE NOT NULL
);

CREATE TABLE post (
    post_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    post_title TEXT NOT NULL,
    post_text TEXT NOT NULL,
    at TIMESTAMPTZ NOT NULL,
    author_name TEXT NOT NULL,
    subreddit_id INT NOT NULL,
    FOREIGN KEY (subreddit_id) REFERENCES subreddit(subreddit_id)
);

INSERT INTO
    subreddit (subreddit_name)
VALUES 
    ('conpiracytheories'),
    ('aww'),
    ('UK_food'),
    ('soccer'),
    ('politics'),
    ('aitah'),
    ('askreddit'),
    ('offmychest'),
    ('batmanarkham')
;