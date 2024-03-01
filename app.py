from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
db = SQLAlchemy(app)


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/habits', methods=['GET'])
def get_habits():
    habits = Habit.query.all()
    habit_list = [{'id': habit.id, 'name': habit.name} for habit in habits]
    return jsonify({'habits': habit_list})


@app.route('/habits', methods=['POST'])
def create_habit():
    data = request.get_json()
    new_habit = Habit(name=data['name'])
    db.session.add(new_habit)
    db.session.commit()
    return jsonify({'message': 'Habit created successfully'})


@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    habit_id = data['habit_id']
    habit = Habit.query.get(habit_id)
    if habit:
        new_event = Event(habit_id=habit_id)
        db.session.add(new_event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully'})
    else:
        return jsonify({'message': 'Habit not found'}), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
