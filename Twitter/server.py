#PS C:\Users\LENOVO\desktop\Githubrepos\Python\Twitter> python server.py

from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("hello world")
    return "hello world"

if __name__== "__main__":
    app.run(debug= True)