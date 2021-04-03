create table seat(id serial primary key not null, isbooked boolean, name varchar);
insert into seat values(1);
insert into seat values(2);

/* Now if two process at same time checked seat id = 1 and will find that it's unbooked */
begin transaction;
select * from seat where id = 1;
update seat set isbooked=true, name='Jesse' where id = 1;
commit;

/* Process running in Parallel */
/* It will update th seat to someone else */
begin transaction;
select * from seat where id = 1;
update seat set isbooked=true, name='Heisenberg' where id = 1;
commit;

/* An Exclusive Lock can be acquired while checking the status of Seat itself */
/* Process running in Parallel */
begin transaction;
select * from seat where id = 1 for update;
update seat set isbooked=true, name='Sheldon' where id = 2;
commit;

-- Now an another process in parallel is locked until the above locked is release
-- So, that there is no problem of double booking!