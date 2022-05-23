#無限ループで数字のみ受け入れる処理
while True:
    delete_number = input('削除したいメニューを数字で入力してください')
    if delete_number.isdecimal():
        print('削除する数字は' + delete_number)
        delete_sql = "DELETE INTO menu(menu_id) values(%s,%s)"
        break
    else:
        print("数字での入力でお願いします。")
#SQLからどうやって貰った値を紐づける？