#!/usr/bin/python3
"""
api that uses the get method to
get number of done tasks by users
and exported in json format
"""


def main():
    import csv
    import json
    import sys
    import urllib.request

    employee_id = sys.argv[1]
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    request_params = {"userId": sys.argv[1]}
    req_rep1 = requests.get(url1, params=requests_params)
    req_rep2 = requests.get(url2)

    req_rep1 = req_rep1.json()
    req_rep2 = req_rep2.json()

    filename2 = (f"{sys.argv[1]}.json")

    user_data = {f'{req_rep2["id"]}': []}
    user_keys = list(req_rep1[0].keys())
    for data in req_rep1:
        new_dict = {}
        for key in user_keys:
            if key != "title" and key != "completed":
                continue
            if key == "title":
                new_dict["task"] = data[key]
            else:
                new_dict[key] = data[key]
        new_dict["username"] = req_rep2["username"]
        user_data.get(f"{sys.argv[1]}").append(new_dict)
    with open(filename2, 'w', encoding='utf-8') as jsonfile:
        json.dump(user_data, jsonfile)

if __name__ == '__main__':
    main()
