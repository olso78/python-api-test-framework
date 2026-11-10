create database test_bootcamp;
use test_bootcamp;
create table words(
    id int primary key auto_increment,
    word varchar(10) not null ,
    freq int not null,
    created_at datetime default current_timestamp
);
insert into words(word,freq) values('apple', 10),('banana', 20),('orange', 30),('apple', 40),('banana', 50),('apple', 60);
select word from words where freq > 2;
update words set freq = 2 where word = 'apple';
delete from words where word = 'apple' and freq = 60;
select word,freq from words order by freq desc limit 10;