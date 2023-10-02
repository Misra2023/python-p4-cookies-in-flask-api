from flask import Flask, request, session, jsonify, make_response, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.json.compact = False

app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Dummy User Model (Replace with your actual user model if using a database)
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


# Dummy user data (Replace with your user data)
users = {'user1': 'password1', 'user2': 'password2'}

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        user = User(username)
        login_user(user)
        return redirect(url_for('dashboard'))
    else:
        return 'Login failed. Invalid credentials.'


# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully.'


# Dashboard route (requires login)
@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.id}! You are logged in.'


if __name__ == '__main__':
    app.run(port=5555)
