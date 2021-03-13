import requests
import re
import json

TOKEN = 'token is hidden'
USER = 'ooooda'
REPOSITORY = 'python_au'


def get_header():
    headers = {'Authorization': 'token ' + TOKEN}
    return headers


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
    for commit in commits:
        commit_checker(commit['commit']['message'], pull)


def commit_checker(commit, pull):
    part1 = commit.split(" ")[0]
    print(part1)
    part2 = "".join(commit.split(" ")[1:])
    if not re.match(r"(Added |Deleted |Fixed )[^A-Z]*", commit):
        message = "wrong commit format"
        if not re.match(r"(Added|Deleted|Fixed)", part1):
            print('!!!' + part1)
            message += ', wrong action name'
        if not re.match(r"([^A-Z]*)", part2):
            message += ', wrong letters format'
        send_message(pull, message)
        print(commit + '- ' + message)


def pull_checker(pull):
    part1 = pull['title'].split('-')[0]
    part2 = "".join(pull['title'].split('-')[1:])
    if not re.match(r"(HW[0-4]|LEETCODE)-1021", pull['title']):
        message = "wrong pull request format"
        if not re.match(r"(HW[0-4]|LEETCODE)", part1):
            message += ', wrong title name'
        if not re.match(r"1021", part2):
            message += ', wrong group number format'
        send_message(pull, message)
        print(pull['title'] + '- ' + message)


def send_message(pull, message):
    body = {'body': message}
    response = requests.post(get_prefix() + '/issues/' + str(pull['number']) + '/comments', headers=get_header(),
                             data=json.dumps(body))
    if response.status_code != 201:
        print(response)


check_all_pulls(state='all')