from flask import render_template, request, url_for, flash, redirect
from Bookmarker_landing_Page.config import app

@app.route("/")
def landing():
    return render_template("landing_page.html")


@app.route("/guide")
def guide():
    return render_template("guide.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dashboard", methods=['GET', 'POST'])
def bookmarks():
    return render_template("bookmarks.html")


@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route("/bookmark", methods=['GET', 'POST'])
def bookmark():
    return render_template("bookmark.html",)


@app.route("/features", methods=['GET', 'POST'])
def features():
    return render_template("features.html")

if __name__ == "__main__":
    app.run(debug=True)
