from flask import Blueprint, request, jsonify
from app.models import create_user, get_user

main = Blueprint('main', __name__)

@main.route('/favicon.ico')
def favicon():
    return '', 204  # No Content response


# Add a route for the root URL ("/")
@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Food and Clothes Ordering System!"})


@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = get_user(username)
    if user:
        return jsonify({'message': 'User already exists'}), 400
    
    create_user(username, password)
    return jsonify({'message': 'User created successfully'}), 201
