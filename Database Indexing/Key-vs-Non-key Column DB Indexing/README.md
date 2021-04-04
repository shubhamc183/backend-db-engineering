## Use `include` column in index to perform `Index Only` scan instead of `Index Scan`!!

## Index create B tree
```sql
# Size of all DBs;
select pg_relation_size(oid)/(1024*1024) || 'MB', relname from pg_class order by pg_relation_size(oid) desc;

create table grade(id serial primary key, g integer, name character(10));

## Adding 10M series
insert into grade(g, name) select random()*100, substr(md5(random()::text), 0, 10) from  generate_series(0, 10000000);

create index g_idx on grade(g);
## Size of g_idx is 68MB

## Index Scan as name is not present in the index g_idx ~500ms
explain analyze select name from grade where g = 56;

drop index g_idx;

# Include name
create index g_idx on grade(g) include (name);
## Now, the Size of g_idx is 330MB almost 4.5 times

## Since name is present in the index that's why this query is Index Only Scan ~50ms
explain analyze select name from grade where g = 56;
```