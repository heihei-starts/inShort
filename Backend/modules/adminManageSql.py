from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql
#ローカル上で、githubにあげないものの管理

class AdminManageSql(ObjectManageSql):


    #単語削除(admin)
    def delete_word(self, word_name, field_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        #単語削除
        try:
            query = "delete from in_short.words where word_name = %s; AND field_id = %s"

            cursor.execute(query,(word_name. field_id))
            result = self.connection.commit()
            #削除するものがない時
            if result is None:
                return "nothing"
        except Exception as e:
            #ロールバック
            self.connection.rollback()

            print("Exception error delete_word()")
            print(e)


        finally:
            cursor.close()

        return "delete select"


# hei = AdminManageSql()
# query = "delete from in_short.words where id = %s;"
# result = hei.delete_word(query, 3)
# print(result)
