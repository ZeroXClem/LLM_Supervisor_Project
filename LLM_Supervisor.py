import time
import json
import logging
import csv
from api_monitoring import APIMonitor

logging.basicConfig(filename='agent_status.log', level=logging.INFO)

class LLM_Supervisor:

    def __init__(self, config_file):
        self.api_monitor = APIMonitor("http://127.0.0.1:5000")
        self.agents = []
        self.load_config(config_file)
        self.monitoring_interval = 5  # seconds
    
    def load_config(self, config_file):
        # Assuming the config file is a JSON file
        with open(config_file, 'r') as f:
            config = json.load(f)
        self.agents = config['agents']
    
    def initialize_agents(self):
        for agent in self.agents:
            # Here, normally, you'd send an API request to initialize the agent
            # For the sake of this example, let's just print a message
            print(f"Initializing agent {agent['id']}")
    
    def evaluate_agent_status(self, status):
        action = 'none'
        if status['health'] == 'bad':
            action = 'restart'
        elif status['update_required']:
            action = 'update'
        return action

    def take_action(self, agent, action):
        # Here, normally, you'd send an API request to perform the action on the agent
        # For the sake of this example, let's just print a message
        print(f"Performing {action} on agent {agent['id']}")
    
    def log_status(self, agent, status, action):
        log_message = f"Agent ID: {agent['id']}, Status: {status}, Action: {action}"
        logging.info(log_message)
        
        with open('agent_status_report.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([agent['id'], status, action])
    
    def monitor_agents(self):
        self.initialize_agents()
        while True:
            for agent in self.agents:
                status = self.api_monitor.fetch_agent_status(agent['id'])
                action = self.evaluate_agent_status(status)
                self.take_action(agent, action)
                self.log_status(agent, status, action)
                
            time.sleep(self.monitoring_interval)

# Initialize supervisor with config file
supervisor = LLM_Supervisor('config.json')
supervisor.monitor_agents()

