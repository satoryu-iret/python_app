new_menu = str(input('追加するメニュー名を入力してください:'))
print(new_menu)

new_price = int(input('価格を半角数字で入力してください:'))
print(new_price)


new_menu_price = ('new_menu','price')

insert_sql = "INSERT INTO menu(menu_name,price) values(%s,%s)"
cursor.execute(insert_sql,(new_menu,new_price,))