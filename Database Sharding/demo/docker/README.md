### Build the image using the command

```
docker build -t pgshard .
```

### Run the Docker container
```
docker run --name pgshard1 -p 10001:5432 -e POSTGRES_PASSWORD=password -d pgshard
docker run --name pgshard2 -p 10002:5432 -e POSTGRES_PASSWORD=password -d pgshard
docker run --name pgshard3 -p 10003:5432 -e POSTGRES_PASSWORD=password -d pgshard
```