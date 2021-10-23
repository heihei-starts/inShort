from flask import Flask, jsonify

#ローカル上で、githubにあげないものの管理
from dotenv import load_dotenv
import os

import pymysql

load_dotenv()

class AdmingManageSql(object):


    #コンストラクタ
    def __init__(self):
        self.host       = os.getenv('HOST')
        self.port       = int(os.getenv('PORT'))
        self.user       = os.getenv('USE')
        self.password   = os.getenv('PASS')
        self.db         = os.getenv('DB')

        #インスタンス呼び出し時に、mysql接続
        self.connection = pymysql.connect(
            host     = self.host,
            port     = self.port,
            user     = self.user,
            password = self.password,
            db       = self.db)

    #単語削除(admin)
    def delete_word(self, query, word_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        #単語削除
        try:
            cursor.execute(query,(word_id))
            self.connection.commit()
        except Exception as e:
            print("Exception error delete_word()")
            print(e)

        finally:
            cursor.close()

        return "delete select"

    #接続解除
    def closeConnection(self):
        self.connection.close()
