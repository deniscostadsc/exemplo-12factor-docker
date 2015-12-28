import os

from flask import Flask
from redis import Redis

host_redis=os.environ.get('HOST_REDIS') or 'redis'
port_redis=os.environ.get('PORT_REDIS') or '6379'

app = Flask(__name__)
redis = Redis(host=host_redis, port=port_redis)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
