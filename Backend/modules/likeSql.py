from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql

class LikeSql(ObjectManageSql):

    #いいね追加
    def postLike(self, query, user_id, explanation_id):
        #カーソルオブジェクト（DBを管理する）呼び出し
        cursor = self.connection.cursor()


        #いいね追加
        try:
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
    def deleteLike(self, query, user_id, explanation_id):
        #カーソルオブジェクト（DBを管理する）呼び出し
        cursor = self.connection.cursor()
        

        #いいね削除
        try:
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



