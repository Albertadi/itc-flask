from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dataclasses import dataclass

app = Flask(__name__)
# Configuration for SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.app_context().push()

@dataclass
class Todo(db.Model):
    # Dataclass fields for easier serialization
    id: int
    title: str
    createdAt: object
    updatedAt: object
    description: str
    completed: bool

    # SQLAlchemy model definition
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/todos', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        # Extract data from the incoming POST request
        task_title = request.json['title']
        task_description = request.json['description']
        
        # Create a new Todo instance
        new_task = Todo(title=task_title, description=task_description)

        try:
            # Add the new task to the database and commit the session
            db.session.add(new_task)
            db.session.commit()
            # Return the ID of the new task as a response
            return {'id': new_task.id}
        except:
            # Handle exceptions during database operations
            return 'There was an issue adding your task'
    else:
        # Retrieve and return all tasks in JSON format
        tasks = Todo.query.order_by(Todo.createdAt).all()
        return jsonify(tasks)

@app.route('/todos/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def todo(id):
    # Retrieve a specific task by ID or return 404 if not found
    task = Todo.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify(task)
    
    elif request.method == 'DELETE':
        try:
            # Delete the task and commit the changes
            db.session.delete(task)
            db.session.commit()
            return 'Task deleted'
        except:
            # Handle exceptions during deletion
            return 'There was a problem deleting that task'
        
    elif request.method == 'PUT':
        # Update the task attributes from the request data
        task.title = request.json['title']
        task.description = request.json['description']
        task.completed = 'completed' in request.json
        task.updatedAt = datetime.now()
        try:
            # Commit the changes to the database
            db.session.commit()
            return 'Task updated successfully'
        except:
            # Handle exceptions during update
            return 'There was an issue updating your task'

if __name__ == '__main__':
    app.run(debug=True)
