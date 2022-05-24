import insert
import delete
import managemant
import sales_display

while True:
    print('---' + 'メニュー管理システム' + '---')
    print('1、メニュー追加')
    print('2、メニュー削除')
    print('3、売上表示一覧')
    print('4、売上管理')
    print('5、終了')
    
    num = int(input('使用したい機能を数字で入力してください>'))


    if num == 1:
        insert.New_Menu.insert_sql()
    
    elif num == 2:
        #メニュー削除処理
        delete.Delete.sqlRow()
        
    elif num == 3:
        #売上表示一覧
        sales_display.SalesDisplay.display()

    elif num == 4:
        #売上管理
        managemant.Management.connection()
    
    elif num == 5:
        print('システムを終了します。お疲れ様でした!')
        break
        
    else:
        print('1～4の数字を入力してください')