from flask import Flask
from flask_pymongo import pymongo

app=Flask(__name__)

conn='mongodb://localhost:27017'
client=pymongo.MongoClient(conn)

@app.route("/")
def main():
        return("hello world!")

if __name__=='__main__':
    app.run(debug=True)
