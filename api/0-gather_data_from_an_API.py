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












































#!/usr/bin/python3
"""
get data by using api
"""
import requests
import sys

if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/users"
    user_data_url = "https://jsonplaceholder.typicode.com/todos?userId=2"

    user_response = requests.get(user_data_url)
    todo_response = requests.get(todo_url)
    # if todo_response.status_code & user_response.status_code == 200:
    todos = todo_response.json()
    users = user_response.json()
    for user in users:
        if user.get("id") == employee_Id:
            employee_name = user.get("name")
    # filter completed tasks
    done = []
    total = 0
    completed = 0
    for todo in todos:
        if todo.get("userId") == employee_Id:
            total += 1
            if todo.get("completed"):
                completed += 1
                done.append(todo.get("title"))
    # Display the progress information
    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for _ in done:
        print(f"\t {_}")
























#!/usr/bin/python3

"""Fetches and displays an employee's TODO list progress using a REST API."""

import requests
import sys



if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_data_url = "https://jsonplaceholder.typicode.com/users/2"

    user_response = requests.get(user_data_url)
    todo_response = requests.get(todo_url)
    # if todo_response.status_code & user_response.status_code == 200:
    todos = todo_response.json()
    users = user_response.json()
    for user in users:
        if user.get("id") == employee_Id:
            employee_name = user.get("name")
    # filter completed tasks
    done = []
    total = 0
    completed = 0
    for todo in todos:
        if todo.get("userId") == employee_Id:
            total += 1
            if todo.get("completed"):
                completed += 1
                done.append(todo.get("title"))
    # Display the progress information
    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for _ in done:
        print(f"\t {_}")
