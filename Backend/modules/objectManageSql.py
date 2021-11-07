#ローカる状で、githubにあげないものの管理
from dotenv import load_dotenv
import os
#--------------------
import pymysql

load_dotenv()

class ObjectManageSql(object):
    
    #コンストラクタ
    def __init__(self):
        #__で、外部から書き換えも呼び出しもされなくなる。
        self.__host       = os.getenv('HOST')
        self.__port       = int(os.getenv('PORT'))
        self.__user       = os.getenv('USE')
        self.__password   = os.getenv('PASS')
        self.__db         = os.getenv('DB')
        self._connection = pymysql.connect(
           host     = self.__host,
           port     = self.__port,
           user     = self.__user,
           password = self.__password,
           db       = self.__db,
           cursorclass=pymysql.cursors.DictCursor)

    

    @property
    def connection(self):
       return self._connection

    #接続解除
    def closeConnection(self):
        self.connection.close()
