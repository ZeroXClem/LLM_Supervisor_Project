import requests
import json

class APIMonitor:

    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_agent_status(self, agent_id):
        endpoint = f"{self.api_url}/agents/{agent_id}/status"
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error fetching status for agent {agent_id}: {response.status_code}")
            return None

