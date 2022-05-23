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


INSERT INTO menu (menu_name,price) values('ñÉîkì§ïÖ',820);
INSERT INTO menu (menu_name,price) values('ÉâÅ[ÉÅÉì',750);
INSERT INTO menu (menu_name,price) values('âÒìÁì˜',800);

INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);
INSERT INTO menu_sales (sales) values(0);


select * from menu;
select * from menu_sales;

-- INSERT INTO test_user (name,password) values ('tom','tom123');
-- INSERT INTO test_user (name,password) values ('bob','bob123');
-- INSERT INTO test_user (name,password) values ('mike','mike123');

-- select * from test_user;

