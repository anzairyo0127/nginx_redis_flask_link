import redis

r = redis.StrictRedis(host='redis_ctr', port=6379, db=0)

r.set('hoge', 'moge')

hoge = r.get('hoge')
print(hoge.decode())
