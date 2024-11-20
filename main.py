# app.py
from flask import Flask

from controllers.drivers import driver_blueprint
from controllers.trips import trip_blueprint
from controllers.users import user_blueprint

app = Flask(__name__)

# Register the user blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(driver_blueprint)
app.register_blueprint(trip_blueprint)


@app.route('/')
def index():
    return "Welcome to the Flask app with Blueprints!", 200


if __name__ == '__main__':
    app.run(debug=True)
