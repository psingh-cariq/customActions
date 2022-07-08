#!/usr/bin/python3
import json
import os
import requests


def trigger_workflow(auth_token, git_sha, repo_name, env):
    dispatch_url = "https://api.github.com/repos/gocariq/devops/actions/workflows/{}Deployer.yaml/dispatches".format(env)
    payload = json.dumps({
        "ref": "main",
        "inputs": {
            "gitSha": "{}".format(git_sha),
            "gitRepo": "{}".format(repo_name),
        }
    })
    headers = {
        'Accept': 'application/vnd.github.everest-preview+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(auth_token)
    }
    response = requests.request("POST", dispatch_url, headers=headers, data=payload)
    assert response.status_code == 204, "Failed to trigger workflow\n Response code {}\n Error: {}".format(response.status_code, response.json())


def main():
    auth_token = os.environ['INPUT_TOKEN']
    repo_name = os.environ['INPUT_REPONAME']
    git_sha = os.environ['INPUT_GITSHA']
    env = os.environ['INPUT_ENVNAME']
    trigger_workflow(auth_token, git_sha, repo_name, env)


if __name__ == '__main__':
    main()
