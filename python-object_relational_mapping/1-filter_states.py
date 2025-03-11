#!/usr/bin/python3
"""
Lists all states with a starting with 'N' from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
