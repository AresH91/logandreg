from flask_app import app
from flask_app.controllers.users import User

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
