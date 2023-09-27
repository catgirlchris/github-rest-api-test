import requests

# Replace with your GitHub username and repository name
username = 'catgirlchris'
repo_name = 'text-adventure'

# Set up the URL for the GitHub API
api_url = f'https://api.github.com/repos/{username}/{repo_name}/branches'

# Make a GET request to the GitHub API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    branches_info = response.json()
    
    # Access the information you need
    for branch in branches_info:
        for key, value in branch.items():
            print(f"--> {key}: {value}")
            print()

        branch_name = branch['name']
        api_url = f"https://api.github.com/repos/{username}/{repo_name}/commits?sha={branch_name}"
        response = requests.get(api_url)
        if response.status_code == 200:
            commits_info = response.json()
            for commit in commits_info:
                print("----> " + commit['name'])

else:
    print(f"Failed to retrieve repository info. Status code: {response.status_code}")

print()
print()

# Set up the URL for the GitHub API
api_url = f'https://api.github.com/users/{username}'

# Make a GET request to the GitHub API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    user_info = response.json()
    
    # Access the information you need
    for key, value in user_info.items():
        print(f"{key}: {value}")
else:
    print(f"Failed to retrieve repository info. Status code: {response.status_code}")

