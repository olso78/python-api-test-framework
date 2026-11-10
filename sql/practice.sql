-- create database test_bootcamp;
use test_bootcamp;
-- DROP TABLE IF EXISTS words;
-- create table words(
--     id int primary key auto_increment,
--     word varchar(50) not null ,
--     freq int not null,
--     created_at datetime default current_timestamp,
--     unique(word)
-- )default charset = utf8mb4;

-- insert into words(word,freq) values('apple', 10),('banana', 20),('orange', 30);
-- select word from words where freq > 2;
-- update words set freq = 2 where word = 'apple';
-- delete from words where word = 'apple' and freq = 2;
-- select word,freq from words order by freq desc limit 10;

-- select freq,count(*) from words GROUP BY freq HAVING count(*) > 1;
-- select word from words group by word having left(word,1) = 'a' and count(*) > 1;
Start TRANSACTION;
INSERT INTO words(word,freq) values ('temp',99);
select * from words;
Rollback;
select * from words;
Start TRANSACTION;
INSERT INTO words (word, freq) VALUES ('real', 88);
COMMIT;
Rollback;
select * from words;