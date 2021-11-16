from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql

class LikeSql(ObjectManageSql):

    #いいね追加
    def postLike(self, user_id, explanation_id):
        #カーソルオブジェクト（DBを管理する）呼び出し
        cursor = self.connection.cursor()


        #いいね追加
        try:
            query = "INSERT INTO in_short.likes (user_id, explanation_id) VALUES (%s,%s);"
            cursor.execute(query, (user_id, explanation_id))
            self.connection.commit()
        except Exception as e:
            
            #ロールバック
            self.connection.rollback()

            print("Exception error addLike()")
            print(e)
        finally:
            cursor.close()

        return "add_like"

            
        
    #ユーザーごとに、いいねしている値を返す。

    def getLike(self, query, explanation_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        try:
            query = "SELECT explanation_id, COUNT(explanation_id) FROM in_short.likes WHERE word_id = %s GROUP BY explanation_id;"
            cursor.execute(query,(explanation_id))
            #値取り出し
            result = cursor.fetchall()
        except Exception as e:
            
            print("Exception error getLike()")
            print(e)

        finally:
            cursor.close()

        return result


    #いいね削除
    def deleteLike(self, user_id, explanation_id):
        #カーソルオブジェクト（DBを管理する）呼び出し
        cursor = self.connection.cursor()
        

        #いいね削除
        try:
            query = "DELETE FROM in_short.likes WHERE user_id = %s and explanation_id = %s"
            cursor.execute(query, (user_id, explanation_id))
            self.connection.commit()
        except Exception as e:
            
            #ロールバック
            self.connection.rollback()

            print("Exception error deleteLike()")
            print(e)
        finally:
            cursor.close()
        
        return "delete_like"



