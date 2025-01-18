from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance_manager.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(50), nullable=False)


class SavingsGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)


# Initialize the database
with app.app_context():
    db.create_all()


# Routes
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing required fields"}), 400
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400

    user = User(name=data["name"], email=data["email"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"], password=data["password"]).first()
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful", "user_id": user.id}), 200


@app.route("/transactions", methods=["POST"])
def add_transaction():
    data = request.json
    transaction = Transaction(
        user_id=data["user_id"],
        amount=data["amount"],
        date=datetime.strptime(data["date"], "%Y-%m-%d"),
        category=data["category"],
        description=data.get("description"),
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"}), 201


@app.route("/transactions/<int:user_id>", methods=["GET"])
def get_transactions(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    return (
        jsonify(
            [
                {
                    "id": t.id,
                    "amount": t.amount,
                    "date": t.date.strftime("%Y-%m-%d"),
                    "category": t.category,
                    "description": t.description,
                }
                for t in transactions
            ]
        ),
        200,
    )


@app.route("/categories", methods=["POST"])
def add_category():
    data = request.json
    category = Category(user_id=data["user_id"], name=data["name"])
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category added successfully"}), 201


@app.route("/categories/<int:user_id>", methods=["GET"])
def get_categories(user_id):
    categories = Category.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": c.id, "name": c.name} for c in categories]), 200


@app.route("/savings", methods=["POST"])
def add_savings_goal():
    data = request.json
    savings_goal = SavingsGoal(
        user_id=data["user_id"],
        target_amount=data["target_amount"],
        target_date=datetime.strptime(data["target_date"], "%Y-%m-%d"),
    )
    db.session.add(savings_goal)
    db.session.commit()
    return jsonify({"message": "Savings goal added successfully"}), 201


@app.route("/savings/<int:user_id>", methods=["GET"])
def get_savings_goal(user_id):
    savings_goals = SavingsGoal.query.filter_by(user_id=user_id).all()
    return (
        jsonify(
            [
                {
                    "id": sg.id,
                    "target_amount": sg.target_amount,
                    "target_date": sg.target_date.strftime("%Y-%m-%d"),
                }
                for sg in savings_goals
            ]
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
