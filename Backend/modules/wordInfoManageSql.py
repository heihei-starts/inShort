from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql

class WordInfoManageSql(ObjectManageSql):

    
    #単語情報取得
    def get_words_info(self, word_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()
        print(word_id)
        print(word_id)
        #単語解説取得
        try:
            # query = 'SELECT e.explanations, e.word_id, e.user_id, count(l.explanation_id) as "good"'\
            #         ' FROM in_short.explanation e '\
            #         ' OUTER JOIN in_short.likes l'\
            #         ' ON e.id = l.explanation_id'\
            #         ' WHERE e.word_id =  %s'\
            #         ' GROUP BY e.id;'
            query = 'SELECT explanations, word_id, user_id FROM in_short.explanation WHERE word_id = %s;'
            cursor.execute(query, (word_id))
            result = cursor.fetchall()
        except Exception as e:
            print("Exception error get_words_info()")
            print(e)
        finally:
            cursor.close()

        return result

    #単語情報投稿
    def post_word_info(self, user_id, word_id, explanation):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()
        
        #単語解説登録
        try:
            query = "INSERT INTO in_short.explanation('explanations', 'word_id', 'user_id')"
            #トランザクションしたい
            cursor.execute(query, (user_id, word_id, explanation))
            self.connection.commit()
        except Exception as e:

            #トランザクション
            self.connection.rollback()

            print("Exception error post_word_info()")
            print(e)

        finally:
            cursor.close()

        return "ok"
    

    #単語情報削除
    def delete_word_info(self, explanation_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        #単語解説削除
        try:
            query = "DELETE FROM in_short.explanation where id = %s"
            cursor.execute(query, (explanation_id))
            self.connection.commit()
        except Exception as e:
            print("Exception error delete_word_info()")
            print(e)

        finally:
            cursor.close()

        return "delete success"

    #単語情報改稿
    def update_word_info(self, change_explanation, explanation_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        #単語解説変更
        try:
            query = "UPDATE in_short.explanation SET explanations = %s where id = %s"

            cursor.execute(query, (change_explanation, explanation_id))
            self.connection.commit()
        except Exception as e:
            print("Exception error update_word_info()")
            print(e)

        finally:
            cursor.close()

        return "update success"

    #ログインユーザーもしくは単語idの存在確認(引数に、ユーザーidか、単語id)
    def check_loginduser_or_exsistedword(self, the_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()

        #ユーザか、単語の存在チェック
        try:
            cursor.execute(query,(the_id))
            #値取り出し
            result = cursor.fetchone()
        except Exception as e:
            print("Exception error check_loginduser_or_exsistedword()")
            print(e)

        finally:
            cursor.close()
        
        #ないときは、どうする？
        return result

