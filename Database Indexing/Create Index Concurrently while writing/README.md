## Create Index without blocking production writes!
```
create index concurrently g on grades(g);
```

While the above query is executing we can **WRITE** in the `grades` table
```
insert into grades(g) values(1);
```