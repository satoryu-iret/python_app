from tkinter import E
import MySQLdb
class Delete:
    @classmethod
    def sqlRow(cls):
        connection = None   # DB接続状態
        cursor = None       # テーブル情報
        # DB接続ではエラーが発生する可能性があるためtryブロックで囲みます
        try:
            # DB接続情報を指定
            connection = MySQLdb.connect(
                user='test',
                passwd='test',
                host='localhost',
                db='pythonapp',
            )

            # 接続したDBからテーブルの情報を取得
            cursor = connection.cursor()

            delete_sql = "SELECT menu_id, menu_name FROM menu"
            cursor.execute(delete_sql,)
            #全件取得
            rows = cursor.fetchall()

            
            #無限ループで数字のみ受け入れる処理
            while True:
                
                #１つずつメニュー名と数字を表示する
                for row in rows:
                    print(row[0],row[1])
                delete_number = input('削除したいメニューを数字で入力してください。戻りたい場合はeを入力してください。\n >')

                # #入力された値がmenu_idの数以上の場合に削除するコマンド
                # #実行できないためコメントアウト。
                # if delete_number > len[rows] or delete_number == 0:
                #     print("適切な数値が入力されました。")
                # else:
                #     print("入力された数値は不適切です。")


                #inputで入力された値が整数だった場合
                if delete_number.isdecimal():
                    print('削除する数字は' + delete_number + 'でよろしかったでしょうか？')
                    delete_check = input('yesなら\"y\"、noならそれ以外を入力してください。')
                    
                    #yが入力された場合にのみDELETE文が実行されて、指定されたmenu_idをDBから削除
                    if delete_check == "y":
                        delete_sql = "DELETE FROM menu WHERE menu_id = %s"
                        cursor.execute(delete_sql,(delete_number,))
                        connection.commit()
                        break                    
                    else:
                        print("noが選択されました。")

                #inputで入力された値がeだった場合、無限ループから脱出
                elif delete_number == "e":
                    break

                #inputで入力された値が整数でもなく、eでもない場合
                else:
                    print("数字での入力でお願いします。")


        # 例外処理ブロック
        except Exception as e:
            print(f'DB処理に失敗しました : {e}')
        
        # 必須処理ブロック
        finally:
            # 各接続状態を解除
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

Delete.sqlRow()