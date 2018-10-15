import time

import redis
from flask import Flask

# init app var using __name__ attr
app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

# ROUTES
# define route using Python decorator
@app.route('/')
def hello_world():
    count=get_hit_count()
    return 'Hello World! I have been visited {} times.'.format(count)

# FUNCS
def get_hit_count():
    retries=5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries-=1
            time.sleep(0.5)

# normal Python boilerplate to make sure we don't run anything automatically if our code is imported by another Python script
if __name__ == "__main__":
    # starts the development server for Flask and allows us to visit our web application from our local machine by visiting localhost
    app.run(host='0.0.0.0', debug=True)
