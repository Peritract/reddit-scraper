# Reddit database

A simple database to store Reddit data

## Installation & Setup

1. Create a `.env` file with the below details.
2. Run `psql postgres -c "CREATE DATABASE reddit;"` to create the database.
3. RUN `bash setup-db.sh` to create initial tables/seed data.


```sh
DB_HOST=XXXXXXXXXX
DB_USER=XXXXXXXXXX
DB_PASSWORD=XXXXXXXXXX
DB_PORT=5432
DB_NAME=reddit
```