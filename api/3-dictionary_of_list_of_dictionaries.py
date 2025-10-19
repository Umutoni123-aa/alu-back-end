#!/usr/bin/python3

import json
import requests


def main():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_resp = requests.get(users_url)
    todos_resp = requests.get(todos_url)
    if users_resp.status_code != 200 or todos_resp.status_code != 200:
        return

    users = users_resp.json()
    todos = todos_resp.json()

    # build a map userId -> username
    user_map = {u.get('id'): u.get('username') for u in users}

    result = {}
    for t in todos:
        uid = t.get('userId')
        entry = {
            'username': user_map.get(uid),
            'task': t.get('title'),
            'completed': t.get('completed')
        }
        result.setdefault(str(uid), []).append(entry)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(result, f)


if __name__ == '__main__':
    main()
