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


#単語削除API
@app.route("/")
def post_word_info():

    #wordManageInfoSQLオブジェクト呼び出し
    sqlClass = adminManageSql.AdmingManageSql()
    #リクエスト取得
    data = get_json(force=True)
    #リクエストデータ
    word_id = data.get('word_id', None)
    
    #単語削除
    try:
        query = "delete from in_short.words where word_name = %s; AND field_id = %s"

        result = sqlClass.delete_word(query, word_name, field_id)

        body = {'message': result}

        return jsonify(body), HTTP_OK
    
    except Exception as e:
        print("Exception error post_word_info")
        print(e)

    finally:
        #コネクション接続解除
        sqlClass.closeConnection()







#単語削除







if __name__ == "__main__":
    app.run(debug=True, port=5001)

