from flask import Flask, request, jsonify

from flask_cors import CORS

from dotenv import load_dotenv

import os
import sys

sys.path.append(os.path.abspath(".."))
from modules.likeSql import LikeSql

app = Flask(__name__)

#CORS
CORS(app, origins=['http://locaohot:8080'])




#いいね追加
@app.route("/", methods=["POST"])
def add_like():

    #sqlオブジェクトを呼び出し
    sqlClass = LikeSql() 
    #リクエストを受ける
    data = request.get_json(force=True)
    #リクエストデータ分割
    #ユーザーID
    user_id = data.get('user_id', None)
    #解説ID
    explanation_id = data.get('explanation_id', None)
    
    #sql文を介して、DBにアクセス。いいね追加
    try:
        result = sqlClass.postLike(user_id, explanation_id)

        body = {'message': "いいね完了"}

    except Exception as e:

        print("Exception error addLike")
        print(e)

    finally:
        sqlClass.closeConnection()

    
    return jsonify(body), Created
    

#いいね取得
@app.route("/get", methods=["GET"])
def get_like():

    #sqlオブジェクト呼び出し
    sqlClass = LikeSql()

    #リクエストを受け取る
    data = request.get_json()
    #リクエストデータ分割
    #単語id
    word_id = data.get('word_id', None)
    #解説ID
    explanation_id = data.get('explanation_id', None)
    
    #いいね取得
    try:
        #countする

        result = sqlClass.getLike(word_id, explanation_id)

        body = {'message': "いいね取得", 'like': result}

    except Exception as e:
        print("Exception error getLike")
        print(e)

    finally:
        sqlClass.closeConnection()
    
    return jsonify(body), HTTP_OK 



@app.route("/delete", methods=["DELETE"])
def delete_like():
    
    #sqlオブジェクト呼び出し
    sqlClass = LikeSql()

    #リクエストを受ける
    data = request.get_json(force=True)
    #リクエストデータ分割
    #ユーザーID
    user_id = data.get('user_id', None)
    #解説ID
    explanation_id = data.get('explanation_id', None)
    
    #sql文を介して、DBにアクセス。いいね追加
    try:
        result = sqlClass.postLike(user_id, explanation_id)

        body = {'message': "いいね削除完了"}

    except Exception as e:

        print("Exception error delete_like")
        print(e)

    finally:
        sqlClass.closeConnection()

    
    return jsonify(body), HTTP_OK




if __name__ = "__main__":
    app.run(debug=True, port=5004)
