```
/* Create a table */
create table grades_org(id serial not null, g integer not null);
insert into grades_org(g) select floor(random()*100) from generate_series(0, 10000000);
create index grades_org_index on grades_org(g);


/* Create Partitions Table */
create table grades_parts(id serial not null, g integer not null) partition by range(g);
create table g0035 (like grades_parts including indexes);
create table g3560 (like grades_parts including indexes);
create table g6080 (like grades_parts including indexes);
create table g80100 (like grades_parts including indexes);


/* Attach partitons one by one */
alter table grades_parts attach partition g0035 for values from (0) to (35);
alter table grades_parts attach partition g3560 for values from (35) to (60);
alter table grades_parts attach partition g6080 for values from (60) to (80);
alter table grades_parts attach partition g80100 for values from (80) to (100);


/* Populate the partitions */
insert into grades_parts select * from grades_org;

/* Let's create index on master/leader partitions */
/* It will also create index on all the sub partitions! */
create index grades_part_idx on grades_parts(g);
```