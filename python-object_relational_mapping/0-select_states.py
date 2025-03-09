#!/usr/bin/python3
"""
Script to list all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username>\
            <mysql password> <database name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        db.close()
        sys.exit(1)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
