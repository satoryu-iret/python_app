#無限ループで数字のみ受け入れる処理

from lib2to3.refactor import MultiprocessingUnsupported

delete_sql = "SELECT menu_id, menu_name FROM menu"
cursor.execute(delete_sql,)
#全件取得
rows = cursor.fetchall()



while True:
    delete_number = input('削除したいメニューを数字で入力してください')
 
    #menu_idとmenu_nameを格納したい
    for row in rows:
        print(row[0])
        print(row[1])

    if delete_number.isdecimal():
        print('削除する数字は' + delete_number)
        delete_sql = "DELETE FROM menu values(%s)"
        cursor.execute(sql,(delete_number,))
        break
    else:
        print("数字での入力でお願いします。")
#１つずつメニュー名と数字を表示する