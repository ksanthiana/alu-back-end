#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    # Get employee ID from command-line argument
    employee_Id = int(sys.argv[1])

    # Fetch user info and todos
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_Id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_Id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todos_url)

    # Parse JSON data
    user_data = user_response.json()
    todos = todo_response.json()

    # Get employee name
    employee_name = user_data.get("name")

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    # Display the progress
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

