#!/usr/bin/python3
"""
api that uses the get method to
get number of done tasks by users
"""


def main(employee_todo_progress):
    import json
    import sys
    import urllib.request

    employee_id = sys.arg[1]
    url1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"

    req_obj1 = urllib.request.Request(url1, method="GET")
    req_obj2 = urllib.request.Request(url2, method="GET")

    with urllib.request.urlopen(req_obj1) as response_obj1:
        response1 = json.load(response_obj1)
    with urllib.request.urlopen(req_obj2) as response_obj2:
        response2 = json.load(response_obj2)

    completed_tasks = []
    for task in response1:
        if task['completed'] is not True:
            continue
        completed_task.append(task)

    number_of_completed = len(completed_tasks)
    number_of_all_tasks = len(response1)
    employee_name = response2["name"]

    print(f"Employee {employee_name} is done with tasks ({number_of_completed}/{number_of_all_tasks}")
    for tasks in completed_tasks:
        print(f"\t {comp_tasks['title']}")
