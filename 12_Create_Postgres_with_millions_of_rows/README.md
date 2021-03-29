```
➜ docker run --name pg1 -e POSTGRES_PASSWORD=postgres postgres:13

➜ docker exec -it pg1 psql -U postgres

postgres=# create table temp(t int);

postgres=# insert into temp(t) select random()*100 from generate_series(0, 1000000);

postgres=# select count(*) from temp;
```