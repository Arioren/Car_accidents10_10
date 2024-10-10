from flask import Flask

from controller.end_points import end_points


app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(end_points, url_prefix="/api")
    app.run(debug=True)