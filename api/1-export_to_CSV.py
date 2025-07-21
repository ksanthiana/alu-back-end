#!/usr/bin/python3
"""
Exports data for a given employee ID to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-export_to_CSV.py <employee_id>")

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit("Employee ID must be an integer.")

    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit("User not found.")

    user = user_response.json()
    username = user.get("username")

    # Fetch todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])

