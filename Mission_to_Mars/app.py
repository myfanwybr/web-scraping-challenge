from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo, MongoClient
import test 


app=Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
        space_data=mongo.db.mars_info.find_one()

        return render_template("index.html", space_data=space_data)

@app.route("/scrape")
def scrape():
        mars_dict=test.scrape_info()
        mongo.db.mars_info.replace_one({}, mars_dict, upsert=True)
        return redirect("/")

if __name__=='__main__':
    app.run(debug=True)

