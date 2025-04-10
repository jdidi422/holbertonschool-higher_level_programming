#!/usr/bin/python3
"""
Listing all the states from a db
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Check input arguments
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} "
              "<username> <password> <database> <state name>")
        sys.exit(1)

    # Catch db credentials
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    state_name = sys.argv[4]

    # Connection to DB
    db = MySQLdb.connect(host=MY_HOST,
                         user=MY_USER,
                         passwd=MY_PASS,
                         db=MY_DB,
                         port=3306
                         )

    # Cursor creation to execute SQL queries
    cursor = db.cursor()

    # SQL query
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Print results in comma delimited format
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    result = ""
    for row in rows:
        if result:
            result += ", "
        result += row[0]
    print(result)

    # Close connection with db
    cursor.close()
    db.close()