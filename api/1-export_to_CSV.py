#!/usr/bin/python3
import csv
import sys
import requests


def main():
    if len(sys.argv) != 2:
        return
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        return

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        return
    user = user_resp.json()
    username = user.get('username')

    params = {'userId': user_id}
    todos_resp = requests.get(todos_url, params=params)
    if todos_resp.status_code != 200:
        return
    todos = todos_resp.json()

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([str(user_id), username, str(t.get('completed')), t.get('title')])


if __name__ == '__main__':
    main()

