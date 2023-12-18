import requests


def get_csv_files(username,repo_name,subfolder_path):
    api_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{subfolder_path}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        csv_files = [file['name'] for file in data if file['name'].endswith('.csv')]
        return csv_files
    else:
        print(f"Error: {response.status_code}")
        return None

def get_json_files(username,repo_name,subfolder_path):
    api_url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{subfolder_path}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        json_files = [file['name'] for file in data if file['name'].endswith('.json')]
        return json_files
    else:
        print(f"Error: {response.status_code}")
        return None