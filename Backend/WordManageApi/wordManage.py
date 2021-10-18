from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

import os
import sys
#modulesを呼び出すために、相対パスで呼び出せるようにする
sys.path.append(os.path.abspath(".."))

#modules呼び出し
from modules import manageSql 


#ステータスコード 
HTTP_OK = 200
HTTP_BAD_REQUEST = 400

app = Flask(__name__)

#CORS
CORS(app, prigins=["http://localhost:8080"])

#単語取得API
@app.route("/", methods=['GET'])
def get_words():

    #sqlオブジェクト呼び出し
    sqlClass = manageSql.ManageSql()
    #全件取得
    try:
        query = "SELECT word_name,field_id from in_short.words; "
        result = sqlClass.selectAllWords(query)

        body = {'message': "全件取得完了", "words": result}

        return jsonify(body),HTTP_OK
    
    except Exception as e:
        print("Exception error get_words")
        print(e)

        #errorリターん

    finally:
        #コネクション接続解除
        sqlClass.closeConnection()
    


if __name__ == "__main__":
    app.run(debug=True, port=5000)
