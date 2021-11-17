##モジュール呼び出し---------------------------------
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import timedelta
import os
import sys

from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    JWTManager,
    get_jwt_identity
)

#modulesを呼び出すために、相対パスで呼び出せるようにする$
sys.path.append(os.path.abspath(".."))

#modules呼び出し
from modules import authManageSql

#####-----------------------------------------
####------------------------------------------

##-初期設定-------------------------------
app = Flask(__name__)
print(os.getenv('JWT_SECRET_KEY'))
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
#CORS
CORS(app, origins=["http://localhost:8080"])


def jwt_unauthorized_loader_handler(reason):
    return jsonify({'message': 'Unauthorized'}), 401


#token

jwt = JWTManager(app)
jwt.unauthorized_loader(jwt_unauthorized_loader_handler)

####------------------------------------------------------
###-------------------------------------------------------

#登録api
@app.route("/register", methods=['POST'])
def register():
    sqlClass = authManageSql.AuthManageSql() 
    #リクエストを受ける
    data = request.get_json(force=True)
    #リクエストデータを取り出す。
    name = data.get('name', None)
    email = data.get('email', None)
    password = data.get('password', None)

    

    #DBに登録済みではないか確認
    try:
        query1 = "SELECT user_name from in_short.users where email = %s and pass = %s"
        result = sqlClass.check_user(query1, email, password)
       #登録済みであれば、401。登録済みでなければ、dbに登録
        if result is None:
            query2 = "INSERT INTO in_short.users(user_name, email, pass) values (%s,%s,%s)"

            register_success = sqlClass.insert_user(query2, name, email, password)

        
        else:
            body = {'message': "すでに登録済みです。"}

            return jsonify(body), 400
            

    except Exception as e:
        print("Exception error register")
        print(e)
    
    finally:
        sqlClass.closeConnection()

    
    #return
    body = {'message': "登録成功"}
    return jsonify(body), 200

    #sessionにデータ格納
#ログインapi
@app.route("/login", methods=['POST'])
def login():
    
    #リクエストデータを受け取る
    data = request.get_json(force=True)
    password = data.get('password', None)
    email   = data.get('email', None)    
    
    if password is None or email is None:
        body = {'message': "正しくないログインです。。"}
        return jsonify(body, 401)

    print(password, email)
        
    #リクエストデータがない時
    if not password:
        body = {'message': "正しく入力してください。"}
        return jsonify(body)
   
    #sqlオブジェクト呼び出し
    sqlClass = authManageSql.AuthManageSql() 
    #ログイン
    try:
        query = "SELECT user_name  from in_short.users where email= %s and pass = %s" 
        print(query)
        result = sqlClass.check_user(query, email, password)
        print(result)
    except Exception as e:
        print("Exception error login")
        print(e)
    finally:
        sqlClass.closeConnection()

    #resultに値がない時
    if result is None:
        body = {'message': '登録されていません。'}
        return jsonify(body), 401

    #token作成
    token = create_access_token(identity=email)

    print(token)
    
    #return
    body = {'message': "ログイン成功", 'token': token}
    return jsonify(body), 200




if __name__ == '__main__':
    app.run(debug=True, port=5002)
