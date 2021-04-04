## Master/Standy Replication
Master takes all the WRITES whereas all the READS are executed by STANDY/REPLICAS

## Synchronous vs Asynchronous Replication
- Synchronous
  - Client is held till the WRITE is done on master and all other different REPLICAS
  - Some DB gives option like write to first 2
  - **It holds the client for longer time**
- Asynchronous
  - Client only WRITES to the master
  - Master propagates the changes to REPLICAS
  - Example of **EVENTUAL CONSISTENCY**
Depends upon the engineer if they can bear READS on stale data like
- Number of likes on a tweet, fb post
- Number of followers

## Pros
- Horizontal Scaling
- Region based queries - DB per region

## Cons
- EVENTUAL CONSISTENCY
- Slow Writes (Synchronous)
- Complex to Implement (multi-master)
