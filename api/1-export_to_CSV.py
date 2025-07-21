#!/usr/bin/python3
"""
Exports completed tasks of a given employee ID to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-export_to_CSV.py <employee_id>")

    employee_id = sys.argv[1]

    try:
        int_id = int(employee_id)
    except ValueError:
        sys.exit("ID must be an integer")

    # Get user info
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    username = user.get("username")

    # Get todos
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

    # Write completed tasks only
    with open(f"{employee_id}.csv", mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get("completed"):
                writer.writerow([
                    employee_id,
                    username,
                    "True",
                    task.get("title")
                ])
