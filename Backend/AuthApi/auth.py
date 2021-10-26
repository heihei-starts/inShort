from flask import Flask, request, jsonify, session
from flask_cors import CORS
from dotenv import load_dotenv
import os
import sys$
#modulesを呼び出すために、相対パスで呼び出せるようにする$
sys.path.append(os.path.abspath(".."))

#modules呼び出し
from modules.authManageSql import AuthManageSql
app = Flask(__name__)

#C  ORS
CORS(app, origins=["http://localhost:8080"])

#登録api
@app.route("/register", methods=['POST'])
def register():
    sqlClass = AuthManageSql()
    #リクエストを受ける
    data = request.get_json(force=True)
    #リクエストデータを取り出す。
    name = data.get('name'. None)
    email = data.get('email, None')
    password = data.get('password', None)


    #DBに登録済みではないか確認
    try:
        query1 = "SELECT name  from in_short.users where email = %s and password = %s"
        result = sqlClass.check_user(query1, (email, password))
    #登録済みであれば、401。登録済みでなければ、dbに登録
       if result is None:
            query2 = "INSERT INTO in_short.users('user_name', email, pass)"

            goal = sqlClass.insert_user(query2, (name, email, password))
            #sessionにユーザー情報を格納
            session["user_name"] = name
            
            
        
        else:
            body = {'message': "すでに登録済みです。"}

            return jsonify(body, 400)
            
        #return
        return name     

    except Exception as e:
        print("Exception error register")
        print(e)
    
    finally:
        sqlClass.closeConnection()

    #sessionにデータ格納
#ログインapi
@app.route("/login", methods=['POST'])
def login():
    print("login")

@app.route("/logout", methods=['POST'])
def loguot():
    print("logout")
