from flask import Flask, jsonify, request
import csv
all_articles = []
with open("articles.csv") as file:
    reader = csv.reader(file) 
    data = list(reader)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []
did_not_read = []
app = Flask(__name__)
if __name__ == "__main__":
    app.run()
@app.route("/get-articles")
def get_movie():
    return jsonify({
        "data":all_articles[0],
        "status": "success"
    })
@app.route("/did-not-read", methods = ["POST"])
def did_not_read():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    did_not_read.append(articles)
    return jsonify({
        "status":"success"
    }),200