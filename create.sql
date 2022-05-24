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
INSERT INTO menu (menu_name,price) values('�L�q',400);
INSERT INTO menu (menu_name,price) values('�G�r�`��',780);
INSERT INTO menu (menu_name,price) values('�`���[�n��',550);
INSERT INTO menu (menu_name,price) values('���ܒc�q',320);
INSERT INTO menu (menu_name,price) values('�o�j���A�C�X',250);
INSERT INTO menu (menu_name,price) values('�ǐm����',300);
INSERT INTO menu (menu_name,price) values('�G����',300);
INSERT INTO menu (menu_name,price) values('�W���X�~���e�B�[',300);
INSERT INTO menu (menu_name,price) values('�R�[��',350);
INSERT INTO menu (menu_name,price) values('�u������',300);
INSERT INTO menu (menu_name,price) values('���q�l�Z�b�g(�L�q,�`���[�n��)',500);



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

