from redis import Redis
from urllib.parse import urlparse
import ssl

url = 'redis://default:A59DwWke1EahvCkaW3MNCBD7A18kEsmX@redis-18911.c257.us-east-1-3.ec2.cloud.redislabs.com:18911'
url = urlparse(url)

r = Redis(
    host="redis-18911.c257.us-east-1-3.ec2.cloud.redislabs.com", port=18911,
    username="default", # use your Redis user. More info https://redis.io/docs/management/security/acl/
    password="A59DwWke1EahvCkaW3MNCBD7A18kEsmX", # use your Redis password
    ssl=False,
)
r.set('foo', 'bar')
test = r.get('sidequest')


#r = Redis(host=url.hostname, port=url.port, password=url.password, ssl=False, ssl_cert_reqs=ssl.CERT_NONE)
print("redis", r)
print("redis ping", r.ping(), test)