from flask import Flask, request, jsonify

from flask_cors import CORS
from dotenv import load_dotenv

import os
import sys
#modulesを呼び出すために、相対パスで呼び出せるようにする
sys.path.append(os.path.abspath(".."))

#modules呼び出し
from modules.wordManageSql import WordManageSql
#ステータスコード 
HTTP_OK = 200
HTTP_BAD_REQUEST = 400

app = Flask(__name__)

#CORS
CORS(app, origins=["http://localhost:8080"])

#単語取得API
@app.route("/", methods=['GET'])
def get_words():

    #sqlオブジェクト呼び出し
    sqlClass = WordManageSql()
    #全件取得
    try:
        query = "SELECT word_name,field_id from in_short.words; "
        result = sqlClass.selectAllWords(query)
        print(result)
        body = {'message': "全件取得完了", "words": result}
        return jsonify(body),HTTP_OK
    except Exception as e:
        print("Exception error get_words")
        print(e)

        #errorリターん

    finally:
        #コネクション接続解除
        
        sqlClass.closeConnection()
    


#単語追加API
@app.route("/", methods=['POST'])
def post_word():
    

    #wordManagesqlインスタンス呼び出し
    sqlClass = wordManageSql.WordManageSql()

    #リクエスト取得
    data = request.get_json(force=True)

    #リクエストデータ取り出す
    word_name = data.get('word_name', None)
    field_id  = data.get('field_id', None)

    #単語追加
    try:
        query = "INSERT INTO in_short.words (word_name, field_id) VALUES (%s,%s);"
        result = sqlClass.insert_word(word_name, field_id)

        body = {'message': '単語追加完了'}
        return jsonify(body), HTTP_OK

    except Exception as e:
        print("Exception error post_word")
        print(e)
    
    finally:
        #コネクション接続解除
        sqlClass.closeConnection()
            


if __name__ == "__main__":
    app.run(debug=True, port=5000)
