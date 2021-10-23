from flask import Flask, jsonify
from modules.objectManageSql import ObjectManageSql


class WordManageSql(ObjectManageSql):

    
    #単語取得
    def selectAllWords(self, query):
        
        #カーソルオブジェクト(DBを管理するオブジェクト) 呼び出し
        cursor  = self.connection.cursor()
        
        #全件取得
        try:
            cursor.execute(query)
            #値取り出し
            result = cursor.fetchall()

        except Exception as e:
            print("Exception error selectAllWords()")
            print(e)

        finally:
            cursor.close()
    
        return result
        

    #単語追加(adminにあとで移動。)
    
    #引数に、単語と単語のジャンル
    def insert_word(self, query, word, field_id):

        #カーソルオブジェクト呼び出し
        cursor = self.connection.cursor()
        
        #単語追加
        try:
            
            cursor.execute(query,(word, field_id))
            self.connection.commit()
        except Exception as e:
            print("Exception error insert_word()")
            print(e)
        finally:

            cursor.close()
        
        return "success"
  

# query = "insert into in_short.words (word_name, field_id) values (%s, %s)"
# word = "OSI参照モデル"
# field_id = 2
# result = hei.insert_word(query, word, field_id)
# print(result)

#hei = WordManageSql()
