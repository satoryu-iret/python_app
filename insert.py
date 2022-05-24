import MySQLdb


class New_Menu:
    def __init__(self, new_menu, new_price):
        self.new_menu = new_menu
        self.new_price = new_price
    
    @classmethod
    def insert_sql(cls):
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
        

            new_menu = str(input('追加するメニュー名を入力してください:'))
            print(new_menu)

            new_price = int(input('価格を半角数字で入力してください:'))
            print(new_price)


            insert_sql = "INSERT INTO menu (menu_name, price) values(%s,%s)"
            cursor.execute(insert_sql,(new_menu, new_price,))
            insert_sales = "INSERT INTO menu_sales (sales) values(0)"
            cursor.execute(insert_sales)
            connection.commit()
            

            print(new_menu + '(' + str(new_price) +')' +'を新メニューとして追加しました。')

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



# New_Menu.insert_sql()
