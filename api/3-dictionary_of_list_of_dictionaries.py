#!/usr/bin/python3
"""
extending the python script
from task #0
to export data in json
"""


def main():
    import json
    import requests
    import sys
    url1 = f"https://jsonplaceholder.typicode.com/users"
    url2 = f"https://jsonplaceholder.typicode.com/todos"
    req_rep1 = requests.get(url1)
    req_rep2 = requests.get(url2)
    req_rep1 = req_rep1.json()
    req_rep2 = req_rep2.json()
    all_user_keys = req_rep2[0].keys()
    all_user_json = {}
    user_count = 0
    each_user_todo = 20
    for i in range(0, len(req_rep2), each_user_todo):
        new_list = []
        for j in range(i, i+each_user_todo):
            new_dict = {}
            new_dict["username"] = req_rep1[user_count]["username"]
            for key in all_user_keys:
                if key != "title" and key != "completed":
                    continue
                if key == "title":
                    new_dict["task"] = req_rep2[j][key]
                else:
                    new_dict["completed"] = req_rep2[j][key]
            new_list.append(new_dict)
        all_user_json[f'{req_rep1[user_count]["id"]}'] = new_list
        user_count += 1
    with open("todo_all_employees.json", 'w', encoding="utf-8") as jsonfile:
        json.dump(all_user_json, jsonfile)

if __name__ == '__main__':
    main()
