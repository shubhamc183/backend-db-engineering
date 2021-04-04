## Cursors
Cursor is a Temporary Memory or Temporary Work Station. It is Allocated by Database Server at the Time of Performing DML operations on Table by User. Cursors are used to store Database Tables.

### Pros
- Save memory on Client side by fetching limited rows, processing them, dropping them, and then asking more rows instead of all rows at once.
- Streaming
- Cancelling a big query if ahead is not required

### Cons
- Stateful i.e it'll hold resources
- Long waiting transactions

## Server Side vs Client Side Cursor
- Server Side
  - Created on the DB
  - Only when the cursor asks the results are fetched.
  - The server-side cursor returns only the requested data over the network.
  - DB still has open connection to Client(Pythpon/NodeJs/...)
- Client Side Cursor
  - The server-side cursor returns the **whole data** requested data over the network.
  - DB is released at once and everything is handled by Client.