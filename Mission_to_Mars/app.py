from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape


app=Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
        space_data=mongo.db.collection.find_one()

        return render_template("index.html", mars=space_data)

@app.route("/scrape")
def scrape():
        mars_data=mars_scrape.scrape_info()
        mongo.db.collection.update({}, mars_data, upsert=True)
        return redirect("/")

if __name__=='__main__':
    app.run(debug=True)
