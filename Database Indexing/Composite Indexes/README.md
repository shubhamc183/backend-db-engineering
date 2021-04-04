## Composite Index can be made for cases where we plan always query the table using two columns
## table_name(left, right) helpful in doing left=V1 & right=V2 as well as left=V1 query but doesn't index on right
## We can additionally create index(right) too.

```sql
create table example(a integer, b integer, c integer);

# Fill 10 Mil entries
insert into example(a, b, c) select random()*100, random()*100, random()*100  from generate_series(0, 10000000);

# we can create index on a and b
create index idx_example_a on example(a);
create index idx_example_b on example(b);

# but think of a case where you always want to execute the below query
select c from example where a = 10 and b = 20;

# Composite Index he
create index idx_example_a_b on example(a, b);
```