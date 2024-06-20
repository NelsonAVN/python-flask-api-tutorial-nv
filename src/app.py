from flask import Flask, request, jsonify
app = Flask(__name__)

todos=[ { "label": "My first task", "done": False } ]
@app.route('/todos', methods=['GET'])
def get_todos():
  return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    todos.append(request_body)

    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    # Verificar que la posición es válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400

    # Eliminar la tarea de la lista de todos
    todos.pop(position)
    
    # Devolver la lista actualizada todos en formato JSON
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

   
    
