## Transaction
- A collection of queries
- One unit of work

## Atomoicity
- All queries must succeed. If one fails all should rollback.

## Isolation
Can my inflight transaction see changes made by other transactions?

Read Phenomena
- Dirty Reads
  - Reading something which is not yet committed and can be rollback
  - A dirty read (aka uncommitted dependency) occurs when a transaction is allowed to read data from a row that has been modified by another running transaction and not yet committed.
- Non-Repeatable Reads
  - A non-repeatable read is one in which data read twice inside the same transaction cannot be guaranteed to contain the same value. Depending on the isolation level, another transaction could have nipped in and updated the value between the two reads.
- Phantom Read
  - A phantom read occurs when, in the course of a transaction, new rows are added or removed by another transaction to the records being read. This can occur when range locks are not acquired on performing a SELECT ... WHERE operation.

### Isolation Levels for inflight transaction
- Read Uncommited
  - No isolation, any change from the outside is visible to the transaction
- Read Committed
  - Each query in transaction only sees committed stuff
  - This is default in Postgres.
  - `begin transaction isolation level read committed;`
- Repeatable Read
  - Each query in transaction only sees committed updates at the beginning of transcation
  - `begin transaction isolation level repeatable read;`
- Serializable
  - Transaction are serialized
  - `begin transaction isolation level serializable;`

## NOTE
In Postgres `isolation level repeatable read` helps to tackle Phantom reads

## Consistency
- Consistency in Data
  - If a table says Person X has 10 followers then the followers table should have 10 followers of X.
- Consistency in Reads
  - If a transcation committed a change will a new transcation immediately see the change?
  - Relational and NoSQL databases both suffer from this
  - Eventual Consistency

## Durability
Committed transaction must be persisted in a durable non-volatile storage.

## Eventual Consistency
- The updated value in a the master will be eventually committed to other nodes and this is called "Eventual Consistency"
- Both Relational and NoSQL databases suffer from this
- It's upto the Engineer if they can tolerate this.
- Ex.
  - Number of Likes for a post
  - Number of followers
