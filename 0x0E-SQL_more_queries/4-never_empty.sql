-- creates the table id_not_null on my MySQL server if it doesn't exist
-- With columns id INT with the default value 1 & name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command:
-- >>  cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2

CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
