## Intro to Database Engineering by [hnasr](https://github.com/hnasr)
Notes from https://www.udemy.com/course/database-engines-crash-course/

# Database Learnings
- Update your database statistics often or your SQL queries will suffer #shorts
    - Suppose your table have 10 rows and an operation does 1M entries, the next subsequent queries will do full table scan
    - Update table statistics instantly to let the table know new major operations done
    - https://www.youtube.com/watch?v=QClK86lZ0Vo
- Always release the connection pool after a transcation!
    - Or just use `pool.query()` for smaller operation like read, filters.
    - https://www.youtube.com/watch?v=KGbwkbaCwss
- Never use uuid as Primary Key
    - More Randomness and pages need to be pulled into Memory(DB always write in-memory and then WAL) and existing pages will be flushed
    - https://youtu.be/uFbMtOdjEOE?t=1134

# Node.js
- `fetch`
    - Keeps the `body` in `ReadleStream`
    - Nevers parses the body which is quicker as I may be only interested in `headers`, `status_code`, etc
    - If the body is too large and we require to see only limited body then we can read in it stream fashion
    - https://www.youtube.com/watch?v=yk7oeFZ8iPE