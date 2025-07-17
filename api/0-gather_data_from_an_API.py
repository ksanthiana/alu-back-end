#!/usr/bin/python3

"""
getting data by using api
"""

import requests
import sys

if __name__ == "__main__":
        employee_id = int(sys.argv[1])

        
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

                                
        user_data = user_response.json()
        todos_data = todos_response.json()

                                        
        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        number_done_tasks = len(done_tasks)

                                                                
        print(f"Employee {employee_name} is done with tasks({number_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")
