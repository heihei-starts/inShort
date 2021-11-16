from flask import Flask, request, jsonify

from flask_cors import CORS
from dotenv     import load_dotenv

import os
import sys

sys.path.append(os.path.obspath(".."))

#module呼び出し
from modules import adminManageSql


app = Flask(__name__)

CORS(app, origins=["http://localhost:8080"])

#ステータスコード 
#リクエストが成功
HTTP_OK = 200
#リクエストが成功し、その結果新たなリソースが作成された
Created = 201
#構文が、無効。サーバーがリクエストを理解できない
Bad_Request = 400
#認証が必要
Unauthorized = 401
#サーバー側で、処理方法がわからない事態
Internal_Server_Error = 500
#


#単語削除API
@app.route("/")
def delete_word_info():

    #wordManageInfoSQLオブジェクト呼び出し
    sqlClass = adminManageSql.AdmingManageSql()
    #リクエスト取得
    data = get_json(force=True)
    #リクエストデータ
    word_id = data.get('word_id', None)
    
    #単語削除
    try:

        result = sqlClass.delete_word(word_name, field_id)

        body = {'message': result}

        return jsonify(body), HTTP_OK
    
    except Exception as e:
        print("Exception error delete_word_info")
        print(e)

    finally:
        #コネクション接続解除
        sqlClass.closeConnection()








#単語削除







if __name__ == "__main__":
    app.run(debug=True, port=5003)

