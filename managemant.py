# 売り上げ管理
# 実現したいこと
# 一つ一つの既存のメニューに売り上げを入力する
# テーブルを結合し、インプットで入力されたメニュー名とテーブル内のメニュー名が
# 一致する行の売り上げ列に売り上げを更新する



# メニューテーブルと売り上げテーブルを結合させて、取得する


# 取得したすべての行のメニュー名と売り上げを一行づつ取り出した順番で売り上げの更新をする

import MySQLdb

class Management:

    @classmethod
    def connection(cls):
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

            # 売り上げの情報をforで取得
            # 取得した内容をもとにupdateをしていく
            cursor = connection.cursor()
            sql = "SELECT menu.menu_id, menu.menu_name, menu_sales.sales FROM menu INNER JOIN menu_sales ON menu.menu_id = menu_sales.menu_id;"
            rows = cursor.execute(sql)
            rows = cursor.fetchall()
            print('売り上げを更新します')
            for row in rows:
                print(row[1], 'の現在の売り上げ: ', row[2])
                print('↓↓↓↓↓今回の売り上げを入力↓↓↓↓↓')
                num = int(input())
                if type(num) == int:
                    earning = int(row[2]) + int(num)
                    sql = "UPDATE menu_sales SET sales = %s WHERE menu_id = %s"
                    cursor.execute(sql, (earning, row[0]))
                    connection.commit()
                    print('更新後の売り上げ: ', earning)
                    # while True:
                    #     updateConfirm = input('確定したい場合は y 修正したい場合は n を押してください: ')
                    #     if updateConfirm == 'y':
                    #         connection.commit()
                    #         print('更新後の売り上げ: ', earning)
                    #         break
                    #     elif updateConfirm == 'n':
                    #         print('???????????????????????')
                    #     else:
                    #         continue
                else:
                    print('数字で入力してください')
                    break  
                

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

Management.connection()