use pythonapp;

set names sjis;

DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS menu_sales;

CREATE TABLE menu (
  menu_id int NOT NULL AUTO_INCREMENT,
  menu_name     varchar(20) NOT NULL,
  price int NOT NULL,
  PRIMARY KEY  (menu_id)
);

CREATE TABLE menu_sales (
  menu_id int NOT NULL AUTO_INCREMENT,
  sales int NOT NULL,
  PRIMARY KEY  (menu_id)
);


INSERT INTO menu (menu_name,price) values('???k????',820);
INSERT INTO menu (menu_name,price) values('???[????',750);
INSERT INTO menu (menu_name,price) values('????',800);
INSERT INTO menu (menu_name,price) values('餃子',400);
INSERT INTO menu (menu_name,price) values('エビチリ',780);
INSERT INTO menu (menu_name,price) values('チャーハン',550);
INSERT INTO menu (menu_name,price) values('ごま団子',320);
INSERT INTO menu (menu_name,price) values('バニラアイス',250);
INSERT INTO menu (menu_name,price) values('杏仁豆腐',300);
INSERT INTO menu (menu_name,price) values('烏龍茶',300);
INSERT INTO menu (menu_name,price) values('ジャスミンティー',300);
INSERT INTO menu (menu_name,price) values('コーラ',350);
INSERT INTO menu (menu_name,price) values('爽健美茶',300);
INSERT INTO menu (menu_name,price) values('お子様セット(餃子,チャーハン)',500);



INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);

select * from menu;
select * from menu_sales;

-- INSERT INTO test_user (name,password) values ('tom','tom123');
-- INSERT INTO test_user (name,password) values ('bob','bob123');
-- INSERT INTO test_user (name,password) values ('mike','mike123');

-- select * from test_user;

