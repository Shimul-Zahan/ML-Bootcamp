# put and delete here
# working with API's json
# create a toto list using flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# create a initial data for thsi project

todoList= [
    {
      "id": 1,
      "task": "Complete AI assignment",
      "dueDate": "2025-01-20",
      "status": "pending"
    },
    {
      "id": 2,
      "task": "Prepare for DSP exam",
      "dueDate": "2025-01-28",
      "status": "pending"
    },
    {
      "id": 3,
      "task": "Study DSA algorithms",
      "dueDate": "2025-01-25",
      "status": "in-progress"
    },
    {
      "id": 4,
      "task": "Finish Linked List problems",
      "dueDate": "2025-01-22",
      "status": "completed"
    }
]

# show all item
@app.route("/", methods=['GET'])
def home():
    return jsonify(todoList)

# get item by id
@app.route("/get_item/<int:id>", methods=['GET'])
def get_element_by_id(id):
    # for list in todoList:
    #     if list["id"] == id:
    #         return jsonify(list)
    item = next((list for list in todoList if list["id"] == id), None)
    if not item:
        return jsonify({"message" : "item not found"})
    else:
        return item


# post
@app.route("/add", methods=['POST'])
def create_todo():
    if not request.json:
        return jsonify({"message" : "please make a valid request"})
    else:
        list = {
            "id" : todoList[-1]["id"] + 1 if todoList else 1,
            "task": request.json['task'],
            "dueDate": request.json['dueDate'],
            "status": request.json['status']
        }
        todoList.append(list)
        return jsonify(todoList)
    
    
# put method or update methods
@app.route("/update/<int:id>", methods=['PUT'])
def update(id):
    if not id:
        return jsonify({"message" : "give a valid id"})
    else:
        item = next((list for list in todoList if list["id"]==id), None)
        if not item:
            return jsonify({"message" : "item not found"})
        else:
            item["task"] = request.json.get('task', item['task'])
            item["dueDate"] = request.json.get('dueDate', item['dueDate'])
            item["status"] = request.json.get('status', item['status'])
            return jsonify(item)
        
        
# delete method
@app.route("/delete/<int:id>", methods=['DELETE'])
def delete(id):
    if not id:
        return jsonify({"message" : "give a valid id"})
    items = [item for item in todoList if item["id"] != id]
    return jsonify(items)

if __name__=='__main__':
    app.run(debug=True)