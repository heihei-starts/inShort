from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql

class AuthManageSql(ObjectManageSql):

    #ユーザー登録
    def insert_user(self, query, name, email, password):

        cursor = self.connection.cursor()

        #ユーザー登録
        try:
            cursor.execute(query, (name, email, password))
            
            self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            print("Exception error insert_user()")
            print(e)
        finally:
            cursor.close()

        return "register complete"


    #登録済みか確認
    def check_user(self, query, email, password):

        cursor = self.connection.cursor()

        try:
            cursor.execute(query, (email, password))

            result = cursor.fetchone()
        except Exception as e:
            print("Exception error check_user()")
            print(e)
        finally:
            cursor.close()

        return result
