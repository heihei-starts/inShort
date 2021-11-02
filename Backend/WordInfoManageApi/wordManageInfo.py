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

#単語解説取得API
@app.route("/", methods=['GET'])
def get_words_info():
    
    #sqlオブジェクト呼び出し
    sqlClass = wordInfoManageSql.WordInfoManageSql()
    
    #単語と一致する解説全件取得
    try:
        query = "SELECT explanations, user_id from in_short.explanation where word_id = %s"

        result = sqlClass.get_words_info(query, word_id)

        body = {'message': "単語解説取得完了", "explanations": result}

    except Exception as e:
        print(Exception get_words_info)
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
    return jsonify(body), HTTP_OK

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
        query = "INSERT INTO in_short.explanation('explanations', 'word_id', 'user_id')"

        result = sqlClass.post_word_info(query, user_id, word_id, explanation)

        body = {"message": "解説追加完了"}
    except Exception as e:
        print("Exception error post_word_info")
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
    return jsonify(body), HTTP_OK
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
        query = "DELETE hogehoge"

        result = sqlClass.delete_word_info(query, explanation_id)

        body = {'message': '解説削除完了'}
    except Exception as e:
        print("Exception error delete_word_info")
        print(e)

    finally:
        sqlClass.closeConnection()

    #return
     return jsonify(body), HTTP_OK

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
        query = "UPDATE hogehgoe"
        result = sqlClass.update_word_info(query, change_explanation, explanation_id)

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

