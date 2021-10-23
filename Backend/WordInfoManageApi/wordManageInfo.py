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

        return jsonify(body), HTTP_OK
    except Exception as e:
        print(Exception get_words_info)
        print(e)

    finally:
        sqlClass.closeConnection()
