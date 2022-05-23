print('---' + 'メニュー管理システム' + '---')
print('1、メニュー追加')
print('1、メニュー削除')
print('3、売上表示一覧')
print('4、売上管理')
print('5、終了')

while True:
    num = input('使用したい機能を数字で入力してください>')
    if str(num) == 1:
        #メニュー追加処理
    
    elif str(num) == 2:
        #メニュー削除処理
       
    elif str(num) == 3:
        #売上表示一覧

    elif str(num) == 4:
        #売上管理
    
    elif str(num) == 5:
        print('システムを終了します。お疲れ様でした!')
        break
        
    else :
        print('1～4の数字を入力してください')