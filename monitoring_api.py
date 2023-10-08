from flask import Flask, jsonify

app = Flask(__name__)

# Mock database of agent statuses
agent_statuses = {
    '1': {'health': 'good', 'update_required': False},
    '2': {'health': 'bad', 'update_required': True},
    '3': {'health': 'good', 'update_required': True},
}

@app.route('/agents/<agent_id>/status', methods=['GET'])
def get_agent_status(agent_id):
    status = agent_statuses.get(agent_id, None)
    if status:
        return jsonify(status)
    else:
        return jsonify({'error': 'Agent not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

