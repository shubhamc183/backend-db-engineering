### Database Partitioning
Spilting a table into many smaller table

Eg; A table with 10M rows can be divided into 5 tables which will have rows as
- Partition1; 0-2M id
- Partition2; 2-4M id
- Partition3; 4-6M id
- Partition4; 6-8M id
- Partition5; 8-10M id

### Veritcal vs Horizontal Partitioning
* Horizontal
  * Range or List
* Veritcal Partitioning splits columns partitions
  * Large column(blob) that you can store in a slow access drive

### Partitioning Types
1. By Range - Date, ids
2. By List - Discrete value; Zip codes, State
3. By Hash - Hash functions

### Horizontal Partitioning vs Sharding
- HP splits a big table into multiple smaller tables in the same DB; headache of DB; client is agnostic
- Sharding splits big table into multiple tables across multiple DB servers
- In HP tables names changes (or schema)
- Sharding everything is same but server changes

### Pros of Partitioning
1. Improves query peroformance when accessing a single partition
2. Easy bulk loading
3. Archive old data that are barely touched into cheap storage

### Cons of Partitioning
1. Update can move a row from one partition to another
2. Inefficient queries can accidently query multiple partitions
3. Schema changes are hard to maintain across partitions