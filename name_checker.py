import requests
import re
import json

TOKEN = 'token is hidden'
USER = 'ooooda'
REPOSITORY = 'python_au'

def get_header():
    return {'Authorization': 'token ' + TOKEN}

def get_prefix():
    return 'https://api.github.com/repos/' + USER + '/' + REPOSITORY

def check_all_pulls(state):
    response = requests.get(get_prefix() + '/pulls?state=' + state, headers=get_header())
    pulls = response.json()
    if response.status_code != 200:
        raise ValueError(pulls)
    for pull in pulls:
        pull_checker(pull)
        commits = requests.get(
            get_prefix() + '/pulls/' + str(pull['number']) + '/commits', headers=get_header())
        check_all_commits(commits, pull)


def check_all_commits(response, pull):
    commits = response.json()
    if response.status_code != 200:
        raise ValueError(commits)
    comments = requests.get(get_prefix() + '/issues/' + str(pull['number']) + '/comments', headers=get_header()).json()
    comment_time = None
    if len(comments) != 0:
        comment_time = comments[-1]['created_at']
    for commit in commits:
        if comment_time is not None:
            if comment_time >= commit['commit']['author']['date']:
                continue
        commit_checker(commit['commit']['message'], pull)


def commit_checker(commit, pull):
    has_mistake = False
    message = "wrong commit format"
    name = pull['title']
    if '-' not in name:
        send_message(pull, message)
        print(name + ' - ' + message)
        return
    name = name.split('-', maxsplit=1)
    task_name = name[0]
    group_number = name[1]
    if not re.match(r"(HW[0-4]|LEETCODE)", task_name):
        message += ", wrong task name"
        has_mistake = True
    if not re.match(r"1021", group_number):
        message += ", wrong group number"
        has_mistake = True
    if has_mistake:
        send_message(pull, message)
        print(pull['title'] + ' - ' + message)

def pull_checker(pull):
    has_mistake = False
    message = "wrong pull request format"
    name = pull['title']
    if '-' not in name:
        print('happened', name)
        send_message(pull, message)
        print(name + ' - ' + message)
        return
    name = name.split('-', maxsplit=1)
    task_name = name[0]
    group_number = name[1]
    if not re.match(r"(HW[0-4]|LEETCODE)", task_name):
        message += ", wrong task name"
        has_mistake = True
    if not re.match(r"1021", group_number):
        message += ", wrong group number"
        has_mistake = True
    if has_mistake:
        send_message(pull, message)
        print(pull['title'] + ' - ' + message)

def send_message(pull, message):
    body = {'body': message}
    response = requests.post(get_prefix() + '/issues/' + str(pull['number']) + '/comments', headers=get_header(), data=json.dumps(body))
    if response.status_code != 201:
        print(response)

check_all_pulls(state='all')