print('---' + 'メニュー管理システム' + '---')
print('1、メニュー追加')
print('2、メニュー削除')
print('3、売上表示一覧')
print('4、売上管理')
print('5、終了')


import input1

while True:
    num = int(input('使用したい機能を数字で入力してください>'))
    if num == 1:

        # メニュー追加処理
        New_Menu.insert_sql()
    
    elif num == 2:

        #メニュー削除処理
        print(2)
    elif num == 3:
        #売上表示一覧
        print(3)

    elif num == 4:
        #売上管理
        print(4)
    
    elif num == 5:
        print('システムを終了します。お疲れ様でした!')
        break
        
    else:
        print('1～4の数字を入力してください')