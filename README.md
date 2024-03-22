# Sqlite Python Playground

Quickly execute test queries on a sqlite database.

## Usage

1. CSV Files
   Write csv files into the `tables` directory, name these files as `<table_name>.csv`.

2. `query.sql`
   Write your query contents into this text file. For example, `Select * from <table_name>`

3. run `sql.py`
   Run this python script to perform the following:

- Read in all csv files
- Write all csv files to a sqlite database: `db.db`
- Run the query defined in `query.sql` against the newly created database.
