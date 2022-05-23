import MySQLdb

class DBconect:
    
    @classmethod
    def connect(cls):
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
            # cursor = connection.cursor()
            # SQL文を作成
            # 検索条件など動的な情報がある場合は%sで置き換える
            # 動的な情報はタプルで渡します（条件1つでも最後にカンマをつけること！）
            # sql = "SELECT * FROM menu "
            # cursor.execute(sql,)
            # 検索の場合、実行結果を取得
            # rows = cursor.fetchall()
            # for row in rows:
            #     print(row[0],row[1])

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

# 動作確認用
if __name__ == '__main__':
    DBconect.connect()