import MySQLdb
class SalesDisplay:

    @classmethod
    def display(cls):
        print("-------売り上げの一覧表示です-------")
        connection = None   # DB接続状態
        cursor = None       # テーブル情報
        # DB接続ではエラーが発生する可能性があるためtryブロックで囲みます
        try:
            connection,cursor = SalesDisplay.connect_db()
            sql = "SELECT menu.menu_id, menu_name, price * sales FROM menu INNER JOIN menu_sales ON menu.menu_id = menu_sales.menu_id"
            cursor.execute(sql,)
            rows = cursor.fetchall()
            for row in rows:
                print(row[0],row[1],"の売り上げは",row[2],"円です")
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

    @classmethod
    def  connect_db(cls):
        connection = None   # DB接続状態
        cursor = None       # テーブル情報
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
        # 例外処理ブロック
        except Exception as e:
            print(f'DB接続にに失敗しました : {e}')

        return connection,cursor

SalesDisplay.display()

