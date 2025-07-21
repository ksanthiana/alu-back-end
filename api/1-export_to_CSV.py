#!/usr/bin/python3
"""Exports tasks of an employee to a CSV file"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    username = user_response.json().get("username")
    todos = todos_response.json()

    filename = "{}.csv".format(user_id)

    with open(filename, mode='w', newline='') as csvfile: 
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id,
                             username,
                             task.get("completed"),
                             task.get("title")])
