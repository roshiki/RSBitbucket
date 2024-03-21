import requests
import json
from requests.auth import HTTPBasicAuth
from models.BuildSummaries import BuildSummaries


class RSBitbucketApi:

    def __init__(self, user_slug, token, host):
        self.host = host
        self.httpBasic = HTTPBasicAuth(user_slug, token)

    def get_pr(self, project, repo, pull_request_id):
        url = f"{self.host}/rest/api/latest/projects/{project}/repos/{repo}/pull-requests/{pull_request_id}"
        response = requests.get(url, auth=self.httpBasic)
        json_data = json.loads(response.content)
        return json_data

    def get_ui_pr_builds(self, project, repo, pull_request_id):
        url = f"{self.host}/rest/ui/latest/projects/{project}/repos/{repo}/pull-requests/{pull_request_id}/builds?start=0&limit=25&avatarSize=48"
        response = requests.get(url, auth=self.httpBasic)
        json_data = json.loads(response.content)
        return json_data

    def get_pr_activities(self, project, repo, pull_request_id):
        url = f"{self.host}/rest/api/latest/projects/{project}/repos/{repo}/pull-requests/{pull_request_id}/activities?avatarSize=48&start=0&limit=25&markup=true"
        response = requests.get(url, auth=self.httpBasic)
        json_data = json.loads(response.content)
        return json_data['values']

    def get_pr_merge_info(self, project, repo, pull_request_id):
        url = f"{self.host}/rest/api/latest/projects/{project}/repos/{repo}/pull-requests/{pull_request_id}/merge"
        # log(url)
        response = requests.get(url, auth=self.httpBasic)
        json_data = json.loads(response.content)
        return json_data

    # TODO: функция pr_comments_post() или post_pr_comments()
    def post_test_pr(self, project, repo, pull_request_id):
        url = f"{self.host}/rest/api/latest/projects/{project}/repos/{repo}/pull-requests/{pull_request_id}/comments?diffType=EFFECTIVE&markup=true&avatarSize=48"
        json_data = {
            "text": "test pr",
            "severity": "NORMAL"
        }
        response = requests.post(url, auth=self.httpBasic, json=json_data)

    # TODO: функция get_pull_requests с параметрами
    def get_dashboard_prs(self, role: str, state: str, limit: int) -> dict:
        url = f"{self.host}/rest/api/latest/dashboard/pull-requests"
        params = {'role': role, 'state': state, 'limit': limit}
        response = requests.get(url, params=params, auth=self.httpBasic)
        json_data = json.loads(response.content)
        return json_data

    def get_ui_pr_build_summaries(self, project: str, repo: str, pull_request_id: int) -> BuildSummaries:
        url = f"{self.host}/rest/ui/latest/projects/{project}/repos/{repo}/pull-requests/{pull_request_id}/build-summaries"
        response = requests.get(url, auth=self.httpBasic)
        json_data = json.loads(response.content)
        try:
            return BuildSummaries.from_response(json_data)
        except Exception as err:
            print("TODO: EXCEPTION BuildSummaries. Todo logger")
            return BuildSummaries.empty()

    def get_pull_request(self, project: str, repo: str, state: str, at: str, limit: int):
        url = f"{self.host}/rest/api/latest/projects/{project}/repos/{repo}/pull-requests"
        params = {'state': state, 'at': at, 'limit': limit}
        response = requests.get(url, params=params, auth=self.httpBasic)
        json_data = json.loads(response.content)
        return json_data
