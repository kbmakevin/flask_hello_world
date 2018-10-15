from flask import Flask

# init app var using __name__ attr
app = Flask(__name__)

# define route using Python decorator
@app.route('/')
def hello_world():
    return 'Hello World!'

# normal Python boilerplate to make sure we don't run anything automatically if our code is imported by another Python script
if __name__ == "__main__":
    # starts the development server for Flask and allows us to visit our web application from our local machine by visiting localhost
    app.run()
