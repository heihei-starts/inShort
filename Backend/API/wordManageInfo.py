from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import sys

sys.path.append(os.path.abspath(".."))

from modules import wordInfoManageSql
#解説情報追加
#投稿者の投稿に限り、削除
#変更


app = Flask(__name__)

#CORS
CORS(app, origins=["http://localhost:8080"])

HTTP_OK = 200
Created = 201
Bad_Request = 400
Unauthorized = 401
Internal_Server_Error = 500

#単語解説取得API
@app.route("/", methods=['POST'])
def get_words_info():
    
    data = request.get_json(force=True)
    word_id = data.get('word_id', None)

    print(word_id)
    #sqlオブジェクト呼び出し
    sqlClass = wordInfoManageSql.WordInfoManageSql()
    
    #単語と一致する解説全件取得
    try:
        result = sqlClass.get_words_info(word_id)

        print(result)

        body = {'message': "単語解説取得完了", "explanations": result}

    except Exception as e:
        print("Exception get_words_info")
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
    return jsonify(body),HTTP_OK 

#単語解説追加
@app.route("/", methods=['POST'])
def post_word_info():

    #リクエストを受ける
    data = request.get_json(force=True)

    #リクエストデータ取り出し
    explanation = data.get('explanation', None)
    word_id     = data.get('word_id', None)
    user_id     = data.get('user_id', None)

    #sqlオブジェクト呼び出し
    sqlClass= wordInfoManageSql.WordInfoManageSql()

    #解説追加
    try:

        result = sqlClass.post_word_info(user_id, word_id, explanation)

        body = {"message": "解説追加完了"}
    except Exception as e:
        print("Exception error post_word_info")
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
    return jsonify(body),Created

#単語解説削除
@app.route("/", methods=['DELETE'])
def delete_word_info():

    #リクエストを受ける
    data = request.get_json(force=True)

    #リクエストデータ取り出し
    explanation_id = data.get('explanation_id',None)

    #sqlオブジェクト呼び出し
    sqlClass= wordInfoManageSql.WordInfoManageSql()

    #解説削除
    try:
        query = "DELETE FROM in_short.explanation where id = %s"

        result = sqlClass.delete_word_info(explanation_id)

        body = {'message': '解説削除完了'}
    except Exception as e:
        print("Exception error delete_word_info")
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
    return jsonify(body),HTTP_OK 

#単語解説改稿
@app.route("/", methods=['PUT'])
def update_word_info():

    #sqlオブジェクト呼び出し
    sqlClass= wordInfoManageSql.WordInfoManageSql()

    #リクエストを受ける
    data = request.get_json(force=True)

    #リクエストデータ取りだあし
    change_explanation = data.get("change_explanation", None)
    explanation_id     = data.get("explanation_id", None)

    #解説改稿
    try:
        result = sqlClass.update_word_info(change_explanation, explanation_id)

        body = {'message': '解説改稿完了'}
    except Exception as e:
        print("Exception error update_word_info")
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
    return jsonify(body), HTTP_OK


if __name__ == "__main__":
    app.run(debug=True, port=5001)

