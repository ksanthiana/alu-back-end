#!/usr/bin/python3

"""
getting data by using api
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch user data
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch user's todos
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Display output
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
