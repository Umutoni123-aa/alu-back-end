#!/usr/bin/python3

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

    # get username
    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        return
    user = user_resp.json()
    username = user.get('name')

    # get todos for this user
    params = {'userId': user_id}
    todos_resp = requests.get(todos_url, params=params)
    if todos_resp.status_code != 200:
        return
    todos = todos_resp.json()

    total = len(todos)
    done_tasks = [t for t in todos if t.get('completed') is True]
    done_count = len(done_tasks)

    print('Employee {} is done with tasks({}/{}):'.format(username, done_count, total))
    for t in done_tasks:
        print('\t {}'.format(t.get('title')))


if __name__ == '__main__':
    main()
