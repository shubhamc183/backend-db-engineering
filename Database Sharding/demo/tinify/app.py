import base64
import hashlib
from db import CONNECTIONS, HASH_RING


def handle_get(request):
    tinyurl = request.args['tinyurl']
    shard = HASH_RING.get_node(tinyurl)
    CONNECTIONS[shard].execute('SELECT url FROM URL_TABLE where tinyurl = %s', (tinyurl, ))
    result = CONNECTIONS[shard].fetchall()
    response = {'tinyurl': tinyurl, 'shard': shard}
    if result != []:
      response['url'] = result[0][0]
    return response

def handle_post(request):
    url = request.args['url']
    _hash = base64.b64encode(hashlib.sha256(url.encode('utf-8')).digest())
    tinyurl = _hash.decode("utf-8")[0:5]
    shard = HASH_RING.get_node(tinyurl)
    CONNECTIONS[shard].execute(
        'INSERT INTO URL_TABLE(url, tinyurl) values (%s, %s)', (url, tinyurl))
    return {
        'url': url,
        'tinyurl': tinyurl,
        'shard': shard
    }
