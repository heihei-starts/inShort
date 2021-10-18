from flask import Flask, jsonify

#ローカル上で、githubにあげないものの管理----
from dotenv import load_dotenv
import os
#------------

import pymysql

load_dotenv()

class ManageSql(object):

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

    
    #単語取得
    def selectAllWords(self, query):
        
        #カーソルオブジェクト(DBを管理するオブジェクト) 呼び出し
        cursor  = self.connection.cursor()

        #全件取得
        try:
            cursor.execute(sql)
            #値取り出し
            result = cursor.fetchall()

        except Exception as e:
            print("Exception error selectAllWords()")
            print(e)

        finally:
            cursor.close()

        return result
        


    #接続解除
    def closeConnection(self):
        self.connection.close()
