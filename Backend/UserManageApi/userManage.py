from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import sys

from flask_jwt_extended import (
        jwt_required,
        create_access_token,
        JWTManager,
        get_jwt_identity
)
sys.path.append(os.path.abspath(".."))

from modules.userManageSql import UserManageSql

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
CORS(app, origins=["http://localhost:8080"])

HTTP_OK = 200
Created = 201
Bad_Request = 400
Unauthorized = 401
Internal_Server_Error = 500
def jwt_unauthorized_loader_handler(reason):
    return jsonify({'message': 'Unauthorized'}), Unauthorized

jwt = JWTManager(app)
jwt.unauthorized_loader(jwt_unauthorized_loader_handler)
#ログイン済みか
#tokenから、email取り出し
@app.route("/get", methods=['GET'])
@jwt_required()
def get_user_info():

    #ログインユーザーのemail取り出し
    current_user_email = get_jwt_identity()
    print(current_user_email)
    sqlClass = UserManageSql()
    try:
        result = sqlClass.getuserInfo(current_user_email)
        print(result)
        user_id = result['id']
        user_name = result['user_name']
        print(user_id, user_name)
        body = {'message': 'ログインユーザー取得', 'user_id': user_id, 'user_name': user_name}

    except Exception as e:
        print("Exception error get_user_info")
        print(e)
    finally:
        sqlClass.closeConnection()

    return jsonify(body), HTTP_OK

@app.route("/", methods=['POST'])
def get_user_posted():

    #リクエスト取得
    data = request.get_json(force=True)    
    #各データ取得
    user_id = data.get('user_id', None)
    
    #sqlオブジェクト呼び出し
    sqlClass = UserManageSql()
    
    try:
        result = sqlClass.getUserPosted(user_id)

        body = {'message': "ユーザー情報取得", 'user_info': result}

    except Exception as e:
        print("Exception error get_user_info")
        print(e)

    finally:
        sqlClass.closeConnection()
     
    return jsonify(body), HTTP_OK

if __name__ == "__main__":
    app.run(debug=True, port=5004)
