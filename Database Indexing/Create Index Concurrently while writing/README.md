## Create Index without blocking production writes!
```sql
create index concurrently g on grades(g);
```

While the above query is executing we can **WRITE** in the `grades` table
```sql
insert into grades(g) values(1);
```