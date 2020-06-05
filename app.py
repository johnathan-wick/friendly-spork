from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/one')
def get_user_list():
    data = {
        "username": "user_1",
        "password": "password_1"
    }
    return json.dumps(data, indent=4)


@app.route('/two', methods=['GET'])
def get_user_id_by_name():
    u_name = request.args.get('username')
    if u_name:
        data = {
            "username": u_name,
            "userInfo": {
                "id": 15
            }
        }
    else:
        data = {
            "msg": "Need to input username as params"
        }
    return json.dumps(data, indent=4)


@app.route('/three', methods=['POST'])
def user_login():
    request_data = json.loads(request.get_data())

    u_name = request_data.get("username")
    u_pwd = request_data.get("password")

    if u_name and u_pwd:
        data = {
            "msg": "Login Success"
        }
    else:
        data = {
            "msg": "Failed to login"
        }
    return json.dumps(data, indent=4)

@app.route('/four')
def warp_a_file():
    return app.send_static_file('expected_result.json')


@app.route('/<name>')
def warp_a_variable(name):
    return "Hello, " + name

    
if __name__ == "__main__":
    app.run()
