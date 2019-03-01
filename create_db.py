import sqlite3, argparse

SQL_CREATE_TABLE = """
    CREATE TABLE timetable (
        id integer, pn text, name text, position text, department text, dt date, value text
    )
"""

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser(description = "Create sqlite db")
    parser.add_argument("db", help = "database name")
    args = parser.parse_args()
    if (args.db):
        cursor = sqlite3.connect(args.db)
        cursor.execute(SQL_CREATE_TABLE)
        cursor.close()