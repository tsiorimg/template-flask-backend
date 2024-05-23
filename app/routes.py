from flask import Blueprint, jsonify

main = Blueprint('main', __name__)


@main.route('/api/task', methods=['GET'])
def manage_tasks():
    return jsonify({"message": "Task endpoint"})
