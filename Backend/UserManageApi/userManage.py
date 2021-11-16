from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.abspath(".."))

from modules.userManageSql import UserManageSql

app = Flask(__name__)

CORS(app, origins=["http://localhost:8080"])

HTTP_OK = 200
Created = 201
Bad_Request = 400
Unauthorized = 401
Internal_Server_Error = 500


@app.route("/", methods=[''])
def get_user_info():

    #リクエスト取得
    data = request.get_json(force=True)    
    #各データ取得
    user_id = data.get('user_id', None)
    
    #sqlオブジェクト呼び出し
    sqlClass = UserManageSql()
    
    try:
        result = sqlClass.getUserInfo(user_id)

        body = {'message': "ユーザー情報取得", 'user_info': result}

    except Exception as e:
        print("Exception error get_user_info")
        print(e)

    finally:
        sqlClass.closeConnection()
     
    return jsonify(body), HTTP_OK

if __name__ == "__main__":
    app.run(debug=True, port=5004)
