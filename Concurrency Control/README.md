## Exclusive Lock
No other can read and write on that row. Only one Exclusive lock can obtained on a row at once!

No Shared Lock should be present to take an Exclusive lock.

## `for update` to acquire Exclusive lock on the row in Postgres

```select * from seat where id = 100 for update```

## Shared Lock
Other operations can only read from a row but cannot write in that row. Multiple transcations can take Shared Lock in a row.

Exclusive lock cannot be taken if the row has Shared Lock(s)

## NEVER USE `OFFSET` as it just skips the rows
https://use-the-index-luke.com/no-offset
Never use `OFFSET` for pagination as it slows the performance of client
```sql
select name from student offset 10000000 limit 10;
```
It will actually pick the 10M + 10 rows and skip the first 10M rows which is very bad.

## OFFSET VS Seek method or keyset pagination
```sql
select id from student order by id desc limit 10;
-- Pick the last ID and use in the below manner
select name from student where id < LAST_ID_NUMBER_FROM_ABOVE_RESULT order by id desc limit 10;
```

## Maintain Pool of D/B connections
Instead of starting and closing TCP connections to save time

## Serializable vs Repeated Read
```sql
begin transaction isolation level serializable;
```

## Types of Isolation
```sql
---  No isolation
begin transaction isolation level read uncommitted;

--- DEFAULT; Queries in the transaction only sees committed stuff;
begin transaction isolation level read committed;

---  Queries in the transaction only sees committed some before start of this transaction
begin transaction isolation level repeatable read;

--- Transactions are serialized
begin transaction isolation level serializable;
```