from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (acts like a simple database)
todos = []
counter = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    global counter
    data = request.get_json()
    todo = {"id": counter, "task": data["task"]}
    todos.append(todo)
    counter += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)