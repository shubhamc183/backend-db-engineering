import psycopg2
from uhashring import HashRing

CLIENTS = {
    '10001': {
        "host": "localhost",
        "port": "10001",
        "user": "postgres",
        "password": "password",
        "database": "postgres"
    },
    '10002': {
        "host": "localhost",
        "port": "10002",
        "user": "postgres",
        "password": "password",
        "database": "postgres"
    },
    '10003': {
        "host": "localhost",
        "port": "10003",
        "user": "postgres",
        "password": "password",
        "database": "postgres"
    }
}

CONNECTIONS = {}
for _key, _value in CLIENTS.items():
    _ = psycopg2.connect(
        host=_value['host'],
        port=_value['port'],
        database=_value['database'],
        user=_value['user'],
        password=_value['password'])
    _.autocommit = True
    CONNECTIONS[_key] = _.cursor()

HASH_RING = HashRing(nodes=list(CLIENTS.keys()))
