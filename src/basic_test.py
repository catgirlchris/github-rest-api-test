import requests


def send_request(api_url):
    # Make a GET request to the GitHub API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and return it
        return response.json()
    else:
        print(f"Failed to retrieve repository info. Status code: {response.status_code}")
        return None


def get_user(username):
    api_url = f'https://api.github.com/users/{username}'
    return send_request(api_url)


def get_branches(username, repo_name):
    api_url = f'https://api.github.com/repos/{username}/{repo_name}/branches'
    return send_request(api_url)


def main():
    # Replace with your GitHub username and repository name
    username = 'catgirlchris'
    repo_name = 'text-adventure'

    # Get user info
    user_info = get_user(username)
    print(f"### user {username} info ###")
    for key, value in user_info.items():
        print(f"--> {key}: {value}")

    print()

    branches_info = get_branches(username, repo_name)
    print(f"### Repository {repo_name}@{username} branches ###")
    # Access the information you need
    for branch in branches_info:
        print(f"### Branch {branch['name']} ###")
        for key, value in branch.items():
            print(f"--> {key}: {value}")

        branch_name = branch['name']
        api_url = f"https://api.github.com/repos/{username}/{repo_name}/commits?sha={branch_name}"
        response = requests.get(api_url)
        if response.status_code == 200:
            commits_info = response.json()
            for commit in commits_info:
                print("----> " + commit['sha'])
        print()


if __name__ == "__main__":
    main()