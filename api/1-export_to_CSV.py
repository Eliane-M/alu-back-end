#!/usr/bin/python3
"""
api that uses the get method to
get number of done tasks by users
using CSV
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

    filename = (f"{sys.argv[1]}.csv")

    with open(filename, 'W', newline='') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=",", quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        for data in req_rep1:
            data_writer.writerow([data["userId"], req_rep2["username"],
                                 data["completed"], data["title"]])
