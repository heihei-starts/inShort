from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql

class UserManageSql(ObjectManageSql):

    #ユーザー名、過去投稿取得
    def getUserPosted(self, user_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        query = 'SELECT e.explanations '\
                'FROM in_short.users u '\
                'INNER JOIN in_short.explanation e '\
                'ON u.id = e.user_id '\
                'WHERE u.id =  %s;'

        #ユーザー名、過去投稿取得
        try:
            cursor.execute(query, (user_id))

            #値取り出し
            result = cursor.fetchall()

        except Exception as e:
            print("Exception error getUserInffo()")
            print(e)
        finally:
            cursor.close()

        return result

    #ユーザー名と、user_id(tokenから)
    def getuserInfo(self,email):
        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        query = 'SELECT id, user_name FROM in_short.users WHERE email = %s;'

        #ユーザー名、過去投稿取得
        try:
            cursor.execute(query, (email))

            #値取り出し
            result = cursor.fetchone()

        except Exception as e:
            print("Exception error getUserInfo()")
            print(e)
        finally:
            cursor.close()

        return result

