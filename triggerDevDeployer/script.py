#!/usr/bin/python3
import json
import os

import requests


def trigger_workflow(auth_token, git_sha, repo_name):
    dispatch_url = "https://api.github.com/repos/gocariq/devops/actions/workflows/devDeployer.yaml/dispatches"
    payload = json.dumps({
        "ref": "main",
        "inputs": {
            "gitSha": "{}".format(git_sha),
            "codeRepo": "{}".format(repo_name),
        }
    })
    headers = {
        'Accept': 'application/vnd.github.everest-preview+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(auth_token)
    }
    response = requests.request("POST", dispatch_url, headers=headers, data=payload)
    assert response.status_code == 204


def main():
    auth_token = os.environ['INPUT_AUTH_TOKEN']
    repo_name = os.environ['INPUT_REPO_NAME']
    auth_token = os.environ['INPUT_GIT_SHA']


if __name__ == '__main__':
    main()
